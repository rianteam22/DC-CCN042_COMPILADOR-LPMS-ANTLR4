from gen.GramaticaVisitor import GramaticaVisitor
from gen.GramaticaParser import GramaticaParser

class SemanticError(Exception):
    def __init__(self, message, line):
        super().__init__(f"Erro Semântico: {message} na linha {line}")
        self.line = line

# Definição das classes de nós da AST
class BinaryOpNode:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __str__(self):
        return f"BinaryOpNode(operator={self.operator}, left={self.left}, right={self.right})"

class LiteralNode:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"LiteralNode(value={self.value})"

class VariableNode:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"VariableNode(name={self.name})"

class AssignmentNode:
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

    def __str__(self):
        return f"AssignmentNode(variable={self.variable}, value={self.value})"

class PrintNode:
    def __init__(self, expressions):
        self.expressions = expressions

    def __str__(self):
        expressions_str = ", ".join(str(expr) for expr in self.expressions)
        return f"PrintNode(expressions=[{expressions_str}])"

class InputNode:
    def __init__(self, variables):
        self.variables = variables

    def __str__(self):
        return f"InputNode(variables={self.variables})"

class IfNode:
    def __init__(self, condition, true_block, false_block=None):
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block

    def __str__(self):
        true_str = ", ".join(str(cmd) for cmd in self.true_block)
        false_str = ""
        if self.false_block:
            false_str = ", ".join(str(cmd) for cmd in self.false_block)
        return f"IfNode(condition={self.condition}, true_block=[{true_str}], false_block=[{false_str}])"

class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __str__(self):
        body_str = ", ".join(str(cmd) for cmd in self.body)
        return f"WhileNode(condition={self.condition}, body=[{body_str}])"

class BooleanOpNode:
    def __init__(self, operator, left, right=None):
        self.operator = operator
        self.left = left
        self.right = right

    def __str__(self):
        if self.operator == '!':  
            return f"BooleanOpNode(operator={self.operator}, left={self.left})"
        elif self.right is not None:  
            return f"BooleanOpNode(operator={self.operator}, left={self.left}, right={self.right})"
        else:
            raise ValueError(f"Invalid BooleanOpNode with operator {self.operator} and operands {self.left}, {self.right}")

def format_list(elements, level=0):
    indent = "  " * level
    return ", ".join(indent + str(element) for element in elements)

# Lista de palavras reservadas
RESERVED_WORDS = {"if", "else", "while", "print", "input", "int", "float", "bool", "str", "true", "false"}


class ASTConstrutor(GramaticaVisitor):
    def __init__(self):
        self.symbol_table = {}  # Tabela de símbolos para armazenar tipo e valor

    def visitProg(self, ctx: GramaticaParser.ProgContext):
        return self.visit(ctx.main())

    def visitMain(self, ctx: GramaticaParser.MainContext):
        program_name = ctx.VARNAME().getText()
        declarations = [self.visit(dec) for dec in ctx.decVar()]
        commands = [self.visit(cmd) for cmd in ctx.comandos()]
        return f"({program_name} (Declarations: {self.format_ast(declarations)}) (Commands: {self.format_ast(commands)}))"

    def visitDecVar(self, ctx: GramaticaParser.DecVarContext):
        if ctx.varDecl():
            return self.visit(ctx.varDecl())
        elif ctx.constDecl():
            return self.visit(ctx.constDecl())

    def visitVarDecl(self, ctx: GramaticaParser.VarDeclContext):
        var_type = ctx.VARTYPE().getText()
        variables = [var.getText() for var in ctx.VARNAME()]
        default_values = {
            "int": 0,
            "float": 0.0,
            "bool": False,
            "str": ""
        }
        for var in variables:
            if var in self.symbol_table:
                raise SemanticError(f"Variável '{var}' já declarada", ctx.start.line)
            if var in RESERVED_WORDS:
                raise SemanticError(f"'{var}' é palavra reservada e não pode ser usada como identificador", ctx.start.line)
            self.symbol_table[var] = {"type": var_type, "value": default_values[var_type]}
        return f"(DeclVar: {var_type} {', '.join(variables)})"

    def visitConstDecl(self, ctx: GramaticaParser.ConstDeclContext):
        constants = []
        for i in range(len(ctx.VARNAME())):
            var_name = ctx.VARNAME(i).getText()
            if var_name in self.symbol_table:
                raise SemanticError(f"Constante '{var_name}' já declarada", ctx.start.line)
            if var_name in RESERVED_WORDS:
                raise SemanticError(f"'{var_name}' é palavra reservada e não pode ser usada como identificador", ctx.start.line)
            value = self.visit(ctx.getChild(2 * i + 2))
            self.symbol_table[var_name] = {"type": "const", "value": value}
            constants.append(f"{var_name} = {value}")
        return f"(DeclConst: {', '.join(constants)})"
    
    
    def visitComandos(self, ctx: GramaticaParser.ComandosContext):
        commands = [self.visit(cmd) for cmd in ctx.comando()]
        return f"{self.format_ast(commands)}"

    def visitOpMath(self, ctx: GramaticaParser.OpMathContext):
        var_name = ctx.VARNAME().getText()
        if var_name not in self.symbol_table:
            raise SemanticError(f"Variável '{var_name}' não declarada", ctx.start.line)
        if self.symbol_table[var_name]["type"] == "const":
            raise SemanticError(f"Não é possível atribuir valor à constante '{var_name}'", ctx.start.line)
        
        var_type = self.symbol_table[var_name]["type"]
        value_node = ctx.expressao() or ctx.expressaoBooleana()
        value = self.visit(value_node)
        
         # Verificação de tipo e avaliação da expressão
        try:
            eval_value = eval(value, {}, {k: v["value"] for k, v in self.symbol_table.items()})
        except:
            raise SemanticError(f"Erro ao avaliar a expressão '{value}'", ctx.start.line)

        if var_type == "int" and not isinstance(eval_value, int):
            raise SemanticError(f"Não é possível atribuir valor não inteiro '{value}' à variável inteira '{var_name}'", ctx.start.line)
        elif var_type == "float" and not isinstance(eval_value, float):
            raise SemanticError(f"Não é possível atribuir valor não flutuante '{value}' à variável flutuante '{var_name}'", ctx.start.line)
        elif var_type == "bool" and value not in ["true", "false"]:
            raise SemanticError(f"Não é possível atribuir valor não booleano '{value}' à variável booleana '{var_name}'", ctx.start.line)
        elif var_type == "str" and not isinstance(eval_value, str):
            raise SemanticError(f"Não é possível atribuir valor não string '{value}' à variável string '{var_name}'", ctx.start.line)
        

        self.symbol_table[var_name]["value"] = eval_value
        return f"(Atribuição: {var_name} = {value})"

    def visitFuncprint(self, ctx: GramaticaParser.FuncprintContext):
        expressions = [self.visit(expr) for expr in ctx.expressao()]
        for expr in expressions:
            if isinstance(expr, (int, float, bool, str)) or expr == None:
                continue
            else:
                raise SemanticError(f"Tipos incompatíveis na função print: {expr}", ctx.start.line)
        return f"(Imprimir: {', '.join(map(str, expressions))})"


    def visitFuncinput(self, ctx: GramaticaParser.FuncinputContext):
        variables = [var.getText() for var in ctx.VARNAME()]
        for var in variables:
            if var not in self.symbol_table:
                raise SemanticError(f"Variável '{var}' não declarada", ctx.start.line)
        return f"(Entrada: {', '.join(variables)})"

    def visitCondicional(self, ctx: GramaticaParser.CondicionalContext):
        condition = self.visit(ctx.expressaoBooleana())
        if not isinstance(condition, bool):
            raise SemanticError(f"Condição {condition} do 'if' não é booleana: {condition}", ctx.start.line)
        true_block = [self.visit(cmd) for cmd in ctx.comandos(0).comando()]
        false_block = []
        if ctx.comandos(1):
            false_block = [self.visit(cmd) for cmd in ctx.comandos(1).comando()]
        return f"(Se: {condition} (BlocoVerdadeiro: {self.format_ast(true_block)}) (BlocoFalso: {self.format_ast(false_block)}))"

    def visitCmdWhile(self, ctx: GramaticaParser.CmdWhileContext):
        condition = self.visit(ctx.expressaoBooleana())
        if not isinstance(condition, bool):
            raise SemanticError(f"Condição {condition} do 'while' não é booleana: {condition}", ctx.start.line)
        body = [self.visit(cmd) for cmd in ctx.comandos().comando()]
        return f"(Enquanto: {condition} (Corpo: {self.format_ast(body)}))"


    def visitExpressao(self, ctx: GramaticaParser.ExpressaoContext):
        if ctx.expressaoAritmetica():
            return self.visit(ctx.expressaoAritmetica())
        elif ctx.STRING():
            return ctx.STRING().getText() 
        else:
            raise SemanticError("Expressão inválida", ctx.start.line)

    def visitExpressaoAritmetica(self, ctx: GramaticaParser.ExpressaoAritmeticaContext):
        result = self.visit(ctx.termo(0))
        for i in range(1, len(ctx.termo())):
            operator = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.termo(i))
            result = f"({result} {operator} {right})"
        return result

    def visitExpressaoBooleana(self, ctx: GramaticaParser.ExpressaoBooleanaContext):
        if ctx.VALBOOL():
            return ctx.VALBOOL().getText()
        elif ctx.getChildCount() == 3:
            left = self.visit(ctx.expressaoAritmetica(0) or ctx.expressaoBooleana(0))
            operator = ctx.getChild(1).getText()
            right = self.visit(ctx.expressaoAritmetica(1) or ctx.expressaoBooleana(1))
            return f"({left} {operator} {right})"
        elif ctx.getChildCount() == 2:
            operator = ctx.getChild(0).getText()
            operand = self.visit(ctx.expressaoBooleana(0))
            return f"({operator} {operand})"

    def visitTermo(self, ctx: GramaticaParser.TermoContext):
        result = self.visit(ctx.fator(0))
        for i in range(1, len(ctx.fator())):
            operator = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.fator(i))
            result = f"({result} {operator} {right})"
        return result

    def visitFator(self, ctx: GramaticaParser.FatorContext):
        if ctx.VARNAME():
            var_name = ctx.VARNAME().getText()
            if var_name not in self.symbol_table:
                raise SemanticError(f"Variável '{var_name}' não declarada", ctx.start.line)
            return var_name
        elif ctx.VALINT():
            return ctx.VALINT().getText()
        elif ctx.VALFLOAT():
            return ctx.VALFLOAT().getText()
        elif ctx.expressaoAritmetica():
            return f"({self.visit(ctx.expressaoAritmetica())})"

    def format_ast(self, elements):
        return " ".join(elements)
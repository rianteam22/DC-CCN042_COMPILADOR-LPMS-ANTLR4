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

class ASTConstrutor(GramaticaVisitor):
    def __init__(self):
        self.symbol_table = {} 

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
        for var in variables:
            if var in self.symbol_table:
                raise SemanticError(f"Variável '{var}' já declarada", ctx.start.line)
            self.symbol_table[var] = var_type
        return f"(DeclVar: {var_type} {', '.join(variables)})"

    def visitConstDecl(self, ctx: GramaticaParser.ConstDeclContext):
        constants = []
        for i in range(len(ctx.VARNAME())):
            var_name = ctx.VARNAME(i).getText()
            value = self.visit(ctx.getChild(2 * i + 2))
            if var_name in self.symbol_table:
                raise SemanticError(f"Constante '{var_name}' já declarada", ctx.start.line)
            self.symbol_table[var_name] = "const"
            constants.append(f"{var_name} = {value}")
        return f"(DeclConst: {', '.join(constants)})"
    
    def visitComandos(self, ctx: GramaticaParser.ComandosContext):
        # print("visitComandos")
        commands = [self.visit(cmd) for cmd in ctx.comando()]
        return f"{self.format_ast(commands)}"

    def visitOpMath(self, ctx: GramaticaParser.OpMathContext):
        var_name = ctx.VARNAME().getSymbol().text
        if var_name not in self.symbol_table:
            raise SemanticError(f"Variável '{var_name}' não declarada", ctx.start.line)
        if self.symbol_table[var_name] == "const":
            raise SemanticError(f"Não é possível atribuir valor à constante '{var_name}'", ctx.start.line)
        
        var_type = ctx.VARNAME().getSymbol().type
        value_node = ctx.expressaoAritmetica() or ctx.expressaoBooleana()
        value = self.visit(value_node)
        
        # Verificação de tipo
        if var_type == "int":
            try:
                int(value)
            except ValueError:
                raise SemanticError(f"Não é possível atribuir valor não inteiro à variável inteira '{var_name}'", ctx.start.line)
        elif var_type == "float":
            try:
                float(value)
            except ValueError:
                raise SemanticError(f"Não é possível atribuir valor não flutuante à variável flutuante '{var_name}'", ctx.start.line)
        elif var_type == "bool" and value not in ["true", "false"]:
            raise SemanticError(f"Não é possível atribuir valor não booleano à variável booleana '{var_name}'", ctx.start.line)
        
        return f"(Atribuição: {var_name} = {value})"

    def visitFuncprint(self, ctx: GramaticaParser.FuncprintContext):
        expressions = [self.visit(expr) for expr in ctx.expressao()]
        for idx, expr in enumerate(expressions):
            if expr is None:
                print(f"Erro na expressão no índice {idx}: {ctx.expressao(idx).getText()}")
        return f"(Imprimir: {', '.join(expressions)})"

    def visitFuncinput(self, ctx: GramaticaParser.FuncinputContext):
        # print("visitFuncinput")
        variables = [var.getText() for var in ctx.VARNAME()]
        for var in variables:
            if var not in self.symbol_table:
                raise SemanticError(f"Variável '{var}' não declarada", ctx.start.line)
        return f"(Entrada: {', '.join(variables)})"


    def visitCondicional(self, ctx: GramaticaParser.CondicionalContext):
        condition = self.visit(ctx.expressaoBooleana())
        true_block = [self.visit(cmd) for cmd in ctx.comandos(0).comando()]
        false_block = []
        if ctx.comandos(1):
            false_block = [self.visit(cmd) for cmd in ctx.comandos(1).comando()]
        return f"(Se: {condition} (BlocoVerdadeiro: {self.format_ast(true_block)}) (BlocoFalso: {self.format_ast(false_block)}))"

    def visitCmdWhile(self, ctx: GramaticaParser.CmdWhileContext):
        # print("visitCmdWhile")
        condition = self.visit(ctx.expressaoBooleana())
        body = [self.visit(cmd) for cmd in ctx.comandos().comando()]
        return f"(Enquanto: {condition} (Corpo: {self.format_ast(body)}))"

    def visitExpressao(self, ctx: GramaticaParser.ExpressaoContext):
        # print("visitExpressao")
        if ctx.expressaoAritmetica():
            return self.visit(ctx.expressaoAritmetica())
        elif ctx.STRING():
            # Retorna o valor da string corretamente
            return ctx.STRING().getText() 
        else:
            raise SemanticError("Expressão inválida", ctx.start.line)


    def visitExpressaoAritmetica(self, ctx: GramaticaParser.ExpressaoAritmeticaContext):
        # print("visitExpressaoAritmetica")
        # Começa com o primeiro termo
        result = self.visit(ctx.termo(0))
        # Itera sobre os operadores e os termos subsequentes
        for i in range(1, len(ctx.termo())):
            operator = ctx.getChild(2 * i - 1).getText()  # Operador entre os termos
            right = self.visit(ctx.termo(i))  # Próximo termo
            result = f"({result} {operator} {right})"  # Combina os resultados
        return result
    

    def visitExpressaoBooleana(self, ctx: GramaticaParser.ExpressaoBooleanaContext):
        if ctx.VALBOOL():
            return ctx.VALBOOL().getText()
        elif ctx.getChildCount() == 3:  # Comparação ou operação lógica binária
            left = self.visit(ctx.expressaoAritmetica(0) or ctx.expressaoBooleana(0))
            operator = ctx.getChild(1).getText()
            right = self.visit(ctx.expressaoAritmetica(1) or ctx.expressaoBooleana(1))
            return f"({left} {operator} {right})"
        elif ctx.getChildCount() == 2:  # Negação lógica
            operator = ctx.getChild(0).getText()
            operand = self.visit(ctx.expressaoBooleana(0))
            return f"({operator} {operand})"


    def visitTermo(self, ctx: GramaticaParser.TermoContext):
        # print("visitTermo")
        # Começa com o primeiro fator
        result = self.visit(ctx.fator(0))
        # Itera sobre os operadores e os fatores subsequentes
        for i in range(1, len(ctx.fator())):
            operator = ctx.getChild(2 * i - 1).getText()  # Operador entre os fatores
            right = self.visit(ctx.fator(i))  # Próximo fator
            result = f"({result} {operator} {right})"  # Combina os resultados
        return result

    
    def visitFator(self, ctx: GramaticaParser.FatorContext):
        # print("visitFator")
        if ctx.VARNAME():
            return ctx.VARNAME().getText()
        elif ctx.VALINT():
            return ctx.VALINT().getText()
        elif ctx.VALFLOAT():
            return ctx.VALFLOAT().getText()
        elif ctx.expressaoAritmetica():
            return f"({self.visit(ctx.expressaoAritmetica())})"


    def format_ast(self, elements):
        return " ".join(elements)

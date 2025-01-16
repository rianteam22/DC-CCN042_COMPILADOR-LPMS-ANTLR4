from gen.GramaticaVisitor import GramaticaVisitor
from gen.GramaticaParser import GramaticaParser
from antlr4.error.ErrorListener import ErrorListener

class SemanticError(Exception):
    def __init__(self, message, line):
        super().__init__(f"Semantic Error: {message} at line {line}")
        self.line = line

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Syntax Error: {msg} at line {line}, column {column}")

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
        self.symbol_table = {}  # Symbol table for semantic analysis

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
                raise SemanticError(f"Variable '{var}' already declared", ctx.start.line)
            self.symbol_table[var] = var_type
        return f"(VarDecl: {var_type} {', '.join(variables)})"

    def visitConstDecl(self, ctx: GramaticaParser.ConstDeclContext):
        constants = []
        for i in range(len(ctx.VARNAME())):
            var_name = ctx.VARNAME(i).getText()
            value = self.visit(ctx.getChild(2 * i + 2))
            if var_name in self.symbol_table:
                raise SemanticError(f"Constant '{var_name}' already declared", ctx.start.line)
            self.symbol_table[var_name] = "const"
            constants.append(f"{var_name} = {value}")
        return f"(ConstDecl: {', '.join(constants)})"

    def visitOpMath(self, ctx: GramaticaParser.OpMathContext):
        var_name = ctx.VARNAME().getText()
        if var_name not in self.symbol_table:
            raise SemanticError(f"Variable '{var_name}' not declared", ctx.start.line)
        if self.symbol_table[var_name] == "const":
            raise SemanticError(f"Cannot assign to constant '{var_name}'", ctx.start.line)
        value = self.visit(ctx.expressaoAritmetica() or ctx.expressaoBooleana())
        return f"(Atrib: {var_name} {value})"

    def visitFuncprint(self, ctx: GramaticaParser.FuncprintContext):
        expressions = [self.visit(expr) for expr in ctx.expressao()]
        for idx, expr in enumerate(expressions):
            if expr is None:
                print(f"Error in expression at index {idx}: {ctx.expressao(idx).getText()}")
        return f"(Print: {', '.join(expressions)})"


    def visitFuncinput(self, ctx: GramaticaParser.FuncinputContext):
        variables = [var.getText() for var in ctx.VARNAME()]
        for var in variables:
            if var not in self.symbol_table:
                raise SemanticError(f"Variable '{var}' not declared", ctx.start.line)
        return f"(Input: {', '.join(variables)})"

    def visitCondicional(self, ctx: GramaticaParser.CondicionalContext):
        condition = self.visit(ctx.expressaoBooleana())
        true_block = [self.visit(cmd) for cmd in ctx.comandos(0).comando()]
        false_block = []
        if ctx.comandos(1):
            false_block = [self.visit(cmd) for cmd in ctx.comandos(1).comando()]
        return f"(If: {condition} (TrueBlock: {self.format_ast(true_block)}) (FalseBlock: {self.format_ast(false_block)}))"

    def visitCmdWhile(self, ctx: GramaticaParser.CmdWhileContext):
        condition = self.visit(ctx.expressaoBooleana())
        body = [self.visit(cmd) for cmd in ctx.comandos().comando()]
        return f"(While: {condition} (Corpo: {self.format_ast(body)}))"

    def visitExpressao(self, ctx: GramaticaParser.ExpressaoContext):
        print("visitExpressao")
        if ctx.expressaoAritmetica():
            return self.visit(ctx.expressaoAritmetica())
        elif ctx.STRING():
            return ctx.STRING().getText() 
        else:
            raise SemanticError("Invalid expression", ctx.start.line)


    def visitExpressaoBooleana(self, ctx: GramaticaParser.ExpressaoBooleanaContext):
        if ctx.VALBOOL():
            return ctx.VALBOOL().getText()
        elif ctx.getChildCount() == 3:
            left = self.visit(ctx.expressaoAritmetica(0))
            operator = ctx.getChild(1).getText()
            right = self.visit(ctx.expressaoAritmetica(1))
            return f"({left} {operator} {right})"
        elif ctx.getChildCount() == 2:
            operator = ctx.getChild(0).getText()
            operand = self.visit(ctx.expressaoBooleana(0))
            return f"({operator} {operand})"

    def visitTermo(self, ctx: GramaticaParser.TermoContext):
        return self.visit(ctx.fator(0))

    def visitFator(self, ctx: GramaticaParser.FatorContext):
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
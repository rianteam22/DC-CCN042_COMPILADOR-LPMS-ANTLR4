from antlr4 import *
from gen.GramaticaParser import GramaticaParser
from gen.GramaticaVisitor import GramaticaVisitor

class TACGenerator(GramaticaVisitor):

    def __init__(self):
        self.temp_counter = 0
        self.label_counter = 0
        self.tac_code = []

    def new_temp(self):
        temp_name = f"t{self.temp_counter}"
        self.temp_counter += 1
        return temp_name

    def new_label(self):
        label_name = f"L{self.label_counter}"
        self.label_counter += 1
        return label_name

    def emit(self, code):
        self.tac_code.append(code)

    def visitProg(self, ctx: GramaticaParser.ProgContext):
        self.visit(ctx.main())
        return self.tac_code

    def visitMain(self, ctx: GramaticaParser.MainContext):
        for decVar in ctx.decVar():
            self.visit(decVar)
        for comando in ctx.comandos():
            self.visit(comando)

    def visitVarDecl(self, ctx: GramaticaParser.VarDeclContext):
        for var in ctx.VARNAME():
            self.emit(f"declare {var.getText()}")

    def visitConstDecl(self, ctx: GramaticaParser.ConstDeclContext):
        for i in range(len(ctx.VARNAME())):
            var = ctx.VARNAME(i).getText()
            value = ctx.getChild(4 + i * 4).getText()
            self.emit(f"const {var} = {value}")

    def visitOpMath(self, ctx: GramaticaParser.OpMathContext):
        var = ctx.VARNAME().getText()
        expr_result = self.visit(ctx.getChild(2))
        self.emit(f"{var} = {expr_result}")

    def visitExpressaoAritmetica(self, ctx: GramaticaParser.ExpressaoAritmeticaContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.getChild(0))
        left = self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))
        temp = self.new_temp()
        self.emit(f"{temp} = {left} {op} {right}")
        return temp

    def visitTermo(self, ctx: GramaticaParser.TermoContext):
        if len(ctx.children) == 1:
            return ctx.getChild(0).getText()
        left = self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))
        temp = self.new_temp()
        self.emit(f"{temp} = {left} {op} {right}")
        return temp

    def visitCondicional(self, ctx: GramaticaParser.CondicionalContext):
        cond = self.visit(ctx.expressaoBooleana())
        label_true = self.new_label()
        label_end = self.new_label()
        self.emit(f"if {cond} goto {label_true}")
        if ctx.getChild(6):
            self.visit(ctx.getChild(6))
        self.emit(f"goto {label_end}")
        self.emit(f"{label_true}:")
        self.visit(ctx.comandos(0))
        self.emit(f"{label_end}:")

    def visitCmdWhile(self, ctx: GramaticaParser.CmdWhileContext):
        label_start = self.new_label()
        label_end = self.new_label()
        self.emit(f"{label_start}:")
        cond = self.visit(ctx.expressaoBooleana())
        self.emit(f"if not {cond} goto {label_end}")
        self.visit(ctx.comandos())
        self.emit(f"goto {label_start}")
        self.emit(f"{label_end}:")

    def visitExpressaoBooleana(self, ctx: GramaticaParser.ExpressaoBooleanaContext):
        if len(ctx.children) == 1:
            return ctx.getChild(0).getText()
        left = self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))
        temp = self.new_temp()
        self.emit(f"{temp} = {left} {op} {right}")
        return temp

    def visitFuncprint(self, ctx: GramaticaParser.FuncprintContext):
        for expr in ctx.expressao():
            result = self.visit(expr)
            self.emit(f"print {result}")

    def visitFuncinput(self, ctx: GramaticaParser.FuncinputContext):
        for var in ctx.VARNAME():
            self.emit(f"input {var.getText()}")

if __name__ == "__main__":
    from antlr4 import FileStream
    from gen.GramaticaLexer import GramaticaLexer
    from gen.GramaticaParser import GramaticaParser

    input_stream = FileStream("input0.lps")
    lexer = GramaticaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GramaticaParser(token_stream)
    tree = parser.prog()

    tac_generator = TACGenerator()
    tac = tac_generator.visit(tree)

    for line in tac:
        print(line)

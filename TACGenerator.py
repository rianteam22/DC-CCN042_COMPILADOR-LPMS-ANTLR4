import sys
from antlr4 import *
from antlr4 import FileStream
from gen.GramaticaParser import GramaticaParser
from gen.GramaticaVisitor import GramaticaVisitor

RED = '\033[91m'
RESET = '\033[0m'

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

    def visitOpMath(self, ctx: GramaticaParser.OpMathContext):
        #print(RED, "visitOpMath", RESET)
        var = ctx.VARNAME().getText()
        expr_result = self.visit(ctx.getChild(2))
        self.emit(f"{var} = {expr_result}")

    def visitExpressao(self, ctx: GramaticaParser.ExpressaoContext):
        if len(ctx.children) == 1:
            child = ctx.getChild(0)
            if isinstance(child, TerminalNode) and child.symbol.type == GramaticaParser.STRING:
                return child.getText()
            else:
                return self.visit(child)
        return self.visitExpressaoAritmetica(ctx)

    def visitExpressaoAritmetica(self, ctx: GramaticaParser.ExpressaoAritmeticaContext):
        if len(ctx.children) == 1:
            return self.visit(ctx.getChild(0))
        
        left = self.visit(ctx.getChild(0))
        for i in range(1, len(ctx.children) - 1, 2):
            op = ctx.getChild(i).getText()
            right = self.visit(ctx.getChild(i + 1))
            temp = self.new_temp()
            self.emit(f"{temp} = {left} {op} {right}")
            left = temp
        
        return left

    def visitTermo(self, ctx: GramaticaParser.TermoContext):
        if len(ctx.children) == 1:
            return ctx.getChild(0).getText()
        
        left = self.visit(ctx.getChild(0))
        for i in range(1, len(ctx.children) - 1, 2):
            op = ctx.getChild(i).getText()
            right = self.visit(ctx.getChild(i + 1))
            temp = self.new_temp()
            self.emit(f"{temp} = {left} {op} {right}")
            left = temp
        
        return left
    
    
    def visitFator(self, ctx: GramaticaParser.FatorContext):
        if len(ctx.children) == 1:
            return ctx.getChild(0).getText()
        if ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
            return self.visit(ctx.getChild(1))
        left = self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))
        temp = self.new_temp()
        self.emit(f"{temp} = {left} {op} {right}")
        return temp


    def visitCondicional(self, ctx: GramaticaParser.CondicionalContext):
        cond = self.visit(ctx.expressaoBooleana())
        label_else = self.new_label()
        label_end = self.new_label()
        
        self.emit(f"if not {cond} goto {label_else}")
        
        # Emitir comandos do bloco if
        self.visit(ctx.getChild(5))  # Supondo que o bloco if é o terceiro filho
        #print
        self.emit(f"goto {label_end}")
        
        self.emit(f"{label_else}:")
        
        # Emitir comandos do bloco else
        self.visit(ctx.getChild(9))  # Supondo que o bloco else é o quinto filho
        
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
        #print("visitExpressaoBooleana")
        if len(ctx.children) == 1:
            return ctx.getChild(0).getText()
        if len(ctx.children) == 2 and ctx.getChild(0).getText() == '!':
            return f"not {self.visit(ctx.getChild(1))}"
        if len(ctx.children) == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.getChild(1))
        left = self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))
        temp = self.new_temp()
        self.emit(f"{temp} = {left} {op} {right}")
        return temp

    
    def visitFuncprint(self, ctx: GramaticaParser.FuncprintContext):
        param_count = 0
        for i in range(2, len(ctx.children)-2):
            if ctx.getChild(i).getText() == ',': continue
            else:
                exp = self.visit(ctx.getChild(i))
                #exp = ctx.getChild(i).getText()
                self.emit(f"param {exp}")
                param_count += 1
        self.emit(f"call print {param_count}")


    def visitFuncinput(self, ctx: GramaticaParser.FuncinputContext):
        param_count = 0
        for i in range(2, len(ctx.children)-2):
            if ctx.getChild(i).getText() == ',': continue
            else:
                var = ctx.getChild(i).getText()
                self.emit(f"param {var}")
                param_count += 1
        self.emit(f"call input {param_count}")

if __name__ == "__main__":
    from antlr4 import FileStream
    from gen.GramaticaLexer import GramaticaLexer
    from gen.GramaticaParser import GramaticaParser

    if len(sys.argv) != 2:
        print("Usage: python TACGenerator.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    input_stream = FileStream(input_file)
    lexer = GramaticaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GramaticaParser(token_stream)
    tree = parser.prog()

    tac_generator = TACGenerator()
    tac = tac_generator.visit(tree)

    for line in tac:
        print(line)

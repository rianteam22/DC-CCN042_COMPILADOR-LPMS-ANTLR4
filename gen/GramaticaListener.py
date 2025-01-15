# Generated from Gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete listener for a parse tree produced by GramaticaParser.
class GramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by GramaticaParser#prog.
    def enterProg(self, ctx:GramaticaParser.ProgContext):
        pass

    # Exit a parse tree produced by GramaticaParser#prog.
    def exitProg(self, ctx:GramaticaParser.ProgContext):
        pass


    # Enter a parse tree produced by GramaticaParser#main.
    def enterMain(self, ctx:GramaticaParser.MainContext):
        pass

    # Exit a parse tree produced by GramaticaParser#main.
    def exitMain(self, ctx:GramaticaParser.MainContext):
        pass


    # Enter a parse tree produced by GramaticaParser#decVar.
    def enterDecVar(self, ctx:GramaticaParser.DecVarContext):
        pass

    # Exit a parse tree produced by GramaticaParser#decVar.
    def exitDecVar(self, ctx:GramaticaParser.DecVarContext):
        pass


    # Enter a parse tree produced by GramaticaParser#varDecl.
    def enterVarDecl(self, ctx:GramaticaParser.VarDeclContext):
        pass

    # Exit a parse tree produced by GramaticaParser#varDecl.
    def exitVarDecl(self, ctx:GramaticaParser.VarDeclContext):
        pass


    # Enter a parse tree produced by GramaticaParser#constDecl.
    def enterConstDecl(self, ctx:GramaticaParser.ConstDeclContext):
        pass

    # Exit a parse tree produced by GramaticaParser#constDecl.
    def exitConstDecl(self, ctx:GramaticaParser.ConstDeclContext):
        pass


    # Enter a parse tree produced by GramaticaParser#comandos.
    def enterComandos(self, ctx:GramaticaParser.ComandosContext):
        pass

    # Exit a parse tree produced by GramaticaParser#comandos.
    def exitComandos(self, ctx:GramaticaParser.ComandosContext):
        pass


    # Enter a parse tree produced by GramaticaParser#funcprint.
    def enterFuncprint(self, ctx:GramaticaParser.FuncprintContext):
        pass

    # Exit a parse tree produced by GramaticaParser#funcprint.
    def exitFuncprint(self, ctx:GramaticaParser.FuncprintContext):
        pass


    # Enter a parse tree produced by GramaticaParser#funcinput.
    def enterFuncinput(self, ctx:GramaticaParser.FuncinputContext):
        pass

    # Exit a parse tree produced by GramaticaParser#funcinput.
    def exitFuncinput(self, ctx:GramaticaParser.FuncinputContext):
        pass


    # Enter a parse tree produced by GramaticaParser#condicional.
    def enterCondicional(self, ctx:GramaticaParser.CondicionalContext):
        pass

    # Exit a parse tree produced by GramaticaParser#condicional.
    def exitCondicional(self, ctx:GramaticaParser.CondicionalContext):
        pass


    # Enter a parse tree produced by GramaticaParser#cmdWhile.
    def enterCmdWhile(self, ctx:GramaticaParser.CmdWhileContext):
        pass

    # Exit a parse tree produced by GramaticaParser#cmdWhile.
    def exitCmdWhile(self, ctx:GramaticaParser.CmdWhileContext):
        pass


    # Enter a parse tree produced by GramaticaParser#opMath.
    def enterOpMath(self, ctx:GramaticaParser.OpMathContext):
        pass

    # Exit a parse tree produced by GramaticaParser#opMath.
    def exitOpMath(self, ctx:GramaticaParser.OpMathContext):
        pass


    # Enter a parse tree produced by GramaticaParser#expressao.
    def enterExpressao(self, ctx:GramaticaParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#expressao.
    def exitExpressao(self, ctx:GramaticaParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#expressaoAritmetica.
    def enterExpressaoAritmetica(self, ctx:GramaticaParser.ExpressaoAritmeticaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#expressaoAritmetica.
    def exitExpressaoAritmetica(self, ctx:GramaticaParser.ExpressaoAritmeticaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#termo.
    def enterTermo(self, ctx:GramaticaParser.TermoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#termo.
    def exitTermo(self, ctx:GramaticaParser.TermoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#fator.
    def enterFator(self, ctx:GramaticaParser.FatorContext):
        pass

    # Exit a parse tree produced by GramaticaParser#fator.
    def exitFator(self, ctx:GramaticaParser.FatorContext):
        pass


    # Enter a parse tree produced by GramaticaParser#expressaoBooleana.
    def enterExpressaoBooleana(self, ctx:GramaticaParser.ExpressaoBooleanaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#expressaoBooleana.
    def exitExpressaoBooleana(self, ctx:GramaticaParser.ExpressaoBooleanaContext):
        pass



del GramaticaParser
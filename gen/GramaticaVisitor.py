# Generated from Gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete generic visitor for a parse tree produced by GramaticaParser.

class GramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramaticaParser#prog.
    def visitProg(self, ctx:GramaticaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#main.
    def visitMain(self, ctx:GramaticaParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#decVar.
    def visitDecVar(self, ctx:GramaticaParser.DecVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#varDecl.
    def visitVarDecl(self, ctx:GramaticaParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#constDecl.
    def visitConstDecl(self, ctx:GramaticaParser.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#comandos.
    def visitComandos(self, ctx:GramaticaParser.ComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#funcprint.
    def visitFuncprint(self, ctx:GramaticaParser.FuncprintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#funcinput.
    def visitFuncinput(self, ctx:GramaticaParser.FuncinputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#condicional.
    def visitCondicional(self, ctx:GramaticaParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#cmdWhile.
    def visitCmdWhile(self, ctx:GramaticaParser.CmdWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#opMath.
    def visitOpMath(self, ctx:GramaticaParser.OpMathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#expressao.
    def visitExpressao(self, ctx:GramaticaParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#expressaoAritmetica.
    def visitExpressaoAritmetica(self, ctx:GramaticaParser.ExpressaoAritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#termo.
    def visitTermo(self, ctx:GramaticaParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#fator.
    def visitFator(self, ctx:GramaticaParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#expressaoBooleana.
    def visitExpressaoBooleana(self, ctx:GramaticaParser.ExpressaoBooleanaContext):
        return self.visitChildren(ctx)



del GramaticaParser
# Generated from Gramatica.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,208,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,1,1,1,1,1,1,1,5,1,39,8,1,10,1,12,1,
        42,9,1,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,1,1,1,1,2,1,2,3,2,54,8,
        2,1,3,1,3,1,3,1,3,5,3,60,8,3,10,3,12,3,63,9,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,5,4,75,8,4,10,4,12,4,78,9,4,1,4,1,4,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,3,5,89,8,5,1,6,1,6,1,6,1,6,1,6,5,6,96,8,6,
        10,6,12,6,99,9,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,5,7,109,8,7,10,
        7,12,7,112,9,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,123,8,8,10,
        8,12,8,126,9,8,1,8,1,8,1,8,1,8,5,8,132,8,8,10,8,12,8,135,9,8,1,8,
        3,8,138,8,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,146,8,9,10,9,12,9,149,9,
        9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,157,8,10,1,10,1,10,1,11,1,11,
        3,11,163,8,11,1,12,1,12,1,12,1,12,1,12,5,12,170,8,12,10,12,12,12,
        173,9,12,1,13,1,13,1,13,1,13,1,13,5,13,180,8,13,10,13,12,13,183,
        9,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,192,8,14,1,15,1,15,
        1,15,3,15,197,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,206,8,
        15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,2,1,
        0,29,32,1,0,20,25,220,0,32,1,0,0,0,2,34,1,0,0,0,4,53,1,0,0,0,6,55,
        1,0,0,0,8,66,1,0,0,0,10,88,1,0,0,0,12,90,1,0,0,0,14,103,1,0,0,0,
        16,116,1,0,0,0,18,139,1,0,0,0,20,152,1,0,0,0,22,162,1,0,0,0,24,164,
        1,0,0,0,26,174,1,0,0,0,28,191,1,0,0,0,30,205,1,0,0,0,32,33,3,2,1,
        0,33,1,1,0,0,0,34,35,5,1,0,0,35,36,5,28,0,0,36,40,5,2,0,0,37,39,
        3,4,2,0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,
        41,46,1,0,0,0,42,40,1,0,0,0,43,45,3,10,5,0,44,43,1,0,0,0,45,48,1,
        0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,49,
        50,5,3,0,0,50,3,1,0,0,0,51,54,3,6,3,0,52,54,3,8,4,0,53,51,1,0,0,
        0,53,52,1,0,0,0,54,5,1,0,0,0,55,56,5,27,0,0,56,61,5,28,0,0,57,58,
        5,4,0,0,58,60,5,28,0,0,59,57,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,
        61,62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,65,5,5,0,0,65,7,1,0,
        0,0,66,67,5,6,0,0,67,68,5,28,0,0,68,69,5,7,0,0,69,76,7,0,0,0,70,
        71,5,4,0,0,71,72,5,28,0,0,72,73,5,7,0,0,73,75,7,0,0,0,74,70,1,0,
        0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,
        1,0,0,0,79,80,5,5,0,0,80,9,1,0,0,0,81,89,3,14,7,0,82,89,3,12,6,0,
        83,89,3,20,10,0,84,89,3,16,8,0,85,89,3,18,9,0,86,87,5,8,0,0,87,89,
        5,5,0,0,88,81,1,0,0,0,88,82,1,0,0,0,88,83,1,0,0,0,88,84,1,0,0,0,
        88,85,1,0,0,0,88,86,1,0,0,0,89,11,1,0,0,0,90,91,5,9,0,0,91,92,5,
        10,0,0,92,97,3,22,11,0,93,94,5,4,0,0,94,96,3,22,11,0,95,93,1,0,0,
        0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,97,
        1,0,0,0,100,101,5,11,0,0,101,102,5,5,0,0,102,13,1,0,0,0,103,104,
        5,12,0,0,104,105,5,10,0,0,105,110,5,28,0,0,106,107,5,4,0,0,107,109,
        5,28,0,0,108,106,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,
        1,0,0,0,111,113,1,0,0,0,112,110,1,0,0,0,113,114,5,11,0,0,114,115,
        5,5,0,0,115,15,1,0,0,0,116,117,5,13,0,0,117,118,5,10,0,0,118,119,
        3,30,15,0,119,120,5,11,0,0,120,124,5,2,0,0,121,123,3,10,5,0,122,
        121,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,
        127,1,0,0,0,126,124,1,0,0,0,127,137,5,3,0,0,128,129,5,14,0,0,129,
        133,5,2,0,0,130,132,3,10,5,0,131,130,1,0,0,0,132,135,1,0,0,0,133,
        131,1,0,0,0,133,134,1,0,0,0,134,136,1,0,0,0,135,133,1,0,0,0,136,
        138,5,3,0,0,137,128,1,0,0,0,137,138,1,0,0,0,138,17,1,0,0,0,139,140,
        5,15,0,0,140,141,5,10,0,0,141,142,3,30,15,0,142,143,5,11,0,0,143,
        147,5,2,0,0,144,146,3,10,5,0,145,144,1,0,0,0,146,149,1,0,0,0,147,
        145,1,0,0,0,147,148,1,0,0,0,148,150,1,0,0,0,149,147,1,0,0,0,150,
        151,5,3,0,0,151,19,1,0,0,0,152,153,5,28,0,0,153,156,5,7,0,0,154,
        157,3,24,12,0,155,157,3,30,15,0,156,154,1,0,0,0,156,155,1,0,0,0,
        157,158,1,0,0,0,158,159,5,5,0,0,159,21,1,0,0,0,160,163,3,24,12,0,
        161,163,5,32,0,0,162,160,1,0,0,0,162,161,1,0,0,0,163,23,1,0,0,0,
        164,171,3,26,13,0,165,166,5,16,0,0,166,170,3,26,13,0,167,168,5,17,
        0,0,168,170,3,26,13,0,169,165,1,0,0,0,169,167,1,0,0,0,170,173,1,
        0,0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,25,1,0,0,0,173,171,1,0,
        0,0,174,181,3,28,14,0,175,176,5,18,0,0,176,180,3,28,14,0,177,178,
        5,19,0,0,178,180,3,28,14,0,179,175,1,0,0,0,179,177,1,0,0,0,180,183,
        1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,27,1,0,0,0,183,181,1,
        0,0,0,184,192,5,28,0,0,185,192,5,31,0,0,186,192,5,30,0,0,187,188,
        5,10,0,0,188,189,3,24,12,0,189,190,5,11,0,0,190,192,1,0,0,0,191,
        184,1,0,0,0,191,185,1,0,0,0,191,186,1,0,0,0,191,187,1,0,0,0,192,
        29,1,0,0,0,193,196,3,24,12,0,194,195,7,1,0,0,195,197,3,24,12,0,196,
        194,1,0,0,0,196,197,1,0,0,0,197,206,1,0,0,0,198,199,5,26,0,0,199,
        206,3,30,15,0,200,206,5,29,0,0,201,202,5,10,0,0,202,203,3,30,15,
        0,203,204,5,11,0,0,204,206,1,0,0,0,205,193,1,0,0,0,205,198,1,0,0,
        0,205,200,1,0,0,0,205,201,1,0,0,0,206,31,1,0,0,0,21,40,46,53,61,
        76,88,97,110,124,133,137,147,156,162,169,171,179,181,191,196,205
    ]

class GramaticaParser ( Parser ):

    grammarFileName = "Gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Program'", "'{'", "'}'", "','", "';'", 
                     "'const'", "'='", "'break'", "'print'", "'('", "')'", 
                     "'input'", "'if'", "'else'", "'while'", "'+'", "'-'", 
                     "'*'", "'/'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "VARTYPE", 
                      "VARNAME", "VALBOOL", "VALINT", "VALFLOAT", "STRING", 
                      "WS", "LINE_COMMENT", "COMMENT" ]

    RULE_prog = 0
    RULE_main = 1
    RULE_decVar = 2
    RULE_varDecl = 3
    RULE_constDecl = 4
    RULE_comandos = 5
    RULE_funcprint = 6
    RULE_funcinput = 7
    RULE_condicional = 8
    RULE_cmdWhile = 9
    RULE_opMath = 10
    RULE_expressao = 11
    RULE_expressaoAritmetica = 12
    RULE_termo = 13
    RULE_fator = 14
    RULE_expressaoBooleana = 15

    ruleNames =  [ "prog", "main", "decVar", "varDecl", "constDecl", "comandos", 
                   "funcprint", "funcinput", "condicional", "cmdWhile", 
                   "opMath", "expressao", "expressaoAritmetica", "termo", 
                   "fator", "expressaoBooleana" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    VARTYPE=27
    VARNAME=28
    VALBOOL=29
    VALINT=30
    VALFLOAT=31
    STRING=32
    WS=33
    LINE_COMMENT=34
    COMMENT=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main(self):
            return self.getTypedRuleContext(GramaticaParser.MainContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = GramaticaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(GramaticaParser.VARNAME, 0)

        def decVar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.DecVarContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.DecVarContext,i)


        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ComandosContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ComandosContext,i)


        def getRuleIndex(self):
            return GramaticaParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = GramaticaParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(GramaticaParser.T__0)
            self.state = 35
            self.match(GramaticaParser.VARNAME)
            self.state = 36
            self.match(GramaticaParser.T__1)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==27:
                self.state = 37
                self.decVar()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268481280) != 0):
                self.state = 43
                self.comandos()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(GramaticaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecVarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(GramaticaParser.VarDeclContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(GramaticaParser.ConstDeclContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_decVar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecVar" ):
                listener.enterDecVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecVar" ):
                listener.exitDecVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecVar" ):
                return visitor.visitDecVar(self)
            else:
                return visitor.visitChildren(self)




    def decVar(self):

        localctx = GramaticaParser.DecVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decVar)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.varDecl()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.constDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARTYPE(self):
            return self.getToken(GramaticaParser.VARTYPE, 0)

        def VARNAME(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.VARNAME)
            else:
                return self.getToken(GramaticaParser.VARNAME, i)

        def getRuleIndex(self):
            return GramaticaParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = GramaticaParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(GramaticaParser.VARTYPE)
            self.state = 56
            self.match(GramaticaParser.VARNAME)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 57
                self.match(GramaticaParser.T__3)
                self.state = 58
                self.match(GramaticaParser.VARNAME)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(GramaticaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.VARNAME)
            else:
                return self.getToken(GramaticaParser.VARNAME, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.STRING)
            else:
                return self.getToken(GramaticaParser.STRING, i)

        def VALINT(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.VALINT)
            else:
                return self.getToken(GramaticaParser.VALINT, i)

        def VALFLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.VALFLOAT)
            else:
                return self.getToken(GramaticaParser.VALFLOAT, i)

        def VALBOOL(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.VALBOOL)
            else:
                return self.getToken(GramaticaParser.VALBOOL, i)

        def getRuleIndex(self):
            return GramaticaParser.RULE_constDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstDecl" ):
                listener.enterConstDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstDecl" ):
                listener.exitConstDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDecl" ):
                return visitor.visitConstDecl(self)
            else:
                return visitor.visitChildren(self)




    def constDecl(self):

        localctx = GramaticaParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(GramaticaParser.T__5)
            self.state = 67
            self.match(GramaticaParser.VARNAME)
            self.state = 68
            self.match(GramaticaParser.T__6)
            self.state = 69
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 70
                self.match(GramaticaParser.T__3)
                self.state = 71
                self.match(GramaticaParser.VARNAME)
                self.state = 72
                self.match(GramaticaParser.T__6)
                self.state = 73
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self.match(GramaticaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcinput(self):
            return self.getTypedRuleContext(GramaticaParser.FuncinputContext,0)


        def funcprint(self):
            return self.getTypedRuleContext(GramaticaParser.FuncprintContext,0)


        def opMath(self):
            return self.getTypedRuleContext(GramaticaParser.OpMathContext,0)


        def condicional(self):
            return self.getTypedRuleContext(GramaticaParser.CondicionalContext,0)


        def cmdWhile(self):
            return self.getTypedRuleContext(GramaticaParser.CmdWhileContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_comandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandos" ):
                listener.enterComandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandos" ):
                listener.exitComandos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandos" ):
                return visitor.visitComandos(self)
            else:
                return visitor.visitChildren(self)




    def comandos(self):

        localctx = GramaticaParser.ComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comandos)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.funcinput()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.funcprint()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.opMath()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.condicional()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 85
                self.cmdWhile()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 6)
                self.state = 86
                self.match(GramaticaParser.T__7)
                self.state = 87
                self.match(GramaticaParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncprintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExpressaoContext,i)


        def getRuleIndex(self):
            return GramaticaParser.RULE_funcprint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncprint" ):
                listener.enterFuncprint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncprint" ):
                listener.exitFuncprint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncprint" ):
                return visitor.visitFuncprint(self)
            else:
                return visitor.visitChildren(self)




    def funcprint(self):

        localctx = GramaticaParser.FuncprintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcprint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(GramaticaParser.T__8)
            self.state = 91
            self.match(GramaticaParser.T__9)
            self.state = 92
            self.expressao()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 93
                self.match(GramaticaParser.T__3)
                self.state = 94
                self.expressao()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self.match(GramaticaParser.T__10)
            self.state = 101
            self.match(GramaticaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncinputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.VARNAME)
            else:
                return self.getToken(GramaticaParser.VARNAME, i)

        def getRuleIndex(self):
            return GramaticaParser.RULE_funcinput

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncinput" ):
                listener.enterFuncinput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncinput" ):
                listener.exitFuncinput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncinput" ):
                return visitor.visitFuncinput(self)
            else:
                return visitor.visitChildren(self)




    def funcinput(self):

        localctx = GramaticaParser.FuncinputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcinput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(GramaticaParser.T__11)
            self.state = 104
            self.match(GramaticaParser.T__9)
            self.state = 105
            self.match(GramaticaParser.VARNAME)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 106
                self.match(GramaticaParser.T__3)
                self.state = 107
                self.match(GramaticaParser.VARNAME)
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self.match(GramaticaParser.T__10)
            self.state = 114
            self.match(GramaticaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoBooleana(self):
            return self.getTypedRuleContext(GramaticaParser.ExpressaoBooleanaContext,0)


        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ComandosContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ComandosContext,i)


        def getRuleIndex(self):
            return GramaticaParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = GramaticaParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(GramaticaParser.T__12)
            self.state = 117
            self.match(GramaticaParser.T__9)
            self.state = 118
            self.expressaoBooleana()
            self.state = 119
            self.match(GramaticaParser.T__10)
            self.state = 120
            self.match(GramaticaParser.T__1)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268481280) != 0):
                self.state = 121
                self.comandos()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self.match(GramaticaParser.T__2)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 128
                self.match(GramaticaParser.T__13)
                self.state = 129
                self.match(GramaticaParser.T__1)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268481280) != 0):
                    self.state = 130
                    self.comandos()
                    self.state = 135
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 136
                self.match(GramaticaParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoBooleana(self):
            return self.getTypedRuleContext(GramaticaParser.ExpressaoBooleanaContext,0)


        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ComandosContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ComandosContext,i)


        def getRuleIndex(self):
            return GramaticaParser.RULE_cmdWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdWhile" ):
                listener.enterCmdWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdWhile" ):
                listener.exitCmdWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdWhile" ):
                return visitor.visitCmdWhile(self)
            else:
                return visitor.visitChildren(self)




    def cmdWhile(self):

        localctx = GramaticaParser.CmdWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cmdWhile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(GramaticaParser.T__14)
            self.state = 140
            self.match(GramaticaParser.T__9)
            self.state = 141
            self.expressaoBooleana()
            self.state = 142
            self.match(GramaticaParser.T__10)
            self.state = 143
            self.match(GramaticaParser.T__1)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268481280) != 0):
                self.state = 144
                self.comandos()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self.match(GramaticaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpMathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(GramaticaParser.VARNAME, 0)

        def expressaoAritmetica(self):
            return self.getTypedRuleContext(GramaticaParser.ExpressaoAritmeticaContext,0)


        def expressaoBooleana(self):
            return self.getTypedRuleContext(GramaticaParser.ExpressaoBooleanaContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_opMath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpMath" ):
                listener.enterOpMath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpMath" ):
                listener.exitOpMath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpMath" ):
                return visitor.visitOpMath(self)
            else:
                return visitor.visitChildren(self)




    def opMath(self):

        localctx = GramaticaParser.OpMathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_opMath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(GramaticaParser.VARNAME)
            self.state = 153
            self.match(GramaticaParser.T__6)
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 154
                self.expressaoAritmetica()
                pass

            elif la_ == 2:
                self.state = 155
                self.expressaoBooleana()
                pass


            self.state = 158
            self.match(GramaticaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoAritmetica(self):
            return self.getTypedRuleContext(GramaticaParser.ExpressaoAritmeticaContext,0)


        def STRING(self):
            return self.getToken(GramaticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao" ):
                return visitor.visitExpressao(self)
            else:
                return visitor.visitChildren(self)




    def expressao(self):

        localctx = GramaticaParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expressao)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 28, 30, 31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.expressaoAritmetica()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(GramaticaParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoAritmeticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.TermoContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.TermoContext,i)


        def getRuleIndex(self):
            return GramaticaParser.RULE_expressaoAritmetica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoAritmetica" ):
                listener.enterExpressaoAritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoAritmetica" ):
                listener.exitExpressaoAritmetica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressaoAritmetica" ):
                return visitor.visitExpressaoAritmetica(self)
            else:
                return visitor.visitChildren(self)




    def expressaoAritmetica(self):

        localctx = GramaticaParser.ExpressaoAritmeticaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expressaoAritmetica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.termo()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 169
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [16]:
                    self.state = 165
                    self.match(GramaticaParser.T__15)
                    self.state = 166
                    self.termo()
                    pass
                elif token in [17]:
                    self.state = 167
                    self.match(GramaticaParser.T__16)
                    self.state = 168
                    self.termo()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.FatorContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.FatorContext,i)


        def getRuleIndex(self):
            return GramaticaParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermo" ):
                return visitor.visitTermo(self)
            else:
                return visitor.visitChildren(self)




    def termo(self):

        localctx = GramaticaParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.fator()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 179
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [18]:
                    self.state = 175
                    self.match(GramaticaParser.T__17)
                    self.state = 176
                    self.fator()
                    pass
                elif token in [19]:
                    self.state = 177
                    self.match(GramaticaParser.T__18)
                    self.state = 178
                    self.fator()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(GramaticaParser.VARNAME, 0)

        def VALFLOAT(self):
            return self.getToken(GramaticaParser.VALFLOAT, 0)

        def VALINT(self):
            return self.getToken(GramaticaParser.VALINT, 0)

        def expressaoAritmetica(self):
            return self.getTypedRuleContext(GramaticaParser.ExpressaoAritmeticaContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_fator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFator" ):
                return visitor.visitFator(self)
            else:
                return visitor.visitChildren(self)




    def fator(self):

        localctx = GramaticaParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_fator)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(GramaticaParser.VARNAME)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(GramaticaParser.VALFLOAT)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 186
                self.match(GramaticaParser.VALINT)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 187
                self.match(GramaticaParser.T__9)
                self.state = 188
                self.expressaoAritmetica()
                self.state = 189
                self.match(GramaticaParser.T__10)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoBooleanaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoAritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExpressaoAritmeticaContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExpressaoAritmeticaContext,i)


        def expressaoBooleana(self):
            return self.getTypedRuleContext(GramaticaParser.ExpressaoBooleanaContext,0)


        def VALBOOL(self):
            return self.getToken(GramaticaParser.VALBOOL, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_expressaoBooleana

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoBooleana" ):
                listener.enterExpressaoBooleana(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoBooleana" ):
                listener.exitExpressaoBooleana(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressaoBooleana" ):
                return visitor.visitExpressaoBooleana(self)
            else:
                return visitor.visitChildren(self)




    def expressaoBooleana(self):

        localctx = GramaticaParser.ExpressaoBooleanaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expressaoBooleana)
        self._la = 0 # Token type
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.expressaoAritmetica()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0):
                    self.state = 194
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 195
                    self.expressaoAritmetica()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.match(GramaticaParser.T__25)
                self.state = 199
                self.expressaoBooleana()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 200
                self.match(GramaticaParser.VALBOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 201
                self.match(GramaticaParser.T__9)
                self.state = 202
                self.expressaoBooleana()
                self.state = 203
                self.match(GramaticaParser.T__10)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






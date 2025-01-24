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
        4,1,35,196,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,1,1,1,1,1,1,1,4,1,41,8,1,
        11,1,12,1,42,1,1,4,1,46,8,1,11,1,12,1,47,1,1,1,1,1,2,1,2,3,2,54,
        8,2,1,3,1,3,1,3,1,3,5,3,60,8,3,10,3,12,3,63,9,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,5,4,75,8,4,10,4,12,4,78,9,4,1,4,1,4,1,5,
        4,5,83,8,5,11,5,12,5,84,1,6,1,6,1,6,1,6,3,6,91,8,6,1,6,1,6,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,3,7,102,8,7,1,8,1,8,1,8,1,8,1,8,5,8,109,8,
        8,10,8,12,8,112,9,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,5,9,122,8,9,
        10,9,12,9,125,9,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,3,10,142,8,10,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,12,1,12,3,12,154,8,12,1,13,1,13,1,13,5,13,159,8,
        13,10,13,12,13,162,9,13,1,14,1,14,1,14,5,14,167,8,14,10,14,12,14,
        170,9,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,179,8,15,1,16,1,
        16,1,16,3,16,184,8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,193,
        8,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,
        4,1,0,29,32,1,0,16,17,1,0,18,19,1,0,20,25,202,0,34,1,0,0,0,2,36,
        1,0,0,0,4,53,1,0,0,0,6,55,1,0,0,0,8,66,1,0,0,0,10,82,1,0,0,0,12,
        86,1,0,0,0,14,101,1,0,0,0,16,103,1,0,0,0,18,116,1,0,0,0,20,129,1,
        0,0,0,22,143,1,0,0,0,24,153,1,0,0,0,26,155,1,0,0,0,28,163,1,0,0,
        0,30,178,1,0,0,0,32,192,1,0,0,0,34,35,3,2,1,0,35,1,1,0,0,0,36,37,
        5,1,0,0,37,38,5,28,0,0,38,40,5,2,0,0,39,41,3,4,2,0,40,39,1,0,0,0,
        41,42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,44,46,3,
        10,5,0,45,44,1,0,0,0,46,47,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,
        49,1,0,0,0,49,50,5,3,0,0,50,3,1,0,0,0,51,54,3,6,3,0,52,54,3,8,4,
        0,53,51,1,0,0,0,53,52,1,0,0,0,54,5,1,0,0,0,55,56,5,27,0,0,56,61,
        5,28,0,0,57,58,5,4,0,0,58,60,5,28,0,0,59,57,1,0,0,0,60,63,1,0,0,
        0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,65,
        5,5,0,0,65,7,1,0,0,0,66,67,5,6,0,0,67,68,5,28,0,0,68,69,5,7,0,0,
        69,76,7,0,0,0,70,71,5,4,0,0,71,72,5,28,0,0,72,73,5,7,0,0,73,75,7,
        0,0,0,74,70,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,
        79,1,0,0,0,78,76,1,0,0,0,79,80,5,5,0,0,80,9,1,0,0,0,81,83,3,14,7,
        0,82,81,1,0,0,0,83,84,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,11,
        1,0,0,0,86,87,5,28,0,0,87,90,5,7,0,0,88,91,3,24,12,0,89,91,3,32,
        16,0,90,88,1,0,0,0,90,89,1,0,0,0,91,92,1,0,0,0,92,93,5,5,0,0,93,
        13,1,0,0,0,94,102,3,18,9,0,95,102,3,16,8,0,96,102,3,12,6,0,97,102,
        3,20,10,0,98,102,3,22,11,0,99,100,5,8,0,0,100,102,5,5,0,0,101,94,
        1,0,0,0,101,95,1,0,0,0,101,96,1,0,0,0,101,97,1,0,0,0,101,98,1,0,
        0,0,101,99,1,0,0,0,102,15,1,0,0,0,103,104,5,9,0,0,104,105,5,10,0,
        0,105,110,3,24,12,0,106,107,5,4,0,0,107,109,3,24,12,0,108,106,1,
        0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,113,1,
        0,0,0,112,110,1,0,0,0,113,114,5,11,0,0,114,115,5,5,0,0,115,17,1,
        0,0,0,116,117,5,12,0,0,117,118,5,10,0,0,118,123,5,28,0,0,119,120,
        5,4,0,0,120,122,5,28,0,0,121,119,1,0,0,0,122,125,1,0,0,0,123,121,
        1,0,0,0,123,124,1,0,0,0,124,126,1,0,0,0,125,123,1,0,0,0,126,127,
        5,11,0,0,127,128,5,5,0,0,128,19,1,0,0,0,129,130,5,13,0,0,130,131,
        5,10,0,0,131,132,3,32,16,0,132,133,5,11,0,0,133,134,5,2,0,0,134,
        135,3,10,5,0,135,141,5,3,0,0,136,137,5,14,0,0,137,138,5,2,0,0,138,
        139,3,10,5,0,139,140,5,3,0,0,140,142,1,0,0,0,141,136,1,0,0,0,141,
        142,1,0,0,0,142,21,1,0,0,0,143,144,5,15,0,0,144,145,5,10,0,0,145,
        146,3,32,16,0,146,147,5,11,0,0,147,148,5,2,0,0,148,149,3,10,5,0,
        149,150,5,3,0,0,150,23,1,0,0,0,151,154,3,26,13,0,152,154,5,32,0,
        0,153,151,1,0,0,0,153,152,1,0,0,0,154,25,1,0,0,0,155,160,3,28,14,
        0,156,157,7,1,0,0,157,159,3,28,14,0,158,156,1,0,0,0,159,162,1,0,
        0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,27,1,0,0,0,162,160,1,0,0,
        0,163,168,3,30,15,0,164,165,7,2,0,0,165,167,3,30,15,0,166,164,1,
        0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,29,1,0,
        0,0,170,168,1,0,0,0,171,179,5,28,0,0,172,179,5,31,0,0,173,179,5,
        30,0,0,174,175,5,10,0,0,175,176,3,26,13,0,176,177,5,11,0,0,177,179,
        1,0,0,0,178,171,1,0,0,0,178,172,1,0,0,0,178,173,1,0,0,0,178,174,
        1,0,0,0,179,31,1,0,0,0,180,183,3,26,13,0,181,182,7,3,0,0,182,184,
        3,26,13,0,183,181,1,0,0,0,183,184,1,0,0,0,184,193,1,0,0,0,185,186,
        5,26,0,0,186,193,3,32,16,0,187,193,5,29,0,0,188,189,5,10,0,0,189,
        190,3,32,16,0,190,191,5,11,0,0,191,193,1,0,0,0,192,180,1,0,0,0,192,
        185,1,0,0,0,192,187,1,0,0,0,192,188,1,0,0,0,193,33,1,0,0,0,17,42,
        47,53,61,76,84,90,101,110,123,141,153,160,168,178,183,192
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
    RULE_opMath = 6
    RULE_comando = 7
    RULE_funcprint = 8
    RULE_funcinput = 9
    RULE_condicional = 10
    RULE_cmdWhile = 11
    RULE_expressao = 12
    RULE_expressaoAritmetica = 13
    RULE_termo = 14
    RULE_fator = 15
    RULE_expressaoBooleana = 16

    ruleNames =  [ "prog", "main", "decVar", "varDecl", "constDecl", "comandos", 
                   "opMath", "comando", "funcprint", "funcinput", "condicional", 
                   "cmdWhile", "expressao", "expressaoAritmetica", "termo", 
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
            self.state = 34
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
            self.state = 36
            self.match(GramaticaParser.T__0)
            self.state = 37
            self.match(GramaticaParser.VARNAME)
            self.state = 38
            self.match(GramaticaParser.T__1)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==27:
                self.state = 39
                self.decVar()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 45
                self.comandos()
                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 268481280) != 0)):
                    break

            self.state = 50
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
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.varDecl()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
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
            self.state = 56
            self.match(GramaticaParser.VARTYPE)
            self.state = 57
            self.match(GramaticaParser.VARNAME)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 58
                self.match(GramaticaParser.T__3)
                self.state = 59
                self.match(GramaticaParser.VARNAME)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
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
            self.state = 67
            self.match(GramaticaParser.T__5)
            self.state = 68
            self.match(GramaticaParser.VARNAME)
            self.state = 69
            self.match(GramaticaParser.T__6)
            self.state = 70
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 71
                self.match(GramaticaParser.T__3)
                self.state = 72
                self.match(GramaticaParser.VARNAME)
                self.state = 73
                self.match(GramaticaParser.T__6)
                self.state = 74
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
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

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ComandoContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ComandoContext,i)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 83 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 82
                    self.comando()

                else:
                    raise NoViableAltException(self)
                self.state = 85 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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

        def expressao(self):
            return self.getTypedRuleContext(GramaticaParser.ExpressaoContext,0)


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
        self.enterRule(localctx, 12, self.RULE_opMath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(GramaticaParser.VARNAME)
            self.state = 88
            self.match(GramaticaParser.T__6)
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:

                self.state = 88
                self.expressao()
                pass

            elif la_ == 2:
                self.state = 90
                self.expressaoBooleana()
                pass


            self.state = 93
            self.match(GramaticaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
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
            return GramaticaParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando" ):
                return visitor.visitComando(self)
            else:
                return visitor.visitChildren(self)




    def comando(self):

        localctx = GramaticaParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comando)
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.funcinput()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.funcprint()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.opMath()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.condicional()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 99
                self.cmdWhile()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 6)
                self.state = 100
                self.match(GramaticaParser.T__7)
                self.state = 101
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
        self.enterRule(localctx, 16, self.RULE_funcprint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(GramaticaParser.T__8)
            self.state = 105
            self.match(GramaticaParser.T__9)
            self.state = 106
            self.expressao()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 107
                self.match(GramaticaParser.T__3)
                self.state = 108
                self.expressao()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.match(GramaticaParser.T__10)
            self.state = 115
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
        self.enterRule(localctx, 18, self.RULE_funcinput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(GramaticaParser.T__11)
            self.state = 118
            self.match(GramaticaParser.T__9)
            self.state = 119
            self.match(GramaticaParser.VARNAME)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 120
                self.match(GramaticaParser.T__3)
                self.state = 121
                self.match(GramaticaParser.VARNAME)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self.match(GramaticaParser.T__10)
            self.state = 128
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
        self.enterRule(localctx, 20, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(GramaticaParser.T__12)
            self.state = 131
            self.match(GramaticaParser.T__9)
            self.state = 132
            self.expressaoBooleana()
            self.state = 133
            self.match(GramaticaParser.T__10)
            self.state = 134
            self.match(GramaticaParser.T__1)
            self.state = 135
            self.comandos()
            self.state = 136
            self.match(GramaticaParser.T__2)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 137
                self.match(GramaticaParser.T__13)
                self.state = 138
                self.match(GramaticaParser.T__1)
                self.state = 139
                self.comandos()
                self.state = 140
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


        def comandos(self):
            return self.getTypedRuleContext(GramaticaParser.ComandosContext,0)


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
        self.enterRule(localctx, 22, self.RULE_cmdWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(GramaticaParser.T__14)
            self.state = 145
            self.match(GramaticaParser.T__9)
            self.state = 146
            self.expressaoBooleana()
            self.state = 147
            self.match(GramaticaParser.T__10)
            self.state = 148
            self.match(GramaticaParser.T__1)
            self.state = 149
            self.comandos()
            self.state = 150
            self.match(GramaticaParser.T__2)
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
        self.enterRule(localctx, 24, self.RULE_expressao)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 28, 30, 31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.expressaoAritmetica()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
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
        self.enterRule(localctx, 26, self.RULE_expressaoAritmetica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.termo()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 157
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 158
                self.termo()
                self.state = 163
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
        self.enterRule(localctx, 28, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.fator()
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 165
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 166
                self.fator()
                self.state = 171
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
        self.enterRule(localctx, 30, self.RULE_fator)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(GramaticaParser.VARNAME)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(GramaticaParser.VALFLOAT)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.match(GramaticaParser.VALINT)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 175
                self.match(GramaticaParser.T__9)
                self.state = 176
                self.expressaoAritmetica()
                self.state = 177
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
        self.enterRule(localctx, 32, self.RULE_expressaoBooleana)
        self._la = 0 # Token type
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.expressaoAritmetica()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0):
                    self.state = 182
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 183
                    self.expressaoAritmetica()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.match(GramaticaParser.T__25)
                self.state = 187
                self.expressaoBooleana()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.match(GramaticaParser.VALBOOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.match(GramaticaParser.T__9)
                self.state = 190
                self.expressaoBooleana()
                self.state = 191
                self.match(GramaticaParser.T__10)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






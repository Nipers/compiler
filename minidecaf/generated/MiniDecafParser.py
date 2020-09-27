# Generated from MiniDecaf.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3*")
        buf.write("\32\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\2\2\6\2")
        buf.write("\4\6\b\2\2\2\25\2\n\3\2\2\2\4\r\3\2\2\2\6\17\3\2\2\2\b")
        buf.write("\26\3\2\2\2\n\13\5\4\3\2\13\f\5\6\4\2\f\3\3\2\2\2\r\16")
        buf.write("\7\4\2\2\16\5\3\2\2\2\17\20\7\3\2\2\20\21\7\r\2\2\21\22")
        buf.write("\7\16\2\2\22\23\7\21\2\2\23\24\5\b\5\2\24\25\7\22\2\2")
        buf.write("\25\7\3\2\2\2\26\27\7\5\2\2\27\30\7(\2\2\30\t\3\2\2\2")
        buf.write("\2")
        return buf.getvalue()


class MiniDecafParser ( Parser ):

    grammarFileName = "MiniDecaf.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'int'", "'return'", "'if'", 
                     "'else'", "'for'", "'do'", "'while'", "'break'", "'continue'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "';'", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'~'", "'&'", "'<'", "'>'", "'<='", "'>='", "'=='", 
                     "'!='", "'='", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "Int", "Return", "If", "Else", 
                      "For", "Do", "While", "Break", "Continue", "Lparen", 
                      "Rparen", "Lbrkt", "Rbrkt", "Lbrace", "Rbrace", "Comma", 
                      "Semicolon", "Punctuator", "Plus", "Minus", "Asterisk", 
                      "Slash", "Percent", "Exclamation", "Tilde", "Ampersand", 
                      "Langle", "Rangle", "Langle_eq", "Rangle_eq", "Double_eq", 
                      "Exclam_eq", "Equal", "Double_amp", "Double_bar", 
                      "Operator", "Integer", "Whitespace", "Ident" ]

    RULE_function = 0
    RULE_returntype = 1
    RULE_main = 2
    RULE_content = 3

    ruleNames =  [ "function", "returntype", "main", "content" ]

    EOF = Token.EOF
    T__0=1
    Int=2
    Return=3
    If=4
    Else=5
    For=6
    Do=7
    While=8
    Break=9
    Continue=10
    Lparen=11
    Rparen=12
    Lbrkt=13
    Rbrkt=14
    Lbrace=15
    Rbrace=16
    Comma=17
    Semicolon=18
    Punctuator=19
    Plus=20
    Minus=21
    Asterisk=22
    Slash=23
    Percent=24
    Exclamation=25
    Tilde=26
    Ampersand=27
    Langle=28
    Rangle=29
    Langle_eq=30
    Rangle_eq=31
    Double_eq=32
    Exclam_eq=33
    Equal=34
    Double_amp=35
    Double_bar=36
    Operator=37
    Integer=38
    Whitespace=39
    Ident=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returntype(self):
            return self.getTypedRuleContext(MiniDecafParser.ReturntypeContext,0)


        def main(self):
            return self.getTypedRuleContext(MiniDecafParser.MainContext,0)


        def getRuleIndex(self):
            return MiniDecafParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = MiniDecafParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.returntype()
            self.state = 9
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturntypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Int(self):
            return self.getToken(MiniDecafParser.Int, 0)

        def getRuleIndex(self):
            return MiniDecafParser.RULE_returntype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturntype" ):
                listener.enterReturntype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturntype" ):
                listener.exitReturntype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturntype" ):
                return visitor.visitReturntype(self)
            else:
                return visitor.visitChildren(self)




    def returntype(self):

        localctx = MiniDecafParser.ReturntypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_returntype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(MiniDecafParser.Int)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Lparen(self):
            return self.getToken(MiniDecafParser.Lparen, 0)

        def Rparen(self):
            return self.getToken(MiniDecafParser.Rparen, 0)

        def Lbrace(self):
            return self.getToken(MiniDecafParser.Lbrace, 0)

        def content(self):
            return self.getTypedRuleContext(MiniDecafParser.ContentContext,0)


        def Rbrace(self):
            return self.getToken(MiniDecafParser.Rbrace, 0)

        def getRuleIndex(self):
            return MiniDecafParser.RULE_main

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

        localctx = MiniDecafParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(MiniDecafParser.T__0)
            self.state = 14
            self.match(MiniDecafParser.Lparen)
            self.state = 15
            self.match(MiniDecafParser.Rparen)
            self.state = 16
            self.match(MiniDecafParser.Lbrace)
            self.state = 17
            self.content()
            self.state = 18
            self.match(MiniDecafParser.Rbrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Return(self):
            return self.getToken(MiniDecafParser.Return, 0)

        def Integer(self):
            return self.getToken(MiniDecafParser.Integer, 0)

        def getRuleIndex(self):
            return MiniDecafParser.RULE_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent" ):
                listener.enterContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent" ):
                listener.exitContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContent" ):
                return visitor.visitContent(self)
            else:
                return visitor.visitChildren(self)




    def content(self):

        localctx = MiniDecafParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_content)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(MiniDecafParser.Return)
            self.state = 21
            self.match(MiniDecafParser.Integer)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






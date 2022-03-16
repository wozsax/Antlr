# Generated from c:\Users\manue\OneDrive\Desktop\ejemplosANTLR\marzo\antlr\marzo.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("B\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3")
        buf.write("\3\3\3\3\3\5\3\21\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7")
        buf.write("\3(\n\3\f\3\16\3+\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\5\48\n\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4@\n\4")
        buf.write("\3\4\2\3\4\5\2\4\6\2\2\2L\2\t\3\2\2\2\4\20\3\2\2\2\6?")
        buf.write("\3\2\2\2\b\n\5\4\3\2\t\b\3\2\2\2\n\13\3\2\2\2\13\t\3\2")
        buf.write("\2\2\13\f\3\2\2\2\f\3\3\2\2\2\r\16\b\3\1\2\16\21\7\20")
        buf.write("\2\2\17\21\7\21\2\2\20\r\3\2\2\2\20\17\3\2\2\2\21)\3\2")
        buf.write("\2\2\22\23\f\13\2\2\23\24\7\3\2\2\24(\5\4\3\f\25\26\f")
        buf.write("\n\2\2\26\27\7\4\2\2\27(\5\4\3\13\30\31\f\7\2\2\31\32")
        buf.write("\7\5\2\2\32(\5\4\3\b\33\34\f\6\2\2\34\35\7\6\2\2\35(\5")
        buf.write("\4\3\7\36\37\f\5\2\2\37 \7\7\2\2 (\5\4\3\6!\"\f\4\2\2")
        buf.write("\"#\7\b\2\2#(\5\4\3\5$%\f\3\2\2%&\7\t\2\2&(\5\4\3\4\'")
        buf.write("\22\3\2\2\2\'\25\3\2\2\2\'\30\3\2\2\2\'\33\3\2\2\2\'\36")
        buf.write("\3\2\2\2\'!\3\2\2\2\'$\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*")
        buf.write("\3\2\2\2*\5\3\2\2\2+)\3\2\2\2,-\7\n\2\2-.\5\4\3\2./\7")
        buf.write("\13\2\2/\60\5\6\4\2\60@\3\2\2\2\61\62\7\n\2\2\62\63\5")
        buf.write("\4\3\2\63\64\7\13\2\2\64\67\5\6\4\2\65\66\7\f\2\2\668")
        buf.write("\5\6\4\2\67\65\3\2\2\2\678\3\2\2\28@\3\2\2\29:\7\r\2\2")
        buf.write(":@\5\4\3\2;<\7\16\2\2<@\7\20\2\2=>\7\17\2\2>@\7\21\2\2")
        buf.write("?,\3\2\2\2?\61\3\2\2\2?9\3\2\2\2?;\3\2\2\2?=\3\2\2\2@")
        buf.write("\7\3\2\2\2\b\13\20\')\67?")
        return buf.getvalue()


class marzoParser ( Parser ):

    grammarFileName = "marzo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sum'", "'resta'", "'equals'", "'divide'", 
                     "'times'", "'less'", "'mayor'", "'if'", "'then'", "'else'", 
                     "'imprimir'", "'imNumber'", "'imWord'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "Numero", "Palabra", "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_statement = 2

    ruleNames =  [ "program", "expression", "statement" ]

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
    Numero=14
    Palabra=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return marzoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = marzoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.expression(0)
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==marzoParser.Numero or _la==marzoParser.Palabra):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class PalabraContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Palabra(self):
            return self.getToken(marzoParser.Palabra, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPalabra" ):
                listener.enterPalabra(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPalabra" ):
                listener.exitPalabra(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPalabra" ):
                return visitor.visitPalabra(self)
            else:
                return visitor.visitChildren(self)


    class MayorContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMayor" ):
                listener.enterMayor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMayor" ):
                listener.exitMayor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMayor" ):
                return visitor.visitMayor(self)
            else:
                return visitor.visitChildren(self)


    class MenorContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenor" ):
                listener.enterMenor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenor" ):
                listener.exitMenor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMenor" ):
                return visitor.visitMenor(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicarContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicar" ):
                listener.enterMultiplicar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicar" ):
                listener.exitMultiplicar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicar" ):
                return visitor.visitMultiplicar(self)
            else:
                return visitor.visitChildren(self)


    class DividirContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDividir" ):
                listener.enterDividir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDividir" ):
                listener.exitDividir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDividir" ):
                return visitor.visitDividir(self)
            else:
                return visitor.visitChildren(self)


    class IgualContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgual" ):
                listener.enterIgual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgual" ):
                listener.exitIgual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgual" ):
                return visitor.visitIgual(self)
            else:
                return visitor.visitChildren(self)


    class PrimariaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Numero(self):
            return self.getToken(marzoParser.Numero, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaria" ):
                listener.enterPrimaria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaria" ):
                listener.exitPrimaria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaria" ):
                return visitor.visitPrimaria(self)
            else:
                return visitor.visitChildren(self)


    class RestaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResta" ):
                listener.enterResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResta" ):
                listener.exitResta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResta" ):
                return visitor.visitResta(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = marzoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [marzoParser.Numero]:
                localctx = marzoParser.PrimariaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 12
                self.match(marzoParser.Numero)
                pass
            elif token in [marzoParser.Palabra]:
                localctx = marzoParser.PalabraContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(marzoParser.Palabra)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = marzoParser.SumaContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 16
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 17
                        self.match(marzoParser.T__0)
                        self.state = 18
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = marzoParser.RestaContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 19
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 20
                        self.match(marzoParser.T__1)
                        self.state = 21
                        self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = marzoParser.IgualContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 22
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 23
                        self.match(marzoParser.T__2)
                        self.state = 24
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = marzoParser.DividirContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 25
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 26
                        self.match(marzoParser.T__3)
                        self.state = 27
                        self.expression(5)
                        pass

                    elif la_ == 5:
                        localctx = marzoParser.MultiplicarContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 28
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 29
                        self.match(marzoParser.T__4)
                        self.state = 30
                        self.expression(4)
                        pass

                    elif la_ == 6:
                        localctx = marzoParser.MenorContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 31
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 32
                        self.match(marzoParser.T__5)
                        self.state = 33
                        self.expression(3)
                        pass

                    elif la_ == 7:
                        localctx = marzoParser.MayorContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 34
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 35
                        self.match(marzoParser.T__6)
                        self.state = 36
                        self.expression(2)
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfnoelseContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)

        def statement(self):
            return self.getTypedRuleContext(marzoParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfnoelse" ):
                listener.enterIfnoelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfnoelse" ):
                listener.exitIfnoelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfnoelse" ):
                return visitor.visitIfnoelse(self)
            else:
                return visitor.visitChildren(self)


    class PrintContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class DeclararPalabraContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Palabra(self):
            return self.getToken(marzoParser.Palabra, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclararPalabra" ):
                listener.enterDeclararPalabra(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclararPalabra" ):
                listener.exitDeclararPalabra(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclararPalabra" ):
                return visitor.visitDeclararPalabra(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.StatementContext)
            else:
                return self.getTypedRuleContext(marzoParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class DeclararNumeroContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Numero(self):
            return self.getToken(marzoParser.Numero, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclararNumero" ):
                listener.enterDeclararNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclararNumero" ):
                listener.exitDeclararNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclararNumero" ):
                return visitor.visitDeclararNumero(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = marzoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = marzoParser.IfnoelseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(marzoParser.T__7)
                self.state = 43
                self.expression(0)
                self.state = 44
                self.match(marzoParser.T__8)
                self.state = 45
                self.statement()
                pass

            elif la_ == 2:
                localctx = marzoParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(marzoParser.T__7)
                self.state = 48
                self.expression(0)
                self.state = 49
                self.match(marzoParser.T__8)
                self.state = 50
                self.statement()
                self.state = 53
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 51
                    self.match(marzoParser.T__9)
                    self.state = 52
                    self.statement()


                pass

            elif la_ == 3:
                localctx = marzoParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.match(marzoParser.T__10)
                self.state = 56
                self.expression(0)
                pass

            elif la_ == 4:
                localctx = marzoParser.DeclararNumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.match(marzoParser.T__11)
                self.state = 58
                self.match(marzoParser.Numero)
                pass

            elif la_ == 5:
                localctx = marzoParser.DeclararPalabraContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.match(marzoParser.T__12)
                self.state = 60
                self.match(marzoParser.Palabra)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         





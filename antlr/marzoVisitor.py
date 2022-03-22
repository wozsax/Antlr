# Generated from c:\Users\manue\OneDrive\Desktop\ejemplosANTLR\marzo\antlr\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete generic visitor for a parse tree produced by marzoParser.

class marzoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by marzoParser#program.
    def visitProgram(self, ctx:marzoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#suma.
    def visitSuma(self, ctx:marzoParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#palabra.
    def visitPalabra(self, ctx:marzoParser.PalabraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#mayor.
    def visitMayor(self, ctx:marzoParser.MayorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#menor.
    def visitMenor(self, ctx:marzoParser.MenorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#multiplicar.
    def visitMultiplicar(self, ctx:marzoParser.MultiplicarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#dividir.
    def visitDividir(self, ctx:marzoParser.DividirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#igual.
    def visitIgual(self, ctx:marzoParser.IgualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#primaria.
    def visitPrimaria(self, ctx:marzoParser.PrimariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#resta.
    def visitResta(self, ctx:marzoParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#ifnoelse.
    def visitIfnoelse(self, ctx:marzoParser.IfnoelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#if.
    def visitIf(self, ctx:marzoParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#print.
    def visitPrint(self, ctx:marzoParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#declararNumero.
    def visitDeclararNumero(self, ctx:marzoParser.DeclararNumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#declararPalabra.
    def visitDeclararPalabra(self, ctx:marzoParser.DeclararPalabraContext):
        return self.visitChildren(ctx)



del marzoParser
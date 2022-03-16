from antlr.marzoListener import marzoListener
from antlr.marzoParser import marzoParser

class GenCode(marzoListener):
    
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        print(".text")

    def exitPrimaria(self, ctx:marzoParser.PrimariaContext):
        print("load $1, " + ctx.Numero().getText())

    def exitSuma(self, ctx:marzoParser.SumaContext):
        print('ADD')

    def exitResta(self, ctx:marzoParser.RestaContext):
        print('SUBTRACTION')


    def exitMayor(self, ctx:marzoParser.MayorContext):
        print('mayor que')

    def exitMenor(self, ctx:marzoParser.MenorContext):
        print('menor que')

    def exitMultiplicar(self, ctx:marzoParser.MultiplicarContext):
        print('TIMES')

    def exitDividir(self, ctx:marzoParser.DividirContext):
        print('DIVIDE')

    def exitIgual(self, ctx:marzoParser.IgualContext):
        print('EQUALS')
    
    def exitIfnoelse(self, ctx:marzoParser.IfnoelseContext):
        print('IfnoElse')

    def exitIf(self, ctx:marzoParser.IfContext):
        print('If')

    def exitPrint(self, ctx:marzoParser.PrintContext):
        print('PRINT')

    def exitDeclararNumero(self, ctx:marzoParser.DeclararNumeroContext):
        print('declarar entero')

    def exitDeclararPalabra(self, ctx:marzoParser.DeclararPalabraContext):
        print('declarar palabra')

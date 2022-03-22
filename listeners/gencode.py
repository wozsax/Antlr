from antlr.marzoListener import marzoListener
from antlr.marzoParser import marzoParser

class GenCode(marzoListener):
    
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        print(".text")

    def exitPrimaria(self, ctx:marzoParser.PrimariaContext):
        print("load $1, " + ctx.Numero().getText())

    def exitSuma(self, ctx:marzoParser.SumaContext):
        print("ADD $v" + str((self.x)) +", " + "$v" + str(self.list2.pop()) + ", " + "$v" + str(self.list2.pop()))

    def exitResta(self, ctx:marzoParser.RestaContext):
        print("RESTA $v" + str((self.x)) +", " + "$v" + str(self.list2.pop()) + ", " + "$v" + str(self.list2.pop()))


    def exitMayor(self, ctx:marzoParser.MayorContext):
        print("mayor que $v" + str((self.x)) +", " + "$v" + str(self.list2.pop(1)) + ", " + "$v" + str(self.list2.pop()))

    def exitMenor(self, ctx:marzoParser.MenorContext):
        print("menor que $v" + str((self.x)) +", " + "$v" + str(self.list2.pop(1)) + ", " + "$v" + str(self.list2.pop()))

    def exitMultiplicar(self, ctx:marzoParser.MultiplicarContext):
        print("Times $" + str((self.x)) +", " + "$" + str(self.list2.pop()) + ", " + "$" + str(self.list2.pop()))

    def exitDividir(self, ctx:marzoParser.DividirContext):
        print("Divide $" + str((self.x)) +", " + "$" + str(self.list2.pop()) + ", " + "$" + str(self.list2.pop()))

    def exitIgual(self, ctx:marzoParser.IgualContext):
        print('EQUALS')
    
    def exitIfnoelse(self, ctx:marzoParser.IfnoelseContext):
        print('IfnoElse')

    def exitIf(self, ctx:marzoParser.IfContext):
        print("bequals $" + str(self.list.pop(0)) +", $" + str(self.list.pop(0)) + ", ELSE")

    def exitPrint(self, ctx:marzoParser.PrintContext):
        print('PRINT')

    def exitDeclararNumero(self, ctx:marzoParser.DeclararNumeroContext):
        print('declarar entero')

    def exitDeclararPalabra(self, ctx:marzoParser.DeclararPalabraContext):
        print("li $v" + str((self.x)) +", " + "$v" + str(self.list2.pop()) + ", " + "$v" + str(self.list2.pop()))

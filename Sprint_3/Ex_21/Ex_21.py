class Passaro:
    
    def __init__(self, som):
        self.som = som
    
    def voar(self):
        print("Voando...")
        
    def emitir_som(self):
        print(self.som)

class Pato( Passaro ):
    
    def __init__(self, som):
        print("Pato")
        super().__init__(som)
    
class Pardal( Passaro ):
    
    def __init__(self, som):
        print("Pardal")
        super().__init__(som)
    

pato = Pato("Quack Quack")

pato.voar()
print("Pato emitindo som...")
pato.emitir_som()

pardal = Pardal("Piu Piu")
print("Pardal emitindo som...")
pardal.emitir_som()
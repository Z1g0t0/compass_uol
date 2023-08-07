class Lampada():

    def __init__(self, ligada):
        self.ligada = ligada
        
    def liga(self):
        self.ligada = True
    
    def desliga(self):
        self.ligada = False
    
    def esta_ligada(self):
        return True if self.ligada else False
        
lamp = Lampada(False)

lamp.liga()
print('A lâmpada está ligada?', lamp.esta_ligada())
lamp.desliga()
print('A lâmpada ainda está ligada?', lamp.esta_ligada())


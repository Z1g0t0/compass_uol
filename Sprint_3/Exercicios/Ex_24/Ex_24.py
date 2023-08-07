class Ordenadora:
    
    def __init__( self, lista ):
        self.listaBaguncada = lista

    def ordenacaoCrescente( self ):
        self.listaBaguncada.sort()
        return self.listaBaguncada

    def ordenacaoDecrescente( self ):
        self.listaBaguncada.sort()
        return self.listaBaguncada[::-1]


l1 = [3, 4, 2, 1, 5]
crescente = Ordenadora(l1)
print(crescente.ordenacaoCrescente())

l2 = [9, 7, 6, 8]
decrescente = Ordenadora(l2)
print(decrescente.ordenacaoDecrescente())
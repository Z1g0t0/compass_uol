class Aviao:
    def __init__( self, modelo, velocidade_maxima, cor, capacidade ):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = 'azul'
        self.capacidade = capacidade

a1 = Aviao('BOIENG456', '1500 km/h', '', 400)
a2 = Aviao('Embraer Praetor 600', '863km/h', '', 14)
a3 = Aviao('Antonov An-2', '258 Km/h', '', 12)

avioes = [a1, a2, a3]

for aviao in avioes:
    print('O avião de modelo', aviao.modelo, 'possui uma velocidade máxima de', aviao.velocidade_maxima, 'capacidade para', aviao.capacidade, 'passageiros e é da cor', aviao.cor)
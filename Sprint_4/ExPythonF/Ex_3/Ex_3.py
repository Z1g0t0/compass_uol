
from functools import reduce

def calcula_saldo(lancamentos) -> float:
    #continue este código
    valores = map(lambda x: x[0] * -1 if 'D' in x else x[0], lancamentos)
    saldo = reduce(lambda cont, valor: cont + valor, valores, 0)
    
    return saldo
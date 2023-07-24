
# Usei a funcao eval() pois foi a que consegui elaborar para uma solucao de forma enxuta, considera-se entao que os parametros operadores/operandos sao de fonte/intento confiaveis

def calcular_valor_maximo(operadores,operandos) -> float:

    combine = map(lambda x: str(x[1][0]) + x[0] + str(x[1][1]), zip(operadores, operandos))

    return max(map(lambda x: eval(x), combine))
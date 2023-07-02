import random

random_list = random.sample(range(500), 50)

def median(lista):

    lista.sort()
    if len(lista)%2 != 0:
        return lista[(len(lista)//2)]
    else:
        return (lista[(len(lista)//2)] + lista[(len(lista)//2)-1])/2

def mean(lista):
    return sum(lista)/len(lista)

mediana = median(random_list)
media = mean(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print('Media:', str(media) + ',', 'Mediana:', str(mediana) + ',', 'Mínimo:', str(valor_minimo) + ',', 'Máximo:', str(valor_maximo))
def sum_total(lista):

    return sum(map(int, lista.split(',')))
    
lista = "1,3,4,6,10,76"

print(sum_total(lista))
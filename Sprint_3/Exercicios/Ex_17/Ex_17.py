def split_equal(lista):
    parts = len(lista)//3
    l = ''
    for i in range(3):
        l = l + str(lista[i*parts:(i+1)*parts]) + ' '
    return l

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

l = split_equal(lista)

print(l[:-1])


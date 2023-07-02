def f(n):
    return pow(n, 2)

def my_map(list, f):
    lst = []
    for i in list:
        lst.append(f(i))
    print(lst)
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_map(lista, f)
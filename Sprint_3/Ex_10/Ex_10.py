def single(lista):
    return list(set(lista))


lst = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
print(single(lst))
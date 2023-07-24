
with open('number.txt', 'r') as f:
    inteiros = map(lambda x: int(x), f)
    pares = filter(lambda x: x % 2 == 0, inteiros)
    pares = sorted(pares, reverse=True)
    print(pares[:5])
    print(sum(pares[:5]))

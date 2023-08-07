class Ator:
    
    def __init__( self, nome, total, number, average, most_popular, gross ):
        self.nome = nome
        self.total = total
        self.number = number,
        self.average = average
        self.most_popular = most_popular
        self.gross = gross


atores = []
with open('actors.csv', 'r') as f:
    next(f)
    next(f)
    for line in f:
        if '"' in line:
            name = line[line.index('"')+1 : line.index('",')]
            name = name.replace(',', '')
            line = name + line[line.index('",')+1:]

        ator = Ator(*(line.split(',')))
        atores.append(ator)

# 1. 
print("\nExercicio 1:\n")
num = 0
for ator in atores:
    if int(ator.number[0]) > num:
        num = int(ator.number[0])
        volui = ator

print(volui.nome, '-',  num)

# 2.
print("\n\nExercicio 2:\n")
for ator in atores:
    print(ator.nome, '-', ator.average)

# 3. 
print("\n\nExercicio 3:\n")
num = 0
for ator in atores:
    if float(ator.average) > num:
        num = float(ator.average)
        volui = ator
print(volui.nome, '-', num)

# 4.
print("\n\nExercicio 4:\n")
movies = []
counter = []
for ator in atores:
    if ator.most_popular not in movies:
        movies.append(ator.most_popular)
        counter.append(1)
    else:
        counter[movies.index(ator.most_popular)] += 1

print(movies[counter.index(max(counter))], '-',  max(counter))

# 5.
print("\n\nExercicio 5:\n")
atores.sort(key=lambda x: x.total, reverse=True)

for ator in atores:
    print(ator.nome, '-', ator.total)

def ex_5( line ):

    nome = line.split(',')[0]
    notas = map(lambda x: int(x), line.split(',')[1:])
    notas = sorted(list(notas), reverse=True)[:3]
    mean = round(sum(notas)/len(notas), 2)

    return [nome, notas, mean]

with open('estudantes.csv', 'r') as f:

    estudantes = [ex_5(line) for line in f]

    for estudante in sorted(estudantes):
        print(f'Nome: {estudante[0]} Notas: {estudante[1]} Média: {estudante[2]}')

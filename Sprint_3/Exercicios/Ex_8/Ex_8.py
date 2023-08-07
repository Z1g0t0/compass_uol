words = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for word in words:
    if word[::-1] == word:
        print('A palavra:', word, 'é um palíndromo')
    else:
        print('A palavra:', word, 'não é um palíndromo')
#Você deve Utilizar a função enumerate().

primeiroNome = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNome = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idade = [19, 28, 25, 31]

for count, value in enumerate(idade):
    print(count, "-", primeiroNome[count], sobreNome[count], "está com", value, "anos")
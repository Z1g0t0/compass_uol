import random
import time
import names

size = 250

if __name__ == "__main__":

    #random_list = [ random.randint(1, 99999999) for i in range(size) ]
    #random_list.reverse()
    #print(random_list[:5], len(random_list))

    ####################################################

    # Define a semente de aleatoriedade

    random.seed(40)

    qtd_nomes_unicos = 3000

    qtd_nomes_aleatorios = 10000000

    aux=[]

    for i in range(0, qtd_nomes_unicos):
    
        aux.append(names.get_full_name())
    
    print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))
    
    dados=[]

    for i in range(0, qtd_nomes_aleatorios):

        dados.append(random.choice(aux))

    with open("nomes_aleatorios.txt", "w") as f:
        for nome in dados:
            f.write(nome + '\n')
    
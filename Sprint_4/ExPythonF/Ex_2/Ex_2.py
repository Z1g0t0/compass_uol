
def conta_vogais(texto:str)-> int:
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    count = filter(lambda x: x in vogais, texto)
    
    return len(list(count))


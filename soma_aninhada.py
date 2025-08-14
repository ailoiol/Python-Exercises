#o exercício pede uma função que calcule o valor de todos os elementos numa input, podendo ser uma list de números inteiros ou um número inteiro
#ex: [1,1{3,11},{1,1,1}] // output= 19

def soma_aninhada(L):
    total = 0
    for item in L:
        if isinstance(item, int): #verifica se o item é um número inteiro
            total += item
        elif isinstance(item, list): #verifica se é uma lista de números inteiros
            total += soma_aninhada(item) #soma todos os números da lista
    return total

def remove_duplicatas (lista):
    x=[] #cria uma nova lista 
    for i in lista: #para cada numero na lista anterior
        if i not in x: #se esse numero não estiver na nova lista o adicione
            x.append(i)
    return x
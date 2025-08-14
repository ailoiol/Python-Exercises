a=list(map(int, input().split()))
visto=[] #lista para usar de parâmetro quais elementos estão ou não repetidos
for n in a:
    if n in visto:
        print ('True') #retorna true caso tenha elementos repetidos
        break
    else:
       visto.append(n) #adiciona o elemento à lista de vistos
else:
    print ('False')
t=int(input())
chinelos=list(map(int, input().split()))

chinelos.sort() #ordena os itens em ordem crescente
for i in range(len(chinelos)): #len (chinelos) é para o range identificar a qntd de itens na lista chinelos
    if chinelos[i] >= t:
        print (i)
        break
else:
    print ('-1')
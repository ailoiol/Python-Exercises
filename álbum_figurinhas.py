n = int(input())
m = int(input())
figurinhas=set()
for _ in range (m):
    x=int(input())
    figurinhas.add(x)
y= n-len(figurinhas)
print(y)


#Primeira linha contém o número total de figurinhas, e o programa deve retornar quantas faltam para completar o álbum
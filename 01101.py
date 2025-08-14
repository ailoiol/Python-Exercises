n=int(input())
for _ in range (n):
    x=input()
    a=x.find('1') #retorna a posição do primeiro 1, se não tiver retorna -1
    b=x.rfind('1') #retorna a posição do último 1
    print(0 if a == -1 else x[a:b+1].count('0')) #pega quantos caracteres existem entre o primeiro e ultimo 1 e conta o numero de zeros entre eles
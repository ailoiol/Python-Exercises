n=int(input())
x=0
for _ in range (n):
    i= input()
    if i=='X++' or i=='++X':
        x+=1
    elif i=='X--' or i=='--X':
        x-=1
print (x)
        

#caso a input tenha um 'x++' ou '++x' deve-se adicionar 1 ao total
#caso a input tenha um 'x--' ou '--x' deve-se subtrair 1 ao total
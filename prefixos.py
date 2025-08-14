#função de soma de todos os vetores
#ex: 1,2,3 retorna: 1,3,6

x=list(map(int, input().split()))
prefixos=[] #lista de retorno da soma dos prefixos
a=0
for y in x: #para um número na lista x
    a += y #calcula a soma dos prefixos // na segunda vezn a=1 e y=2 por exemplo, então guardará o valor 3 à nova lista
    prefixos.append(a)
print (*prefixos)
print (*x)
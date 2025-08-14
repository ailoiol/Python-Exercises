n=int(input())
a=list(map(int, input().split()))
a.sort(reverse=True) #os 11 primeiros serão os jogadores com maior habilidade
x=a[:11] #pega os 11 primeiros da lista em ordem crescente
t=0
for y in x:
    t+=y #soma o total das habilidades dos jogadores titulares juntos
k=min(11,n-11) #pega o total de jogadores disponiveis para ficar no banco
r=0
for y in a[11:11+k]:
    r+=y #soma o total das habilidades dos reservas
print (t-r) #diferença entre os titulares e os reservas
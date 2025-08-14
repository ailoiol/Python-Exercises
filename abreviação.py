n = int(input())

for _ in range(n):
    palavra = input().strip()
    if len(palavra) > 10:
        abreviada = palavra[0] + str(len(palavra) - 2) + palavra[-1]
        print(abreviada)
    else:
        print(palavra)


#meu código
n=int(input())
for _ in range(n):
  p=input()
  if len(p)<=10:
    print (p)
  else:
    resposta=p[0]+str(len(p)-2)+p[-1] #esse -1 percorre diretamente a última letra da palavra
    print (resposta)


#variação desse exercício, conta quantas vogais tem no meio da palavra
n=int(input())
for _ in range(n):
  p=input()
  if len(p)<=5:
    print (p)
  else:
    meio = p[1:-1]
    vogais = sum(1 for c in meio if c.lower() in "aeiou")
    resposta=p[0]+str(vogais)+p[-1]
    print (resposta)
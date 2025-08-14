x = int(input())  # número de consultas

for _ in range(x):
    entrada = input().split()
    l = int(entrada[0])      # primeiro parametro, 0 por exemplo
    r = int(entrada[1])      # ultimo parametro, 2 por exemplo
    s = entrada[2]           # string a ser manipulada, por exemplo Galileu

    # pega a substring de l até r (inclusive) e inverte
    invertida = s[l:r+1][::-1] #de l até r, e o [::-1] inverte isso

    print(invertida)

#input: 2
# 0 2 Galileu
#output: laG
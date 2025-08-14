n = int(input())
s = input().strip()

# Verifica se n é divisível por 4
if n % 4 != 0:
    print("Feiticeiro misterioso")
else:
    from collections import Counter

    count = Counter(s)
    alvo = n // 4

    # Conta o número de ? disponíveis
    faltando = 0
    for letra in "ACGT":
        atuais = count.get(letra, 0)
        if atuais > alvo:
            print("Feiticeiro misterioso")
            break
        faltando += alvo - atuais
    else:
        # Se temos interrogações suficientes
        if faltando == count.get('?', 0):
            print("Segredos desvendados")
        else:
            print("Feiticeiro misterioso")


#código que eu tentei fazer
n = int(input())
s = input()

a = 0
t = 0
g = 0
c = 0
q = 0

for i in s:
    if i == 'A':
        a += 1
    elif i == 'T':
        t += 1
    elif i == 'G':
        g += 1
    elif i == 'C':
        c += 1
    elif i == '?':
        q += 1

need = n // 4

# 1) Se n não for divisível por 4, impossível
if n % 4 != 0:
    print('Feiticeiro Misterioso')
else:
    # 2) Se já passou do limite de alguma letra, impossível
    if a > need or t > need or g > need or c > need:
        print('Feiticeiro Misterioso')
    else:
        # 3) Verifica se as interrogações completam o que falta
        x = (need - a) + (need - t) + (need - g) + (need - c)
        if x == q:
            print('Segredos desvendados')
        else:
            print('Feiticeiro Misterioso')

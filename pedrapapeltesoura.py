n = int(input())

ganha_de = {
    "pedra": "tesoura",
    "tesoura": "papel",
    "papel": "pedra"
}

for _ in range(n):
    jog1, jog2 = input().strip().split()
    
    if jog1 == jog2:
        print("Empate.")
    elif ganha_de[jog1] == jog2:
        print("Jogador 01 venceu.")
    else:
        print("Jogador 02 venceu.")

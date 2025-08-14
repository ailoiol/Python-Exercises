
s = input().strip()

corinthians = '0000000' in s
sao_paulo = '1111111' in s

if corinthians and sao_paulo:
    print("JOGO PESADO")
elif corinthians:
    print("VAI TIMAO")
elif sao_paulo:
    print("VAMO TRICOLOR")
else:
    print("BORA UM VIRTUAL NO CODEFORCES")

    #se tiverem 7 jogadores um do lado do outro a situação é favoravel para o time
    #1 são jogadores do são paulo e 0 do corinthians
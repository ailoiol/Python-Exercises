def imprime_tabuleiro(tab):
    for linha in tab:
        print(' ' + '  '.join(linha))
def imprime_tabuleiro(tab):
    for linha in tab:
        print(' ' + '  '.join(linha))

def jogoTerminou(matriz):
    for i in range(3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] != '-':
            return 1
        if matriz[0][i] == matriz[1][i] == matriz[2][i] != '-':
            return 1
    if matriz[0][0] == matriz[1][1] == matriz[2][2] != '-':
        return 1
    if matriz[0][2] == matriz[1][1] == matriz[2][0] != '-':
        return 1
    for linha in matriz:
        if '-' in linha:
            return 0
    return 2

def main():
    tabuleiro = [['-' for _ in range(3)] for _ in range(3)]
    jogador = 'X'

    while True:
        imprime_tabuleiro(tabuleiro)

        while True:
            try:
                l, c = map(int, input().split())
                if 0 <= l <= 2 and 0 <= c <= 2:
                    if tabuleiro[l][c] == '-':
                        break
            except:
                pass

        tabuleiro[l][c] = jogador

        status = jogoTerminou(tabuleiro)
        if status == 1:
            imprime_tabuleiro(tabuleiro)
            print("Ganhou")
            break
        elif status == 2:
            imprime_tabuleiro(tabuleiro)
            print("Empate")
            break

        jogador = 'O' if jogador == 'X' else 'X'

if __name__ == "__main__":
    main()

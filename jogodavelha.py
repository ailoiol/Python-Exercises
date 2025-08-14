def jogoTerminou(matriz):
    for i in range(3):
        # Verifica linhas
        if matriz[i][0] == matriz[i][1] == matriz[i][2] != ' - ':
            return 1
        # Verifica colunas
        if matriz[0][i] == matriz[1][i] == matriz[2][i] != ' - ':
            return 1

    # Verifica diagonais
    if matriz[0][0] == matriz[1][1] == matriz[2][2] != ' - ':
        return 1
    if matriz[0][2] == matriz[1][1] == matriz[2][0] != ' - ':
        return 1

    # Verifica espaços vazios
    for linha in matriz:
        if ' - ' in linha:
            return 0

    return 2

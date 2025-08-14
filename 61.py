def decompress(x):
    palavra = ""
    while x > 0:
        letra_valor = x & 31  # pega os últimos 5 bits
        letra = chr(letra_valor - 1 + ord('A'))
        palavra += letra  # adiciona no final, mantendo a ordem correta
        x >>= 5  # desloca 5 bits para a direita
    return palavra

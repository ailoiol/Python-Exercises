def desenha_forca(erros):
    forca = [
        " +---+",
        " |   |",
        "     |",
        "     |",
        "     |",
        "     |",
        "========"
    ]

    if erros >= 1:
        forca[2] = " O   |"
    if erros >= 2:
        forca[3] = " |   |"
    if erros >= 3:
        forca[3] = "/|   |"
    if erros >= 4:
        forca[3] = "/|\  |"
    if erros >= 5:
        forca[4] = "/    |"
    if erros >= 6:
        forca[4] = "/ \  |"

    for linha in forca:
        print(linha)

palavra_secreta = input("Digite a palavra secreta: ").lower()
print()

letras_descobertas = ['_'] * len(palavra_secreta)
letras_digitadas = []
erros = 0
limite_erros = 6

desenha_forca(erros)
print()
print(' '.join(letras_descobertas) + ' ')

while True:
    letra = input("Digite uma letra: ").lower()
    print()

    letras_digitadas.append(letra)

    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_descobertas[i] = letra
    else:
        erros += 1

    desenha_forca(erros)
    print()
    print(' '.join(letras_descobertas) + ' ')

    if '_' not in letras_descobertas:
        print(f'Sim! A palavra secreta eh "{palavra_secreta}"')
        break

    if erros >= limite_erros:
        print("Voce teve muitas oportunidades e perdeu!")
        break
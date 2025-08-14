senha = input()

if len(senha) < 6 or len(senha) > 32: #caso a senha seja invalida, já para aqui, por isso o for está dentro
    print('Senha invalida')
else:
    minusculas = 0
    maiusculas = 0
    digitos = 0
    invalidos = 0

    for i in senha:
        if i.islower():  # letras minúsculas
            minusculas += 1
        elif i.isupper():  # letras maiúsculas
            maiusculas += 1
        elif i.isdigit():  # dígitos
            digitos += 1
        else:
            invalidos += 1

    if invalidos >= 1: #caso haja um caractere invalido já quebra
        print('Senha invalida')
    elif minusculas != 0 and maiusculas != 0 and digitos != 0:
        print('Senha valida')
    else:
        print('Senha invalida')

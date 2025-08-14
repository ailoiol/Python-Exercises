N = int(input())

for _ in range(N):
    s = input().strip()
    i = 0
    resultado = ""

    while i < len(s):
        letra = s[i]  # letra maiúscula
        i += 1

        # Agora vamos ler o número que vem após a letra
        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1

        # Converter para inteiro e repetir a letra
        qtd = int(num_str)
        resultado += letra * qtd

    print(resultado)

senha = input().strip()

# Verifica o tamanho
if not (6 <= len(senha) <= 32):
    print("Senha invalida.")
    exit()

# Flags para as verificações
tem_maiuscula = False
tem_minuscula = False
tem_numero = False

# Verifica cada caractere
for c in senha:
    if c.isupper():
        tem_maiuscula = True
    elif c.islower():
        tem_minuscula = True
    elif c.isdigit():
        tem_numero = True
    else:
        # Se for qualquer outro caractere, inválido
        print("Senha invalida.")
        exit()

# Verifica se todos os requisitos foram atendidos
if tem_maiuscula and tem_minuscula and tem_numero:
    print("Senha valida.")
else:
    print("Senha invalida.")

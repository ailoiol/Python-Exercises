s = input().strip()
n = len(s)

# Conta os pares simétricos diferentes
erros = 0
for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        erros += 1

# Agora decidimos
if erros == 1:
    print("ON")  # uma troca resolve
elif erros == 0 and n % 2 == 1:
    print("ON")  # já é palíndromo, mas podemos trocar o caractere do meio
else:
    print("OFF")  # não dá pra resolver com uma troca só

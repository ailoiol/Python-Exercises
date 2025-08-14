s = input().strip()
vogais = 'aeiou'

for x in vogais:
    resultado = ''
    for c in s:
        if c in vogais:
            resultado += x
        else:
            resultado += c
    print(resultado)

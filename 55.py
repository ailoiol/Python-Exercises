s = input()
corrigida = []

i = 0
while i < len(s):
    if s[i] == 'n' and i + 1 < len(s) and s[i + 1] in ('p', 'b'):
        corrigida.append('m')  # troca 'n' por 'm'
    else:
        corrigida.append(s[i])
    i += 1

print(''.join(corrigida))

s = input()
disparos = 0

for i in range(len(s)):
    if s[i] == 'o' and (i == 0 or s[i-1] == '.'): #a condição diz que caso não haja um . antes, não se deve contar o 'o' como um navio
        disparos += 1

print(disparos)


#barcos são compostos de o e os . são a água
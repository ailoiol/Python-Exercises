
#5
#abcda

#output:abca

n = int(input())
s = input()

for i in range(n - 1):
    if s[i] > s[i + 1]: #se a variável for maior que a próxima termina o if, exemplo, de d>a, logo retira-se o d
        print(s[:i] + s[i+1:]) 
        break
else:
    print(s[:-1])

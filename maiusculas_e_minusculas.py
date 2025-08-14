s = input().strip()

maiusculas = sum(1 for c in s if c.isupper()) #essa linha faz toda a função do for no codigo abaixo
minusculas = len(s) - maiusculas

if maiusculas > minusculas:
    print(s.upper())
else:
    print(s.lower())



#que eu escrevi
s=input().strip()

maiusculas=0
minusculas=0

for i in s:
  if i.islower():
    minusculas+=1
  elif i.isupper():
    maiusculas+=1

if maiusculas>minusculas:
  print (s.upper())
else:
  print (s.lower())
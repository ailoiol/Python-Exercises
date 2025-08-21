senha=input()
maiuscula=False
minuscula=False
numero=False
if 6<=len(senha)<=32:
  for i in senha:
    if i.isupper():
      maiuscula=True
    elif i.islower():
      minuscula=True
    elif i.isdigit():
      numero=True
    else:
      print ('Senha inválida')

if maiuscula and minuscula and numero:
  print ('Senha válida')
else:
  print ('Senha inválida')
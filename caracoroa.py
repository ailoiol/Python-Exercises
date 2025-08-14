import random

num = random.randint(0, 1)   # Gera um número aleatório dentro desse intervalo

if num > 0.5:
  print('Cara')
else:
  print('Coroa')
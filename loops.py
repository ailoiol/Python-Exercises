for i in range(99, 0,-1): #inicio,fim,padrão (no caso o padrão é subtrair 1 de i)
  print (f'{i} bottles of beer on the wall')
  print (f'{i} bottles of beer')
  print ('Take one down, pass it around')
  print (f'{i-1} bottles of beer on the wall')


#segundo código de looping

guess = 0
tries=0

while guess != 6:
  guess = int(input("Guess the number:  "))
  tries+=1
  if guess==6:
    print("You got it!")
    break
  elif tries==3:
    print("You failed!")
    break

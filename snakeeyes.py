import random

total=0
x=0

while total!=2:
    print ('Nope')
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    x+=1

#soma de dois dados=1
print ('Snake Eyes!')
print (f'It only took you {x} {'try' if x==1 else 'tries'}')
g=0
r=0
h=0
s=0

print ('Q1) Do you like Dawn or Dusk?')
print ('1) Dawn')
print ('2) Dusk')
x=int(input())
if x==1:
  g+=1
  r+=1
elif x==2:
  s+=1
  h+=1
else:
  print ('Wrong input.')

print ('Q2) When I’m dead, I want people to remember me as:')
print ('1) The Good')
print ('2) The Great')
print ('3) The Wise')
print ('4) The Bold')
y=int(input())
if y==1:
  h+=2
elif y==2:
  s+=2
elif y==3:
  r+=2
elif y==4:
  g+=2
else:
  print ('Wrong input.')

print ('Q3)Which kind of instrument most pleases your ear?')
print ('1) The violin')
print ('2) The trumpet')
print ('3) The piano')
print ('4) The drum')
z=int(input())
if z==1:
  s+=4
elif z==2:
  h+=4
elif z==3:
  r+=4
elif z==4:
  g+=4
else:
  print ('Wrong input.')

if g>r and g>h and g>s:
  print ('Gryffindor')
elif r>g and r>h and r>s:
  print ('Ravenclaw')
elif h>g and h>r and h>s:
  print ('Hufflepuff')
elif s>g and s>r and s>h:
  print ('Slytherin')
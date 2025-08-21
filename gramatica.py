s=input()
c=[]
for i in range(len(s)):
  if s[i]=='n':
    if i+1 < len(s) and s[i+1] in 'pb': #para não ter risco de percorrer a ultima letra
      c.append('m')
    else:
      c.append('n')
  else:
    c.append(s[i])

print("".join(c))

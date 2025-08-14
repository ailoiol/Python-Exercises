palavra=input()
maiuscula=[]
for i in palavra:
    if i.islower():
        x=i.upper() #transforma uma letra minuscula em maiuscula
        maiuscula.append(x)
    else:
        maiuscula.append(i)
print (''.join(maiuscula)) #para que as letras não sejam escritas com espaços entre elas
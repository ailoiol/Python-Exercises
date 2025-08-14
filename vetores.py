def maior_norma (a,b):
    A=sum(abs(x) for x in a) #sum é soma de todos os elementos
    B=sum(abs(x) for x in b) #abs é para que se some o valor em módulo dos números na lista de vetores

    if A>B:
        print('PRIMEIRO')
    else:
        print('SEGUNDO')
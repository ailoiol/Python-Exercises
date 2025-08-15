import random 
wordbank=['radio','furia','censo','pareo','orfao','vapor','oasis','marte']
palavra=random.choice(wordbank)

linha = ['_']*len(palavra) #cria o 'tabuleiro' para que o jogador advinhe a palavra
tentativas=5
while tentativas>0:
  print ('\nPalavra atual: '+ ' '.join(linha)) #transforma a lista 'linha' em uma string basicamente
  letra = input('Advinhe uma letra: ').lower() #para que o codigo não descarte uma letra maiuscula mesmo que esteja na palavra
  if letra in palavra:
    tentativas-=1
    for i in range (len(palavra)): #atribui um numero para cada letra
      if palavra[i]==letra: #quando a letra advinhada estiver na mesma posição da letra na palavra
        linha[i]=letra #adiciona-se a letra na exata posição que ela está na palavra
    print ('\nBom palpite!')
    print ('Tentativas restantes: '+ str(tentativas))
  else:
    tentativas-=1
    print ('\nTente outra letra')
    print ('Tentativas restantes: '+ str(tentativas))

  if '_' not in linha: #se a palavra foi descoberta
    print ('Parabéns!')
    break
else: #printa isso apenas se o jogador perder
  print ('Tente novamente mais tarde')

s = input()

# Substitui todas as ocorrências de "WUB" por espaço
s = s.replace("WUB", " ")

# Divide a string em palavras (removendo múltiplos espaços)
palavras = s.split()

# Junta as palavras com um único espaço e imprime
print(" ".join(palavras))

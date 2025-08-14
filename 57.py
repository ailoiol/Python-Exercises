X = input().strip()
Y = input().strip()

distancia = 0
for x, y in zip(X, Y):
    if x != y:
        distancia += 1

print(distancia)

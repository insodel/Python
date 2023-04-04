# Realiza un programa que, dado un array de números de 5 posiciones con 
# números aleatorios, guardar los valores de este array en otro array, pero 
# con los valores invertidos.

import random

n = 5
arrayOriginal = []
arrayInverso = []

for x in range(n):
    arrayOriginal.append(random.randint(0,50))
    arrayInverso.append(arrayOriginal[x])

arrayInverso.reverse()

for x in range(n):
    print("La posición", x, "del primer array tiene un valor de", arrayOriginal[x])
for x in range(n):
    print("La posición", x, "del array invertido tiene un valor de", arrayInverso[x])


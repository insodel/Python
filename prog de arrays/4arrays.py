# Realiza un programa que contenga un array de 100 números aleatorios.
# El usuario indicará un número, y el programa buscará dicho número e
# indicará cuántas veces aparece y en qué posiciones.
import random

miArray = []

for x in range(1,100):
    miArray.append(random.randint(0,50))

numABuscar = int(input("Introduce el número a buscar:\n"))
conteo = 0

for x in range(len(miArray)):
    if miArray[x] == numABuscar:
        conteo = conteo + 1
        print("El número", numABuscar, "ha sido encontrado por", conteo, "vez en la posición", x)
    else: 
        continue
""" 
Realiza un programa que cree un array donde el usuario elija el número
de elementos que contiene y se rellene el array con los múltiplos de otro
número pedido por teclado. 
"""
import random

size = int(input("Introduzca el tamaño del array:\n"))
miArray = []

for x in range(size):
    miArray.append(random.randint(0,20))
    print("El elemento", x, "en el array tiene un valor de", miArray[x])

numeroMultiplo = int(input("Elija el número múltiplo:\n"))

for x in range(len(miArray)):
    miArray[x] = miArray[x] * numeroMultiplo
    print("El elemento", x, "en el array multiplicado tiene un valor de", miArray[x])




# Realiza un programa que tenga dos arrays del mismo tamaño, lo
# introducirá el usuario por teclado. En uno de ellos almacenarás nombres
# de personas como cadenas, mientras que en el otro se irán almacenando
# la longitud de los nombres.

size = int(input("Introduzca el tamaño de los arrays:\n"))
arrayNombres = []
arraySizes = []

for x in range (size):
    arrayNombres.append(input())

for x in range (len(arrayNombres)):
    arraySizes.append(len(arrayNombres[x]))

for x in range (len(arrayNombres)):
    print("El tamaño del nombre", arrayNombres[x], "es de", arraySizes[x], "carácteres.")
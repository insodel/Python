# Realiza un programa con dos array de n elementos, y los sume en un 
# nuevo array. Mostrará los tres arrays.
import random

numElementos = int(input("Introduzca el número de elementos de los arrays:\n"))
primerArray = []
segundoArray = []
arrayResultado = []

for x in range(numElementos):
    primerArray.append(random.randint(0,9))
    segundoArray.append(random.randint(0,9))
    arrayResultado.append(primerArray[x] + segundoArray[x]) 

print("array A | array B   | suma de A y B")
for x in range(numElementos):
    print(primerArray[x], "      |    ", segundoArray[x], "    |  ", arrayResultado[x])
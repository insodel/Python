# Realiza un programa con un array con N notas de 0 a 20, calcule el 
# promedio de aprobados y el promedio de los suspensos e indique la 
# cantidad de aprobados y desaprobados.
import random

size = int(input("Introduzca el número de notas:\n"))
arrayNotas = []
conteoAprobados = 0
conteoSuspensos = 0
sumaAprobado = 0
sumaSuspenso = 0

for x in range(size):
    arrayNotas.append(random.randint(0,20))
    if (arrayNotas[x] >= 10):
        sumaAprobado += arrayNotas[x]
        conteoAprobados = conteoAprobados + 1
    else:
        sumaSuspenso += arrayNotas[x]
        conteoSuspensos = conteoSuspensos + 1

promedioAprobado = sumaAprobado / size
promedioSuspenso = sumaSuspenso / size

print("El promedio de la nota de las personas que han aprobado es de", promedioAprobado, "puntos sobre 10.", conteoAprobados, "personas han aprobado.")
print("El promedio de la nota de las personas que han suspendido es de", promedioSuspenso, "puntos sobre 10.", conteoSuspensos, "personas han suspendido.")
    


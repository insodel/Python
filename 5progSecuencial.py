import math

catetoA = int(input("Introduce el primer cateto:\n"))
catetoB = int(input("Introduce el segundo cateto:\n"))

hipotenusaAlCuadrado = (catetoA*catetoA) + (catetoB*catetoB)
hipotenusa = math.sqrt(hipotenusaAlCuadrado)
print("La hipotenusa de un rectángulo con catetos", catetoA, "y", catetoB, "es", float(hipotenusa))
# Realiza un programa que pida un número, y calcule el perímetro de la 
# circunferencia y el área del círculo con ese radio.


import math

radio = float(input("Introduzca el radio: \n"))

pi = math.pi
area = pi * radio * radio
perimetro = 2 * pi * radio

print("El área del círculo es", area, "y el perímetro de la circunferencia es", perimetro)
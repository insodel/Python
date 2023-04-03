# Realiza una modificación al programa anterior. El consumo del coche será 
# fijado por el programador a 5 litros a los 100 kilómetros.

distanciaViaje = int(input("Introduce el número de kilometros del viaje:\n"))
precioGasolina = float(input("Introduce el precio de la gasolina:\n"))
consumoCoche = 5

consumo100 = consumoCoche / 100
precioViaje = precioGasolina * consumo100 * distanciaViaje

print("El viaje de", distanciaViaje, "te saldrá por", precioViaje,"euros.")
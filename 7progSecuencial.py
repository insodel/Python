# Realiza un programa que calcule el coste del precio de la gasolina en un 
# viaje. El usuario introducirá los kilómetros a recorrer, el precio de la 
# gasolina y el consumo del coche en litros por cada 100 kilómetros.

distanciaViaje = int(input("Introduce el número de kilometros del viaje:\n"))
precioGasolina = float(input("Introduce el precio de la gasolina:\n"))
consumoCoche = int(input("Introduce el consumo del coche:\n"))

consumo100 = consumoCoche / 100
precioViaje = precioGasolina * consumo100 * distanciaViaje

print("El viaje de", distanciaViaje, "te saldrá por", precioViaje,"euros.")
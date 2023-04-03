# Realiza un programa que calcule el valor de pesetas de una cantidad de euros. 
# La cantidad de euros se entra por teclado.

pesetas = 166.00  # No es el valor exacto de las pesetas, pero es lo que usa el enunciado

euros = float(input("Introduce la cantidad de euros:\n"))
eurosPesetas = euros * pesetas

print(euros, "euros son", eurosPesetas, "pesetas.")

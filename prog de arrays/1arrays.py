# Realiza un programa que cree un array de 10 elementos, y lo rellene con
# 5 cifras más de su posición.
# Ejemplo: Posición 0 – Valor 5. Posición 1 – Valor 6.

arrayOriginal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in range(len(arrayOriginal)):
    arrayOriginal[x] = x + 5
    

for x in range(len(arrayOriginal)):
    print("Posición", x, "- Valor:", arrayOriginal[x])
# Ahora hablaremos sobre como asignamos un valor a una variable (o varias) en Python

# Podemos asignar valores a más de una variable en una sola línea:
variableUno, variableDos = "contenido de variableUno", "contenido de variableDos"
print(variableUno)
print(variableDos)

# También podemos asignar un mismo valor a varias variables diferentes:
x = y = z = "Hola"
print(x)
print(y)
print(z)

# Otra cosa chachi, desempaquetar tuplas:
frutas = ["manzana", "mandarina", "fresa"]
a, b, c = frutas 

print(a)
print(b)
print(c)
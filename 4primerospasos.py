# A diferencia de C#, 
# Python no requiere indicar el tipo de variable.
# Esto permite que las siguientes declaraciones sean todas válidas:

x = 1
y = 1.5
z = "soy una cadena"

# Podemos cambiar el tipo de una variable asignándole
# un valor de tipo diferente al original tal que así:

x = "ahora yo soy una cadena"
y = 1
z = 1.5

# Como seguramente hayas deducido, print() permite mostrar contenido por pantalla. 
# Si no lo has probado ya, te ánimo a intentarlo con los ejemplos siguientes.


# También podemos hacer Casting a una variable. Ejemplo para cambiar el valor de 3:
a = str(3)  # a almacenará 3 como string (cadena, como "3" o '3')
b = int(3)  # b almacenará 3 como int (entero, como 3) 
z = float(3) # c almacenará 3 como float (3.0)


# Si queremos saber el tipo de datos de una variable, usamos type()

print(type(a)) # esto devolverá por pantalla <class 'str'> indicando que es de tipo string
print(type(b)) # esto devolverá <class 'int'>
print(type(z)) # esto devolverá <class 'float'>
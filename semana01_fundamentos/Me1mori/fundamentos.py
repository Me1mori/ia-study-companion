# Variables
Nombre = "Me1mori"
edad = 44

""""
Variables:
En Python solo se escribe el nombre de la variable y dependiendo
del valor que se le asigne, Python lo interpreta automáticamente.
Si es una cadena de texto, se usan comillas (" ") y se convierte
en tipo str (string). Para definir un número entero se escribe
directamente (int), y para decimales se usa un punto (float).
También existen las variables booleanas: True y False, que sirven
para validar condiciones en ciertas situaciones.

Si defines una variable fuera de funciones, bucles o condicionales,
se vuelve una variable global, lo que significa que puede ser
usada desde cualquier parte del código.

Funciones:
Se definen con la palabra clave 'def', seguida del nombre de la
función y paréntesis (). Si la función recibe variables, se
escriben dentro de los paréntesis. Se termina la línea con ':' y
el bloque de código se escribe con sangría. Para finalizar la
función, simplemente se deja de usar sangría y se continúa con el
flujo normal del programa.

Condicionales:
Los más comunes son 'if' y 'else', que permiten ejecutar código
según si una condición es verdadera o falsa. También existe 'elif'
(else if), que permite evaluar múltiples condiciones. Las
condiciones pueden incluir números, texto, booleanos o comparaciones
como ==, !=, >, <, etc.
"""

def condicionales(Nombre, edad):
    if edad >= 75:
        print(f"Eres de la tercera edad {Nombre}")
    elif edad >= 18:
        print(f"Eres mayor de edad {Nombre}")
    else:
        print(f"Eres menor de edad {Nombre}")

"""
Bucles:
Los bucles permiten repetir bloques de código varias veces.

Bucle 'for':
Se usa para recorrer elementos de una secuencia
(como listas, cadenas o rangos).
Ejemplo:
for i in range(5):
    print(i)  # Imprime del 0 al 4

Bucle 'while':
Se ejecuta mientras una condición sea verdadera.
Ejemplo:
contador = 0
while contador < 5:
    print(contador)
    contador += 1

Precaución:
Es importante asegurarse de que la condición del 'while' se vuelva
falsa en algún momento,de lo contrario se crea un bucle infinito.

Control de bucles:
- 'break': termina el bucle antes de que finalice normalmente.
- 'continue': salta a la siguiente iteración sin ejecutar el resto
    del código actual.
"""

def bucles():
    for i in range(10):
        print(i)


# Escribe la función esperada
print(bucles())

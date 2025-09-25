# EJERCICIO:
#  * - Crea un comentario en el código y coloca la URL del sitio web oficial del
#  *   lenguaje de programación que has seleccionado.
#  * - Representa las diferentes sintaxis que existen de crear comentarios
#  *   en el lenguaje (en una línea, varias...).
#  * - Crea una variable (y una constante si el lenguaje lo soporta).
#  * - Crea variables representando todos los tipos de datos primitivos
#  *   del lenguaje (cadenas de texto, enteros, booleanos...).
#  * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"


# https://python.org

# Comentaario de una linea 

"""
Ejemplo de un comentario
en varias 
lineas
"""

'''
Esto es otra forma de 
escribir un comentario
en Varias Lineas
'''

variable_1 = 3 # ejemplo de una variable
PI = 3.1416    # Constante por convención

# Tipos de Datos primitivos

numero = 5 # Int  Numeros Enteros (positivos,negativos o cero) 
estatura = 1.72  # Float  Numero Decimales
zeta = 2 + 3j # complex Numeros complejos 

name = 'hello' # Str string cadena de Texto
name_1 = "! Hi" # Str string otra forma de escribir cadena de textos
impar = True # Bool Booleano Valores logicos
total = None # NoneType Ausencia de Valor

print("!Hola , Python")
print(numero)
print(type(numero)) 
print(estatura)
print(type(estatura))
print(name)
print(type(name))
print(impar)
print(type(impar))

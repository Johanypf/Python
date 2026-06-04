'''
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
'''

cadena = "Hola mundo"
def invirtiendo_cadena(dato: str) -> str:

    return dato[::-1]


print(invirtiendo_cadena(cadena))
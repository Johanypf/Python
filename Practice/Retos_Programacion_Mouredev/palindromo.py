'''
/*
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 */
'''

def palindromo(dato:str)-> bool:
    
    limpio = dato.lower()

    caracteres_invalidos = " .,¿?¡!;:"

    for c in caracteres_invalidos:
        limpio = limpio.replace(c, "")
    
    return limpio == limpio[::-1]

print(palindromo('¿Qué tal Hackermen?'))
print(palindromo('Anita lava la tina'))
# Descripción del problema
# En este ejercicio deberás identificar la letra más común (o moda) en una cadena 
# recibida por parámetro. Crea una función que reciba una cadena (str) que será a
# analizada, y que retorne otra cadena (str) que contenga la letra más común en la cadena inicial.
# Para tu facilidad, las cadenas que recibirás solo contendrán letras mayúsculas
#  y no tendrán tildes o acentos. No obstante, estas pueden tener espacios, puntos
#  y comas.
# En caso de que haya 2 letras con la misma cantidad de apariciones, debes retornar 
# la que sea alfabéticamente posterior.


# Función requerida
# Tu solución debe tener una función de acuerdo con la siguiente especificación. 
# Nombre de la función: letra_ mas_comun
#                  Parámetros
# Nombre               Tipo                   Descripción
# cadena               str                   La cadena en la que se quiere saber cuál es la letra más común.
# Tipo del retorno                    Descripción del retorno
# str                                 La letra más común en la cadena que ingresa como parámetro. 
#                                     Si son dos o más, es la letra alfabéticamente posterior.


def letra_mas_comun(word:str)-> str:
    cant_words = {}
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in word:
        if i in alfabeto:
            if  i in cant_words:
                cant_words[i] += 1
            else:
                cant_words[i] = 1

    mayor =  0
    max_word = []  
    for x in cant_words:
        if cant_words[x] >= mayor:
            mayor = cant_words[x]

    for i in cant_words:
        if cant_words[i] >= mayor:
            max_word.append(i)

    max_word.sort()

        
        
    return (max_word[-1])

print(letra_mas_comun("ABCDEFGH"))

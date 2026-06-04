"""
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
"""

def re_suprime(texto):
    caracteres = [".", ",", ":", ";", "!", "¡", "?", "¿", "(", ")", "{", "}", "[", "]", "-"]
    new_string = ""
    for letter in texto:       
        if letter in caracteres:
            letter = ("")
        new_string += letter
    return new_string.lower().split(" ")

def contar_palabras(texto):
    modified_string = re_suprime(texto)
    words = {}
    for i in modified_string:
        if not i in words:
            words[i] = 1
        else:
            words[i] += 1

    return words

string = "Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev)."
print(f"Listado de Palabras:\n{chr(10).join(f'{k}: {v}' for k, v in contar_palabras(string).items())}")
# /*
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.
#  */


def Anagrama(word1:str, word2:str):
    word1 = "".join(sorted(word1.lower()))
    word2 = "".join(sorted(word2.lower()))
    if word1 == word2:
        return True
    else:
        return False
    
print(Anagrama("hola", "chao"))
    

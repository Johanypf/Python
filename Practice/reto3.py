# Escriba una función que cuente la cantidad de caracteres diferentes que aparecen más de una vez en una cadena.
# Suponga que todas las cadenas se componen únicamente de letras minúsculas del alfabeto en inglés.
# Su solución debe tener una función de acuerdo con la siguiente especificación:
# Nombre de la función: contar_caracteres_repetidos

def contar_caracteres_repetidos(cadena:str)->int:
    words = {}
    for i in cadena:
        if not i in words:
            words[i] = 1
        else:
            words[i] += 1
    rep = []
   
    for x,y in words.items():
        if y > 1:
            rep.append(x)
            
    return len(rep)
print(contar_caracteres_repetidos("manzana"))
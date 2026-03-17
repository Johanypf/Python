# La función recibirá dos parámetros: una lista y una función (func). 
# La lista contendrá un conjunto de elementos (números, objetos, cadenas, etc.),
# y la función se utilizará para realizar una acción específica en cada elemento de la lista.
# El objetivo es retornar una nueva lista con los resultados obtenidos de aplicar la función a 
# cada elemento, de manera similar a como lo haría el método map.

# Ejemplo 1:


# Input: my_map([1, 2, 3, 4], lambda num: num * 2)

# Output: [2, 4, 6, 8]

# Ejemplo 2:


# Input: my_map([
# {"name": "michi", "age": 2},
# {"name": "firulais", "age": 6}],
# lambda pet: pet["name"])

# Output: ["michi", "firulais"]

def my_map(list, func):
    resultado = []
    for valor in list:
        resultado.append(func(valor))
    return resultado



print(my_map([1, 2, 3, 4], lambda num: num * 2))
print(my_map([
{"name": "michi", "age": 2},
{"name": "firulais", "age": 6}],
lambda pet: pet["name"]))
# Reto 5: Buscar el índice de un elemento en una lista
# Escriba una función que reciba una lista y un número entero a buscar, y que retorne un entero 
# que indique el índice 
# en que se encuentra este elemento.
# En caso de que el elemento se encuentre más de una vez dentro de la lista, debe retornar
#  la primera posición en que lo encuentre.

# En caso de no encontrar el número, retorne -1.
nuemros = [3,2,4,2,5,6,7]
def  buscar_elemento(entrada:list,buscado:int)-> int:
    indice = 0
    for i in entrada:
        if i == buscado:
            indice = entrada.index(i)
            print(i)
            break
        else:
                indice = -1

    return indice
        
print(buscar_elemento(nuemros,10))
# Reto 6: Encontrar el elemento mayor
# Escriba una función que encuentre el mayor número en una lista de enteros positivos.
# En caso de que la lista esté vacía, se debe retornar-1.  
# Nombre de la función: encontrar_mayor

def encontrar_mayor(entrada:list)->int:
    mayor = 0
    if len(entrada) == 0:
        return -1
    for i in entrada:
        if i > mayor:
            mayor = i
    return mayor


nuemros = []
print(encontrar_mayor(nuemros))
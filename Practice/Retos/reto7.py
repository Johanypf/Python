# Reto 7: Aproximación de notas
# Una clase de la Universidad de los Andes tiene las siguientes reglas con
#  respecto a las aproximaciones de las notas finales.  
# Si la nota es mayor o igual a 4.5, la nota se aproxima a 5.0.
# Si la nota es mayor o igual a 3.5 y menor a 4.5, la nota se aproxima a 4.0.
# Si la nota es mayor o igual a 2.5 y menor a 3.5, la nota se aproxima a 3.0.
# De lo contrario, la nota asignada será 1.5.  
# Teniendo una lista de diccionarios en donde cada uno corresponde a un
#  estudiante y que tiene como llaves "nombre" y "nota" (sin aproximar), 
# retorne una lista con todos los diccionarios actualizados con sus notas después de aproximación.

# Cada uno de los diccionarios retornados tiene las llaves "nombre" y "nota"(aproximada).
# Se garantiza que la lista tiene al menos un diccionario.  
# Su solución debe tener una función de acuerdo con la siguiente especificación: 

# Nombre de la función: calcular_definitivas
# Si lo requiere, puede agregar funciones adicionales. 


def calcular_definitivas(estudiantes:list)->list:
    
    estudiantes_final = []
    for i in estudiantes:
        nota = i["nota"]
        if nota >= 4.5:
            i["nota"] = 5.0
        elif nota >= 3.5:
            i["nota"] = 4.0
        elif  nota >= 2.5:
            i["nota"] = 3.0
        else:
            i["nota"] = 1.5
        estudiantes_final.append(i)
    return estudiantes_final


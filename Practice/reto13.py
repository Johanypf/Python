# Reto 13: Estadísticas de las tareas
# Como parte de una iniciativa de analítica sobre el desempeño de los estudiantes para 
# identificar las dificultades que tienen en un curso, se recopilaron las notas que obtuvieron
#  en diferentes tareas. Ahora, queremos analizarlas con un pequeño programa que usted tendrá
#  que construir.


# La información obtenida está organizada en un diccionario donde las llaves son los nombres 
# de los estudiantes (cadenas de caracteres) y los valores son diccionarios.

# En estos diccionarios "internos", las llaves son los nombres de las tareas y los valores 
# son las notas obtenidas por el estudiante para esa tarea (un número entero entre 0 y 100).

# Es decir, si el único estudiante en la muestra se llama "Roberto" y ha realizado dos tareas 
# ("Tarea 1" y "Tarea 2" con notas de 80 y 90 respectivamente), el diccionario de diccionarios 
# con esta información se vería en Python de la siguiente forma: {"Roberto": {"Tarea 1": 80, "Tarea 2" : 90}}.

# Tenga cuidado: no todos los estudiantes resolvieron todas las tareas.

# Usted debe construir una función que, dados los resultados de los estudiantes, calcule las 
# siguientes estadísticas para una tarea dada su nombre: la mayor nota obtenida, el nombre del 
# estudiante que obtuvo la mejor nota, la menor nota obtenida, el nombre del estudiante que 
# obtuvo la peor nota, el promedio de las notas de los estudiantes, la cantidad de estudiantes 
# que recibieron una nota y la suma de las notas obtenidas por los estudiantes.

# La función debe retornar un diccionario con las siguientes llaves: "mayor", "mejor", "menor", 
# "peor", "promedio", "cantidad" y "total".

#  Su solución debe tener una función de acuerdo con la siguiente especificación: 

# Nombre de la función: calcular_estadisticas_tarea   

def calcular_estadisticas_tarea(estudiantes_tareas:dict, nombre_tarea: str)->dict:
    #menor_edad_valor = float('inf')
    best_nota = ''
    mayor_nota = 0
    cantidad_notas = 0 
    suma_notas = 0
    menor_nota = None
    peor_student = ''
    for i,y in estudiantes_tareas.items():
        if  nombre_tarea in y: 
            nota = y.get(nombre_tarea) 
            suma_notas += nota
            cantidad_notas += 1 
            if nota > mayor_nota:
                mayor_nota = nota
                best_nota = i
            if   menor_nota is None or nota < menor_nota:
                menor_nota = nota
                peor_student = i

    promedio = suma_notas / cantidad_notas
    dict_final = {"mayor":mayor_nota,
                   "mejor":best_nota,
                   "menor":menor_nota,
                  "peor": peor_student, 
                  "promedio": promedio, 
                  "cantidad":cantidad_notas,
                  "total": suma_notas
                  }
    
    return dict_final


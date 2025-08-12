


estudiantes = {
    "Juan" : {'tarea 1':100 #'tarea 2':90
              },
   "Ana" : {'tarea 1':90, 'tarea 2':150}
    }


def calcular_estadisticas_tarea(estudiantes_tareas:dict,nombre_tarea:str)->dict:
    
    best_student = None
    nota_mayor = 0
    menor_nota = None

    average = 0
    suma = 0 
    cantidad = 0
    valor_menor = float('inf')

    for cant in estudiantes.values():
        if nombre_tarea in cant:
            cantidad += 1
            suma += cant[nombre_tarea]
            


    for nombre, tareas in estudiantes.items():
        if nombre_tarea in tareas:
            nota = tareas[nombre_tarea]
            if nota > nota_mayor:
                nota_mayor = nota
                best_student = nombre
            if nota < valor_menor:
                valor_menor = nota
                menor_nota = nombre
                            
            
    average = suma / cantidad 

    dict_sal = {"mayor": -1,
                "mejor": -1 ,
                "menor": -1,
                "peor": -1,
                "promedio": -1,
                "cantidad":-1,
                "total":-1 
                } 

    dict_sal["mayor"] = nota_mayor
    dict_sal["mejor"] = best_student
    dict_sal["menor"] = valor_menor
    dict_sal["peor"] = menor_nota
    dict_sal["promedio"] = average
    dict_sal["cantidad"] = cantidad
    dict_sal["total"] = suma

    return dict_sal



print(calcular_estadisticas_tarea(estudiantes,"tarea 1"))



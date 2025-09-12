# Reto 12: La mejor aerolínea
# Recopilamos los registros de los vuelos que ocurrieron durante un día entre aeropuertos
#  ubicados en Estados Unidos y los organizamos en un diccionario de diccionarios. Ahora 
# queremos que usted nos ayude a averiguar cuál es la mejor aerolínea con base en la puntualidad.
#  Es decir, queremos saber cuál es la aerolínea que acumuló el menor retraso promedio en los vuelos 
# que recopilamos.

# El parámetro vuelos de la función, es un diccionario de diccionarios con la información de los vuelos.

# Las llaves en este diccionario son el código de cada vuelo.

# Los valores en este diccionario son diccionarios con la información de un vuelo organizado de
#  acuerdo con las siguientes llaves:

# aerolinea, corresponde al nombre de la aerolínea.
# origen, corresponde al código de aeropuerto de origen.
# destino, corresponde al código de aeropuerto destino del vuelo.
# distancia, corresponde a la distancia entre el origen y el destino.
# retraso, corresponde a la cantidad de minutos de retraso que tuvo el vuelo.
# duracion, corresponde a la duración planeada del vuelo en minutos.
# salida, corresponde a un entero que representa la hora de salida.
# La hora de salida, se representa usando la hora en formato 24 horas multiplicada por 100 más 
# la cantidad de minutos (por ejemplo, las 2007 indica que el vuelo salió a las 8:07 pm).  

# Su solución debe tener una función de acuerdo con la siguiente especificación: 

# Nombre de la función: mejor_aerolinea 
vuelos = {
    "AV123": {
        "aerolinea": "Avianca",
        "origen": "BOG",
        "destino": "MIA",
        "distancia": 2450,      # en km
        "retraso": 15,          # en minutos
        "duracion": 210,        # en minutos (3h30)
        "salida": 945           # 09:45 AM
    },
    "LA456": {
        "aerolinea": "LATAM",
        "origen": "SCL",
        "destino": "LIM",
        "distancia": 2450,
        "retraso": 0,
        "duracion": 180,
        "salida": 1430          # 14:30 (2:30 PM)
    },
    }


def mejor_aerolinea(vuelos:dict)->str:

    new_dict = {}
    for i, y in vuelos.items():
        aerolinea = y["aerolinea"]
        retraso = y["retraso"]

        if aerolinea not in new_dict:
            new_dict[aerolinea] = {"suma": retraso, "conteo": 1}
        else:
            new_dict[aerolinea]["suma"] += retraso
            new_dict[aerolinea]["conteo"] += 1
        

    promedios = {}
    for aerolinea, datos in new_dict.items():
        promedio = datos["suma"] / datos["conteo"] if datos["conteo"] > 0 else 0
        promedios[aerolinea] = promedio


   
    best_aerolinea = min(promedios, key=promedios.get)
    return best_aerolinea

print(mejor_aerolinea(vuelos))
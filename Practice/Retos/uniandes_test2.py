# Descripción del problema

# Recopilamos los registros de los vuelos que ocurrieron durante un día
#  entre aeropuertos ubicados en Estados Unidos y los organizamos en un
#  diccionario de diccionarios. Ahora queremos que nos ayudes a identificar
#  si hay aeropuertos a los cuales hayan llegado vuelos durante ese día, pero 
# no hayan salido vuelos.

            # El parámetro vuelos de la función es un diccionario de diccionarios con la 
            # información de los vuelos.

            # Las llaves en este diccionario son el código de cada vuelo.

            # Los valores en este diccionario son diccionarios con la información de un 
            # vuelo, organizado de acuerdo con las siguientes llaves:

            # aerolínea, que corresponde al nombre de la aerolínea
            # origen, que corresponde al código de aeropuerto de origen
            # destino, que corresponde al aeropuerto destino del vuelo
            # distancia, que corresponde a la distancia entre el origen y el destino
            # retraso, que corresponde a la cantidad de minutos de retraso que tuvo el vuelo
            # duracion, que corresponde a la duración planeada del vuelo en minutos
            # salida, que corresponde a un entero que representa la hora de salida.
            # La hora de salida se representa usando la hora en formato 24 horas multiplicada
            #  por 100 más la cantidad de minutos (por ejemplo, las 2007 indica que el vuelo salió a las 8:07 pm).

# Nombre de la función: listar_aeropuertos_sin_salida
# Parámetros
# Nombre.  Tipo.    Descripción
# vuelos dict       Es un diccionario de diccionarios con la información de los vuelos.
# Tipo del retorno
# Descripción del retorno
# list Una lista de cadenas de caracteres que tiene los códigos de los aeropuertos de los cuales no salieron  vuelos.
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
    "UA789": {
        "aerolinea": "United",
        "origen": "MIA",
        "destino": "JFK",
        "distancia": 1750,
        "retraso": 45,
        "duracion": 180,
        "salida": 2007          # 20:07 (8:07 PM)
    },
    "IB101": {
        "aerolinea": "Iberia",
        "origen": "MAD",
        "destino": "BOG",
        "distancia": 8030,
        "retraso": 10,
        "duracion": 600,        # 10 horas
        "salida": 2330          # 23:30 (11:30 PM)
    }
}
def listar_aeropuertos_sin_salida(vuelos:dict)->list:

    llegada = set()
    salida = set()
   
    for externo,interno in vuelos.items():
        llegada.add(interno['destino'])
        salida.add(interno['origen'])

    no_salida = llegada - salida

    
    return list(no_salida)

print(listar_aeropuertos_sin_salida(vuelos))
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
    "AV223": {
        "aerolinea": "Avianca",
        "origen": "BOG",
        "destino": "MIA",
        "distancia": 2450,      # en km
        "retraso": 15,          # en minutos
        "duracion": 210,        # en minutos (3h30)
        "salida": 945           # 09:45 AM
    },
     "LA556": {
        "aerolinea": "LATAM",
        "origen": "SCL",
        "destino": "LIM",
        "distancia": 2450,
        "retraso": 0,
        "duracion": 180,
        "salida": 1430          # 14:30 (2:30 PM)
    }

    }

for i in vuelos.values():
    print(i)

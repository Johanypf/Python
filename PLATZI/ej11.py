def listar_aeropuertos_sin_salida(vuelos):
    
    aeropuertos_origen = set()
    aeropuertos_destino = set()

    
    for vuelo in vuelos.values():
        aeropuertos_origen.add(vuelo['origen'])
        aeropuertos_destino.add(vuelo['destino'])

    
    aeropuertos_sin_salida = aeropuertos_destino - aeropuertos_origen

    
    return list(aeropuertos_sin_salida)
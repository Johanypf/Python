
def calcular_costo_boletas (cantidad_boletas:int, tipo_sala: str,  hora_pico: bool, pago_tarjeta_cinema:bool, reserva:bool)-> int:
    
    tarifas_base = {
        "Dinamix": 18800,
        "3D": 15500,
        "2D": 11300
    }

    tarifa_base = tarifas_base[tipo_sala]
    descuento_total_por_boleta = 0
    recargo_total_por_boleta = 0

    

    # ---- 1) Descuentos por hora no pico ----
       
    if  not hora_pico:
        descuento_total_por_boleta += tarifa_base * 0.10
        if cantidad_boletas >=3:
          descuento_total_por_boleta += 500

    # ----- 2) pago es la tarjeta del cinema ----    
    if pago_tarjeta_cinema :
       descuento_total_por_boleta += tarifas_base[tipo_sala] * 0.05
    
    # ---- 3)  una reserva, se tiene un recargo de $2000 ----

    if reserva:
        recargo_total_por_boleta += 2000
    else:
        recargo_total_por_boleta += 0

    #---- Ajustar tarifa por hora pico -----
    if hora_pico:
        if tipo_sala == "Dinamix":
            tarifa_base = tarifa_base * 1.5
        else:
            tarifa_base = tarifa_base * 1.25

    
    precio_por_boleta = tarifa_base-descuento_total_por_boleta + recargo_total_por_boleta
    precio_por_boleta = round(precio_por_boleta )
    
    total = cantidad_boletas * precio_por_boleta
    return total



     
print(calcular_costo_boletas(1,"2D",False,True,True))


# Caso 1
# Su programa falló cuando se usaron estas entradas: 
# cantidad_boletas = 1
# tipo_sala = 2D
# hora_pico = False
# pago_tarjeta_cinema = True
# reserva = True
# Su programa respondió: 9605 -11605
#20 de noviembre de 1986, y la fecha actual fuese el 16 de octubre de 1987, la función retornaría que la edad de Julieta es “0,10,26”



def calcular_edad(dia_nacio: int,mes_nacio: int, anio_nacio: int,dia_actual: int,mes_actual: int, anio_actual:int)-> str:
    
    anios = anio_actual - anio_nacio
    meses = mes_actual - mes_nacio
    dias = dia_actual - dia_nacio

    # Ajustar si los días son negativos
    if dias < 0:
        dias += 30
        meses -= 1

    # Ajustar si los meses son negativos
    if meses < 0:
        meses += 12
        anios -= 1
    
    
    return  (f"{anios},{meses},{dias}")


print(calcular_edad(1,12,1987,3,12,1987))

def calcular_edad(anio_nac, mes_nac, dia_nac, anio_act, mes_act, dia_act):
    # Convertimos todas las fechas a días, suponiendo que todos los meses tienen 30 días y todos los años 12 meses.
    total_dias_nac = anio_nac * 360 + mes_nac * 30 + dia_nac
    total_dias_act = anio_act * 360 + mes_act * 30 + dia_act

    # Calculamos la diferencia en días totales
    diferencia_dias = total_dias_act - total_dias_nac

    # Convertimos de nuevo a años, meses y días
    anios = diferencia_dias // 360
    print(anios)
    diferencia_dias %= 360
    print(diferencia_dias)
    meses = diferencia_dias // 30
    dias = diferencia_dias % 30

    return f"{anios},{meses},{dias}"



print(calcular_edad(1,12,1987,3,12,1987))
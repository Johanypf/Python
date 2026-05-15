# /*
#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  */



def area_poligono(base,altura,poligono):
    if poligono.lower() == "triangulo":
        print(f"El area del Triángulo es: {base * altura / 2 } m\u00B2 ")
    elif poligono.lower() == "cuadrado":
        print(f"El area del Cuadrado es: {base * altura } m\u00B2 ")
    elif poligono.lower() == "rectangulo":
        print(f"El area del Rectángulo es: {base * altura } m\u00B2 ")
    else:
        raise ValueError("Polígono Incorrecto")
    
area_poligono(5,5,"Triangulo")


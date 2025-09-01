# Escriba una función que determine si en dos números enteros aparecen los mismos dígitos. 
# No tenga en cuenta ni la frecuencia ni el orden de aparición de los dígitos en los números.

# Los números no tienen necesariamente la misma cantidad de dígitos. Por ejemplo, si los números
#  son 998 y 89 la función debería retornar True.

   

# Su solución debe tener una función de acuerdo con la siguiente especificación:

# Nombre de la función: mismos_digitos
# Si lo requiere, puede agregar funciones adicionales.

def mismos_digitos(a:int,b:int)->bool:

    num_1 = set(str(a))
    num_str = set(str(b))
    

    if num_1 == num_str:
        return True
    else:
        return False


    
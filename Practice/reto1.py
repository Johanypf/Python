# Reto 1: Calcular sucesión de Fibonacci
# En matemáticas, la sucesión o serie de Fibonacci es la siguiente sucesión 
# infinita de números naturales: 0,1,1,2,3,5,8,13,...

#  La sucesión comienza con los números 0 y 1, y a partir de estos, 
# cada término es la suma de los dos anteriores.

# Cree una función que reciba un número que indica la cantidad de números de 
# la sucesión que se quieren encontrar y retorne una cadena con los números separados por coma.

# Por ejemplo, el resultado de la función, si se pasa como parámetro el número
#  18 es el siguiente:

# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597
# Su solución debe tener una función de acuerdo con la siguiente especificación:
# Nombre de la función: sucesion_fibonacci
# Si lo requiere, puede agregar funciones adicionales. 
#  Descripción de parámetros:
# Nombre
# Tipo
# Descripción
# cantidad_numeros
# int
# Cantidad de números de la sucesión que se quieren encontrar.
# Descripción del retorno:
# Tipo
# Descripción
# str
# Cadena que contiene los números de la sucesión de Fibonacci hasta la cantidad que indica 
# el parámetro, separados por coma y sin espacios intermedios.


def sucesion_fibonacci(cantidad_numeros:int)->str:

    data = cantidad_numeros
    data_final = []
    a = 0
    b = 1 
    if data == 1:
        data_final.append(a)
    elif data == 2:
        data_final.append(a)
        data_final.append(b)
    else:
        data_final = [0,1]
        i=3
        while i <= data:
            num = a + b
            a=b
            b=num
            data_final.append(num)
            i+=1

    
    result_string = ",".join(map(str, data_final))
    
    return result_string


print(sucesion_fibonacci(3))

# Reto 15: La fila juiciosa
# Andrés es un profesor que tiene la teoría de que hay filas del salón que tienen mejor promedio
#  que otras.

# Para comprobarlo, ha decidido crear una función que calcule el promedio de la nota de una fila.
#  La función recibe como parámetros una matriz, un número de fila y retorna el promedio de la fila
#  redondeado a dos decimales.

# Cuidado: un 0 en la matriz no significa que el estudiante haya sacado 0, sino que no hay ningún
#  estudiante en dicha silla.

# Tenga muy en cuenta que para Andrés la primera fila es la número 1. Si se pide un número de fila
#  que no tenga sentido, su función debe retornar -1. Si la fila no tiene estudiantes, su función
#  debe retornar 0.  

# Su solución debe tener una función de acuerdo con la siguiente especificación:

# Nombre de la función: promedio_fila

# Descripción de parámetros:
# matriz -  list - Matriz que representa el salón de clases.
# fila   -   int  -  Fila a la cual se le va a calcular el promedio.

# Descripción de retorno:

# float -Promedio de la fila que el profesor solicitó. 



def promedio_fila(matriz:list,fila:int)->float:
    students = 0
    nota_total = 0

    if   0 < fila <= len(matriz):
        for i in range(len(matriz)):
            if fila == (i+1):
                for  c in matriz[i]:
                    if c > 0:
                        nota_total += c
                        students += 1
        
        if nota_total > 0 :
            return round(nota_total/students,2)
        else:
            return 0
            
    else:
        return(-1)


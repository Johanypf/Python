# Reto 1: Sumar dos vectores (3d)
# Construya una función que reciba dos vectores (con 3 componentes cada uno) y 
# retorne un nuevo vector que sea la suma de los dos vectores recibidos. Cada vector
#  debe recibirse como una tupla con tres valores flotantes.

# Su solución debe tener una función de acuerdo con la siguiente especificación:

# Nombre de la función: suma_vectorial    
# suma_vectorial 

def suma_vectorial(vector_1:tuple,vector_2:tuple)->tuple:
   
        total = []
        for i in range(3):
            x = vector_1[i]
            y = vector_2[i]
            total.append(vector_1[i]+ vector_2[i])

        total_tupla = tuple(total)

        return(total_tupla)
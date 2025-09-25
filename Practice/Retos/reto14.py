# Reto 14: La vaca de cumpleaños
# Una clase de estudiantes ejemplares ha decidido hacer una vaca para el cumpleaños 
# de su profesor favorito. Para esto, un estudiante recorrerá todo el salón recogiendo 
# el dinero que cada estudiante va a aportar. Tienen dos opciones de regalo: una 
# botella de licor que cuesta 120.000 o un pastel que cuesta 35.000. Además, el 
# estudiante que más dinero ponga, será el que tenga el honor de darle el regalo al profesor. 
# Recree este caso en una función que reciba una matriz que representa al salón y una cadena
#  que indica el regalo. Debe retornar una lista cuya primera posición es un mensaje que indica
#  si el dinero alcanzó para la vaca y las siguientes dos posiciones son las coordenadas del
#  puesto del estudiante que más aportó.  

# Su solución debe tener una función de acuerdo con la siguiente especificación: 

# Nombre de la función: hacer_la_vaca 
#Descripción de parámetros:
# salon - list-  Matriz que representa el salón de estudiantes, los valores son enteros que representan cuánto dinero aportarán.
#vaca    -str -  Cadena que indica qué vaca se está realizando, esta puede ser 'botella' o 'pastel .

# Descripción de retorno:
#list
# Lista cuya primera posición es un str de la forma 'Hay Vaca' si se alcanzó la vaca, y 'No Alcanza' de lo contrario. 
# Las siguientes dos posiciones, son las coordenadas del estudiante qué más dinero aportó.  

def hacer_la_vaca(salon:list,vaca:str)->list:

    total = 0
    mayor= 0
    pos_fila = 0
    pos_col = 0
    detalles = {'botella':120000 ,'pastel': 35000}
    
    for fila in range(len(salon)):
         for col in range(len(salon[fila])):
              aporte = salon[fila][col]
              total += aporte


              if aporte > mayor:
                   mayor = aporte
                   pos_fila = fila
                   pos_col = col 

    if total >= detalles[vaca]:
         mensaje = "Hay Vaca"
    else:
        mensaje = "No Alcanza"

    return [mensaje,pos_fila,pos_col]
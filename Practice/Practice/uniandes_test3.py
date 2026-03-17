# Estadísticas de descargas

# Descripción del problema

# Una plataforma web que vende y distribuye modelos tridimensionales  para 
# su uso en proyectos de arquitectura tiene información sobre cada venta  
# que han tenido los modelos publicados. A partir de esa información, ellos
#  quieren que tú los ayudes a calcular estadísticas  sobre cada modelo.

# Tu tarea será construir la función calcular_estadisticas que recibe 
# un DataFrame con la información de las descargas y retorna un DataFrame 
# con las estadísticas.

# El DataFrame de entrada tendrá una fila con la información de cada 
# descarga: el nombre del modelo descargado, el nombre del usuario que la 
# descargó, el dinero en dólares que pagó por el modelo (número decimal), 
# la cantidad de estrellas (entre 1 y 5) que el usuario le dio al modelo 
# (número decimal) y si dejó o no un comentario sobre el modelo después de
#  haberlo descargado (valor booleano). El precio de un modelo particular 
# podría ser diferente entre descargas porque la plataforma suele hacer 
# promociones y porque los artistas que los crean pueden modificar el 
# precio cuando ellos quieran. El precio podría ser 0 en algunas 
# descargas, pero esos registros no se deberá tener en cuenta.

# El siguiente es un ejemplo de un DataFrame que muestra los nombres de
# las columnas y posibles valores que puede haber en el DataFrame

# El DataFrame que retorna la función tiene que tener una fila por cada
#  modelo. El DataFrame tendrá 7 columnas: CANTIDAD, que tendrá un número 
# entero con la cantidad de descargas que haya tenido el modelo; PROMEDIO,
#  que tendrá un número decimal con la cantidad promedio que se pagó por 
# el modelo; MAXIMO que tendrá un número decimal con la cantidad máxima 
# que se pagó por el modelo; MINIMO que tendrá un número decimal con la 
# cantidad mínima que se pagó por el modelo; ESTRELLAS, que tendrá un 
# número decimal con la cantidad promedio de estrellas que se le dio al 
# modelo; DESV. ESTRELLAS, que tendrá un número decimal con la desviación 
# estándar de la cantidad de estrellas que se le hayan dado al modelo; y 
# COMENTARIOS, que tendrá un número entero con la cantidad de comentarios 
# que hayan dejado los compradores.

# Notas importantes sobre el DataFrame resultado:

# El índice del DataFrame tendrá los nombres de los modelos y sólo 
# deben aparecer aquellos para los que al menos un usuario haya pagado. Es
#  decir que no deben aparecer los modelos que hayan sido siempre 
# gratuitos.
# Los modelos deben aparecer en orden alfabético de acuerdo a su nombre.
# Todos los números que no sean enteros deben aparecer redondeados a dos cifras decimales.
# Como la desviación estándar no se puede calcular cuando haya
# sólo un dato, en lugar de NaN debe aparecer 0.0 en el resultado.
import pandas as pd
df = pd.DataFrame([['Bus urbano #27', 'Ted Mosby', 24.99, 5, True],
                   ['Silla tipo bar', 'Art Vandelay', 4.99, 3.5, False],
                   ['Piano', 'Art Vandelay', 4.99, 3.5, False],
                   ['Fuente con flores', 'Michael', 0, 5, True],
                   ['Bus urbano #27', 'Mark Brendanawicz', 12, 4, True],
                   ['Puesto de Yogurt', 'Michael', 0, 5, True],
                   ['Playground', 'Mark Brendanawicz', 14, 4.5, True],
                   ['Bus urbano #27', 'LeCorbusier_2020', 0, 1, True]],
                   columns=['MODELO', 'USUARIO', 'PAGO', 
                            'ESTRELLAS', 'COMENTARIO'])




import pandas as pd
def calcular_estadisticas(descargas:pd.DataFrame)-> pd.DataFrame:

    new_data = descargas[descargas["PAGO"]>0]
    
    new_df = pd.DataFrame()
   
    new_df["CANTIDAD"] = new_data["MODELO"].value_counts()  
    new_df["PROMEDIO"] = (new_data.groupby("MODELO")['PAGO'].sum()) / new_df["CANTIDAD"]
    new_df["MAXIMO"] = new_data.groupby("MODELO")['PAGO'].max()
    new_df["MINIMO"] = new_data.groupby("MODELO")['PAGO'].min()
    new_df["ESTRELLAS"] = new_data.groupby("MODELO")['ESTRELLAS'].sum()/ new_df["CANTIDAD"]
    new_df["DESV. ESTRELLAS"] = new_data.groupby("MODELO")['ESTRELLAS'].std().fillna(0)
    new_df["COMENTARIOS"] = new_data.groupby("MODELO")['COMENTARIO'].sum()
    new_df = new_df.sort_index()
    new_df = new_df.round(2)
    
    return new_df


print(calcular_estadisticas(df))


# El algoritmo ha fallado antes de tiempo: 'MODELO'
#Ejercicio 1: Decorador de medir tiempo

# Crea un decorador @medir_tiempo que:
# Mida cuánto tarda una función en ejecutarse
# Imprima: "⏱️ [nombre_funcion] tardó X.XXXX segundos"
# Retorne el resultado original
# Use functools.wraps


import time
from functools import wraps


def medir_tiempo(func):
    @wraps(func)
    def envoltura(*args,**kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    
    return envoltura

@medir_tiempo
def tarea_lenta():
    time.sleep(2)
    return "Tarea completada"

resultado = tarea_lenta()
print(f"Resultado: {resultado}")


#Ejercicio 2: Decorador de validación

# Crea un decorador @solo_mayusculas que:

# Valide que el primer argumento sea string
# Lo convierta a mayúsculas
# Lo pase a la función

from functools import wraps

def solo_mayusculas(func):
    @wraps(func)
    def envoltura(*args,**kwargs):
        for arg in args:
            if not isinstance(arg, (str)):
                raise TypeError(f"Se esperaba String, recibí {type(arg).__name__}")
        return func(*args, **kwargs)

    return envoltura

@solo_mayusculas
def saludar(nombre):
    return f"Hola {nombre.upper()}"

print(saludar("ana"))


@solo_mayusculas
def presentarse(nombre, apellido):
    return f"Me llamo {nombre.upper()} {apellido.upper()}"

print(presentarse("carlos", "moreno")) 



# Ejercicio 3: Decorador con parámetro

# Crea un decorador @repetir(n) que:

# Acepte un parámetro n (número de repeticiones)
# Ejecute la función N veces
# Imprima el número de iteración antes de ejecutar



def repetir(n):
    def decorador(func):
        @wraps(func)
        def envoltura(*args,**kwargs):
            for i in range(n):
                print(f"[Iteración {i+1}]")
                resultado = func(*args, **kwargs)
            
            return resultado

        return envoltura
    return decorador

@repetir(n=3)
def imprimir(mensaje):
    print(f"  {mensaje}")

@repetir(n=2)
def saludar(nombre):
    print(f"  Hola {nombre}")

print("=== Test 1 ===")
imprimir("¡Python es genial!")

print("\n=== Test 2 ===")
saludar("Ana")

import time
from functools import wraps

def medir_tiempo(func):
    @wraps(func)
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"⏱️  {func.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return envoltura

@medir_tiempo
def tarea_rapida():
    return "Hecho"

@medir_tiempo
def tarea_lenta():
    time.sleep(2)
    return "Completado"

tarea = tarea_rapida() 
print(tarea)
tarea_lenta()   

from functools import wraps


def retry(veces):  # ← Decorador que recibe parámetro
    def decorador(func):  # ← El verdadero decorador
        @wraps(func)
        def envoltura(*args, **kwargs):
            excepcion = None
            for i in range(veces):
                try:
                    resultado = func(*args, **kwargs)
                    return resultado
                     
                except ValueError as e: 
                    excepcion = e
                    print(f"Intento {i+1} falló. Reintentando...")
            raise excepcion
                
                
        return envoltura
    return decorador




@retry(veces=3)
def operacion_inestable(numero):
    if numero < 5:
        raise ValueError("Número muy pequeño")
    return f"Operación exitosa con {numero}"


try:
    print(operacion_inestable(10))  # ✅ Funciona
    print(operacion_inestable(2))   # ❌ Lanza excepción
except ValueError as e:
    print(f"Error capturado: {e}")
from functools import wraps

def logger(func):
    @wraps(func)
    def envoltura(*args, **kwargs):
        print(f"📝 Llamando: {func.__name__}")
        print(f"   Args: {args}")
        print(f"   Kwargs: {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"   Resultado: {resultado}")
        return resultado
    return envoltura

@logger
def sumar(a, b):
    return a + b

sumar(5, 3)
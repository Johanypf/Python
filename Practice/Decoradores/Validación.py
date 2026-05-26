from functools import wraps

def validar_numeros(func):
    @wraps(func)
    def envoltura(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Se esperaba número, recibí {type(arg).__name__}")
        return func(*args, **kwargs)
    return envoltura

@validar_numeros
def dividir(a, b):
    if b == 0:
        raise ValueError("No puedes dividir por 0")
    return a / b

print(dividir(10, 2))      
print(dividir(10, "dos"))   
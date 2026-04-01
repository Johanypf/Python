from functools import wraps

def mi_decorador(func):
    @wraps(func)  # ← Preserva metadata
    def envoltura(*args, **kwargs):
        return func(*args, **kwargs)
    return envoltura

@mi_decorador
def mi_funcion():
    """Esta es mi función"""
    pass

print(mi_funcion.__name__) 
print(mi_funcion.__doc__)  

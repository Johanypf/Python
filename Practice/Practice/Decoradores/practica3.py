
from functools import wraps 

def validar_tipos(parametros):

    def decorador(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            
            for parametro,tipo_esperado in parametros.items():
                if parametro in kwargs:
                        valor = kwargs[parametro]

                        if not isinstance(valor,tipo_esperado):
                            raise TypeError(f"{parametro} debe ser {tipo_esperado}")
            
            return func(*args,**kwargs)
        return wrapper
    return decorador

        
    
@validar_tipos({"a": int, "b": str})
def ejemplo(a, b):
    return f"{a} - {b}"

print(ejemplo(a=5, b="hola"))     
print(ejemplo(a="cinco", b="hola")) 
print(ejemplo(a=5, b=123)) 

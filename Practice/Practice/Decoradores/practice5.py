



def estado(func):
    def envoltura(*args, **kwargs):
        print(f"Antes de funcion")
        print(func(*args, **kwargs))
        print(f"Despues de suma")
        
    return envoltura
    

    


@estado
def suma(a,b):
    return a + b

suma(2,3)
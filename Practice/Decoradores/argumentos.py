def mi_decorador(func):
    def envoltura(*args, **kwargs):  # ← Acepta cualquier argumento
        print("ANTES")
        resultado = func(*args, **kwargs)  # ← Los pasa a func
        print("DESPUÉS")
        return resultado
    return envoltura

@mi_decorador
def saludar(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años")
    return f"Saludé a {nombre}"

resultado = saludar("Ana", 24)


from functools import wraps

def repetir(veces):  # ← Decorador que recibe parámetro
    def decorador(func):  # ← El verdadero decorador
        @wraps(func)
        def envoltura(*args, **kwargs):
            for i in range(veces):
                print(f"[Iteración {i+1}]")
                resultado = func(*args, **kwargs)
            return resultado
        return envoltura
    return decorador

@repetir(veces=3)  # ← Pasas el parámetro aquí
def saludar(nombre):
    print(f"  Hola {nombre}")

saludar("Ana")

# Con decorador
import time

def verificar_acceso(func):
    def envoltura():
        print("🔐 Verificando permisos...")
        print("✅ Acceso concedido")
        func()
        print("🔒 Cerrando sesión")
    return envoltura

@verificar_acceso
def saludo_admin():
    print("Bienvenido Admin")

@verificar_acceso
def saludo_usuario():
    print("Bienvenido Usuario")

saludo_admin()


print(f" {"#" * 15 } ")
print("\n")



def medir_tiempo(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return envoltura

@medir_tiempo
def calcular_factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


print(f"Con  decorador")
calcular_factorial(10)



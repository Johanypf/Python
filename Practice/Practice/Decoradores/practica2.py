from functools import wraps

def requiere_autenticacion(func):
    @wraps(func)
    def envoltura(*args, **kwargs):
        print("🔐 Verificando permisos...")
        
        usuario = kwargs.get("usuario")  # Accedes a kwargs
        
        if usuario == "admin":
            resultado = func(*args, **kwargs)
            print("✅ Acceso concedido")
            print("🔒 Cerrando sesión")
            return resultado
        else:
            raise PermissionError("❌ Acceso denegado. Solo admins.")
    
    return envoltura

@requiere_autenticacion
def funcion(usuario):
    print("Bienvenido Admin")

funcion(usuario="admin")




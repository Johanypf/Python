class Empleado:
    def trabajar(self):
        print("El empleado está realizando una tarea genérica.")

class Programador(Empleado):
    def trabajar(self):
        # Sobrescribimos el método del padre
        print("El programador está escribiendo código en Python.")

class Gerente(Empleado):
    def trabajar(self):
        # Sobrescribimos el método del padre
        print("El gerente está supervisando al equipo.")

emp = Empleado()
emp.trabajar()
pro = Programador()
pro.trabajar()
ger = Gerente()
ger.trabajar()
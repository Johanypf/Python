
class Empleado():
    def __init__(self,salario):
        self.__salario = salario

    def obtener_salario(self):
        return self.__salario

    def realizar_tarea(self):
        print(f"Empleado cumpliendo Horario.")

class Gerente(Empleado):
    
    def realizar_tarea(self):
        print(f"Gerente supervisando el departamento.")


class Programdor(Empleado):

    def realizar_tarea(self):
        print(f"Programador escribiendo código.")
    
empleados_del_mes = [ Gerente(1455),Programdor(45222)]

for empleado in empleados_del_mes:
    empleado.realizar_tarea()
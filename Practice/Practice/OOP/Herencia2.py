#Clase Padre
class Empleado:
    def __init__(self,nombre,salario):
        self.nombre = nombre
        self.__salario = salario 
       

    def obtener_salario(self):
        return self.__salario
    
    def modificar_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
            print(f" Salario actualizado a: {self.__salario} ")
        else:
            print("Error : El salario debe ser un monto positivo")

class Gerente(Empleado):

    def __init__(self, nombre, salario,departamento):
        super().__init__( nombre, salario)
        self.departamento = departamento

    def presentarse(self):
        pago = self.obtener_salario()
        print (f" Soy {self.nombre}, gerente del departamento de {self.departamento} y gano {pago} ")

emp1 = Empleado("Juan",150)
#emp1.obtener_salario()
emp2 = Gerente("Marco",34522,"Dev")
emp2.presentarse()


class Programador(Empleado):
    def __init__(self, nombre, salario,lenguaje_favorito):
        super().__init__(nombre, salario)
        self.lenguaje_favorito = lenguaje_favorito

    def programar(self):
        salario = self.obtener_salario()
        print(f"Estoy codeando en {self.lenguaje_favorito} y gano {salario}")


junior = Programador("Pedro",34500,"Python")
junior.programar()

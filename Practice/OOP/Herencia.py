#Clase Padre
class Vehiculo():
    def __init__(self,marca):
        self.marca = marca

    def arrancar(self):
        print(f"el {self.marca} está encendido.")

#Clase Hija
class Moto(Vehiculo):
    def hacer_mot(self):
        print(f"la moto {self.marca} está haciendo una vuelta!")

mi_moto = Moto("Yamaha")
mi_moto.arrancar()
mi_moto.hacer_mot()
    


class Dispositivo:
    def __init__(self, marca):
        self.__marca = marca # Privado

    def get_marca(self):
        return self.__marca



class Celular(Dispositivo):
    def __init__(self, marca, modelo):
        # Llamamos al constructor del padre para que guarde la marca
        super().__init__(marca) 
        self.modelo = modelo

    def info(self):
        # Usamos el getter del padre porque la marca es PRIVADA
        print(f"Celular: {self.get_marca()} {self.modelo}")

mi_cel = Celular("Apple", "iPhone 15")
print(mi_cel.modelo)
mi_cel.info()

class Termometro:
    def __init__(self,temperatura):
        self.__temperatura = temperatura

    def obtener_temperatura(self):
        return self.__temperatura

    def asignar_temperatura(self,nueva_temp):
        if nueva_temp <  -273.15:
            print(f"Temperatura Incorrecta")
        else:
            self.__temperatura = nueva_temp
            print(f"Nueva temperatura {self.__temperatura}")

termo = Termometro(-500)
termo.asignar_temperatura(37)
termo.obtener_temperatura()


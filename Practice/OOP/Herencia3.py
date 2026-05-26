

class Consola:
    def __init__(self,encendida = False):
        self.__encendida = encendida
    
    def conectar_corriente(self):
        self.__encendida = True
        print(f"Energia recibida")
    
    def esta_lista(self):
        return self.__encendida
        # if self.__encendida:
        #     return (f"Consola Encendia")
        # else:
        #     return (f"Consola Apagada")


class Playstation(Consola):
    def __init__(self, encendida=False):
        super().__init__(encendida)

        self.juego = None

    def jugar(self,juego):
        self.juego = juego
        self.conectar_corriente()
        if self.esta_lista():
            print(f'Jugando a {self.juego}.')

play = Consola()
print(play.esta_lista())
play.conectar_corriente()
print(play.esta_lista())

play2 = Playstation()
play2.jugar("Cars")

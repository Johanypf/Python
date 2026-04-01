
class Personaje:
    def __init__(self,nombre,vida,fuerza):
        self.nombre = nombre
        self.__vida = vida
        self.fuerza = fuerza

    def recibir_daño(self,cantidad):
        self.__vida -= cantidad
        if self.__vida < 0:
            self.__vida = 0
    
    def esta_vivo(self):
          if self.__vida > 0 :
            return True
    
    def atacar(self,objetivo):
        objetivo.recibir_daño(self.fuerza)
    
    def cantidad_vida(self):
        return self.__vida


class Guerrero(Personaje):

    def __init__(self, nombre, vida, fuerza):
        super().__init__(nombre, vida, fuerza)

    def atacar(self, objetivo): 
         return objetivo.recibir_daño(self.fuerza * 2)


class Mago(Personaje):

    def __init__(self, nombre, vida, fuerza):
        super().__init__(nombre, vida, fuerza)

    def atacar(self, objetivo):
        return objetivo.recibir_daño(self.fuerza)







ragnar = Guerrero("Ragnar", 100, 10)
merlin = Mago("Merlin", 50, 15)

# Aquí le pasas el objeto 'merlin' como argumento
ragnar.atacar(merlin)
print(merlin.cantidad_vida())
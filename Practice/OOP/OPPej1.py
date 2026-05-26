

class Animal:
    def __init__(self,nombre,edad,especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.info = {}

    def hacer_sonido(self):
        return ("Hace un sonido ")
    
    def mostrar_info(self):
        self.info = {"Nombre":self.nombre, "Edad": self.edad , "Especie": self.especie}
        return self.info


class Leon(Animal):
    def __init__(self,nombre,edad,especie,melena):
        super().__init__(nombre,edad,especie)
        self.melena = melena


    def hacer_sonido(self):
        return "El sonido es: ¡Rugido!"
    
    def mostrar_info(self):
        new_info =  super().mostrar_info()
        new_info['melena'] = self.melena
        return new_info


class Elefante(Animal):
    def __init__(self,nombre,edad,especie,tamaño_colmillos):
        super().__init__(nombre,edad,especie)
        self.tamaño_colmillos = tamaño_colmillos


    def hacer_sonido(self):
        return "El sonido es: ¡Barrito!"
    
    def mostrar_info(self):
        new_info =  super().mostrar_info()
        new_info['tamaño_colmillos'] = self.tamaño_colmillos
        return new_info

class Mono(Animal):
    def __init__(self,nombre,edad,especie,puede_columpiarse):
        super().__init__(nombre,edad,especie)
        self.puede_columpiarse = puede_columpiarse


    def hacer_sonido(self):
        return "El sonido es: ¡Chilla!"
    
    def mostrar_info(self):
        new_info =  super().mostrar_info()
        new_info['puede_columpiarse'] = self.puede_columpiarse
        return new_info


class Zoologico:
    def __init__(self):
        self.lista_animales = []


    def agregar_animal(self,animal):
        self.lista_animales.append(animal)

    
    def mostrar_todos(self):
        for i in self.lista_animales:
            print(i.mostrar_info())
    
    def hacer_sonido(self):
        for animal in self.lista_animales:
            print(f"{animal.nombre} :  {animal.hacer_sonido()}")



zoo = Zoologico()

simba = Leon("Simba", 5, "Felino", "larga")
dumbo = Elefante("Dumbo", 10, "Mamífero", "grandes")
george = Mono("George", 3, "Primate", True)

zoo.agregar_animal(simba)
zoo.agregar_animal(dumbo)
zoo.agregar_animal(george)

print("🦁 Información de todos los animales:")
zoo.mostrar_todos()

print("\n🔊 Sonidos de todos los animales:")
zoo.hacer_sonido()
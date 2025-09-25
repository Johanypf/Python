# La clase Animal que define un método hablar()
class Animal:
    def hablar(self):
        print('Sonidos de animal')

# Perro que hereda de la clase Animal y sobrescribe el método hablar()
# con una implementación específica
class Perro(Animal):
    def hablar(self):
        print('Guau guau!')

# Gato que hereda de la clase Animal y sobrescribe el método hablar()
# con otra implementación
class Gato(Animal):
    def hablar(self):
        print('Miau miau!')

# Ahora podemos crear objetos de las tres clases
# y llamar al método hablar(), que proporcionará
# una salida diferente para cada uno de ellos

animal = Animal()
perro = Perro()
gato = Gato()

animal.hablar()  # Sonidos de animal
perro.hablar()  # Guau guau!
gato.hablar()   # Miau miau!

from operator import mul
from tkinter import E


class Libro:
    total_libros = 0

    def __init__(self,titulo,autor,num_paginas):
        self.titulo = titulo
        self.autor  = autor
        self.__num_paginas = num_paginas
        Libro.total_libros += 1
    
    def describir(self):
        print(f"El libro '{self.titulo}' fue escrito por {self.autor} y tiene {self.num_paginas} páginas")

    def cambiar_autor(self, nuevo_autor):
        self.autor = nuevo_autor
    
    def set_paginas(self,nuevas_paginas):
        if nuevas_paginas > 0 :
            self.__num_paginas = nuevas_paginas
        else:
            print("Error: El número de páginas debe ser positivo.")

        
book1 = Libro("Cien años de soledad","Gabriel García Márquez",432)
book1.describir()

book2 = Libro("ALKELARRE","Mario Mendoza",32)
book2.describir()

book2.cambiar_autor("Mario Men")
book2.describir()


print(Libro.total_libros)



class Estudiante:
    total_estudiantes = 0

    def __init__(self,nombre,edad,carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        Estudiante.total_estudiantes += 1
    
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} años y estudio {self.carrera}.")
    
    def cambiar_carrera(self,nueva_carrera):
        self.carrera = nueva_carrera

Estudiante1 = Estudiante("Pedro",26,"Electronica")
Estudiante1.presentarse()
Estudiante2 = Estudiante("Maria",34,"Medicina")
Estudiante2.presentarse()
Estudiante3 = Estudiante("Sandra",24,"Salud")
Estudiante3.presentarse()

Estudiante1.cambiar_carrera("Sistemas")
Estudiante1.presentarse()

print(f" Total Estudiantes {Estudiante.total_estudiantes}")

multiplos_3 = [  i * 3 for i in range(1,11)]
print(multiplos_3)
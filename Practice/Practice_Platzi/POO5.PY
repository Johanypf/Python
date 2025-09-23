

# class CAR():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#         self.state = False

#     def start(self):
#         self.state = True
#         print(f" el carro {self.model} ha sido prendido")

#     def apagar(self):
#         self.state = False
#         print(f"El carro {self.model} se ha apagado")



# carro = CAR("Toyota","2024")

# carro.start()
# print(carro.state)
# carro.apagar()
# print(carro.state)



class User:
  def __init__(self, name, age):
    #Tu código aquí
    self.__name = name
    self.__age = age
    self.__friends =[]
    self.__messages = [] 
  
  @property
  def name(self):
    return self.__name
  
  @name.setter
  def name(self,name):
    self.__name = name

  @property
  def age(self):
    return self.__age
  
  @age.setter
  def age(self,age):
    self.__age= age
    
  def addFriend(self,friend):
    self.__friends.append(friend)

  def sendMessage(self,message, friend):
    self.__messages.append(message)

  def showMessages(self):
   print (self.__messages)


usario = User("ana",23)
usario.addFriend('fed')
usuario2 = User("Maria", 25)
usario.addFriend(usuario2)
usario.sendMessage("Hola Maria!", usuario2)

usario.showMessages()
usario.name


# usuario1 = User("Juan", 20)
# usuario1.name = "Pepito"
# print(usuario1.name)
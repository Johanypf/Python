class MyList:
  def __init__(self):
    self.data = {}
    self.length = 0

  def append(self, item):
    self.data[self.length] = item
    self.length += 1 
    

  def pop(self):
    if self.length == 0:
        return None
    
    keys = list(self.data.keys())
    last_key = keys[-1]
    last_value = self.data[last_key]

    del self.data[last_key]
    self.length -= 1

    return last_value

  def shift(self):
    if self.length == 0:
        return None
    
    keys = list(self.data.keys())
    firts_key = keys[0]
    first_values = self.data[firts_key]

    del self.data[firts_key]
    self.length -= 1

    return first_values

  def unshift(self, item):
    new_data = {0: item}
    for i in range(self.length):
        new_data[i + 1] = self.data[i]
    self.data = new_data
    self.length += 1


  def map(self, func):
     list_final = MyList()
     list_final.data = {k:func(v) for k,v in self.data.items()}
     list_final.length = len(list_final.data)
     return list_final


  def filter(self, func):
    new_data = MyList()
    new_data.data = { k: value for k,value in self.data.items() if func(value)}
    new_data.length = len(new_data.data)
    return new_data
  


  def join(self, character= ","):
    character = str(character)
    new_cha = ""
    if len(character) == 0:
        character = ","
    for i in range(len(self.data.values())):
      if i == (len(self.data.values())-1):
            new_cha += str(self.data[i])
      else:
            new_cha += str(self.data[i]) + character

    return new_cha 
    
      

myList = MyList()
myList.append(1)
myList.append(2)
myList.append(3)

print(myList.data)
print(myList.join("#"))


myList2 = MyList()
myList2.append("Platzinauta")
myList2.unshift("Hola!")


mapped_list = myList.map(lambda x: x.upper())
print(mapped_list.data)


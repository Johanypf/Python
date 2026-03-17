class Pay:
  def __init__(self):
    pass
  
  def make_pay(self,cantidad):
    self.cantidad = cantidad
    return {"realized":True,"quantity": cantidad}
      
class Cash(Pay):
  def make_pay(self,cantidad):
    return super().make_pay(cantidad)

class Card(Pay):
  def __init__(self, card):
    self.card = card

  def make_pay(self,cantidad):
      if len(self.card) == 16:
          data = super().make_pay(cantidad)
          data['last_card_numbers'] = self.card[-4:]
          return data

      else:
         raise Exception("Numeros incorrectos")

class PayPal(Pay):
  def __init__(self,email):
    self.email = email

  def make_pay(self,cantidad):
    data = super().make_pay(cantidad)
    data["platform"] = "PayPal"
    data["email"] = self.email
    return data



def process_pay(metodo_pago,cantidad):
    return metodo_pago.make_pay(cantidad)


card = Card("4913478952341122")
print(process_pay(card, 100))

paypal = PayPal("test@mail.com")
print(process_pay(paypal, 240))

cash = Cash()
print(process_pay(cash, 400))


# from pay import Pay
# from paypal import PayPal
# from cash import Cash
# from card import Card


def map(self, func):
        # Tu código aquí 👇
        """ 
        map(func): itera sobre cada elemento de nuestra estructura aplicando la función func a cada uno de ellos y devuelve una nueva
        lista (que será una instancia de MyList).
        """
        mapped_list = MyList()
        for key, value in self.data.items():
            mapped_list.append(func(value))
        return mapped_list

def filter(self, func):
        # Tu código aquí 👇
        """
        filter(func): itera sobre cada elemento de nuestra estructura filtrándolos según lo que indique la función func y devuelve una lista con los elementos filtrados (también una instancia de MyList).
        """
        filtered_list = MyList()
        for key, value in self.data.items():
            if func(value):
                filtered_list.append(value)
        return filtered_list
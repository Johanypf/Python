# Ejemplo 1:
# Input: calculate_discounted_price(100, 0.2)
# Output: 80.0

# Ejemplo 2:
# Input: calculate_discounted_price(-50, 0.2)
# Output: ValueError: El precio y el descuento deben ser valores positivos

def calculate_discounted_price(price, discount):
    try:
        if price < 0 or discount < 0:
            raise ValueError("El precio y el descuento deben ser valores positivos")
        else:
            return (price - (price * discount))
    except TypeError:
        raise TypeError("El precio y el descuento deben ser números")     
  


print(calculate_discounted_price(-5,0.2))
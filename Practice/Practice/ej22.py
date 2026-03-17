# Input: calculate_average([1, 2, 3, 4, 5])
# Output: 3.0

# Ejemplo 2:
# Input: calculate_average([10, 20, 30, 40, 50])
# Output: 30.0

# Ejemplo 3:
# Input: calculate_average([])
# Output: ValueError: La lista está vacía

# Ejemplo 4:
# Input: calculate_average([1, 2, '3', 4, 5])
# Output: TypeError: La lista contiene elementos no numéricos


def calculate_average(numbers):
  
    if not numbers:
      raise ValueError("La lista está vacía")
    else:
      try:
        return(sum(numbers)/len(numbers))
      except TypeError :
        raise TypeError("La lista contiene elementos no numéricos")
  


print(calculate_average([1, 2, '3', 4, 5]))  







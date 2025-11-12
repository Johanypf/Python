"""
PAR O IMPAR
Crea un programa que compruebe si
un número entero es par o impar.
"""

def Even_Oddo(num):
    
    if num % 2 == 0:
        return (f"El numero {num} es Par")
    else:
         return (f"El numero {num} es Impar")


print(Even_Oddo(10))
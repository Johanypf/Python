"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""

def num_primo(num):
   
     if num == 1:
        return False
     for i in range(2,num):
        if num % i == 0:
            return False
     
     return True

for i in range(1,101):
    print(f"el Numero {i} es  {'Primo' if num_primo(i) else'No Primo'}")
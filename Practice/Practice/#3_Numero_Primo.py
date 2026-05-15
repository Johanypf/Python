# # /*
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  */



def num_primo(number:int):
    if number < 2:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

for i in range(1,101):
    if num_primo(i):
        print(f"El numero {i} es Primo")
    else:
        print(f"El numero {i} No es Primo")
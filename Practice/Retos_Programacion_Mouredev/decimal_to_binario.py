"""
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
"""
 
def decimal_binario(num):
    binario = []
    while num:
        binario.append(num % 2)
        num = num // 2

    return  int("".join(map(str, binario[::-1])))

print(decimal_binario(10))

 
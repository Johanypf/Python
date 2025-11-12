"""
DECIMAL A BINARIO
Crea un programa se encargue de
transformar un número decimal a binario.
"""




def decimal_to_binario(x):
    binario = ''
    while x>0:
        binario = f"{x % 2}{binario}"
        x = x//2 
    
    if binario == '': 
        return "0"
    else:
        return binario


print(decimal_to_binario(3))

    
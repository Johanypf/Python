numeros = [
    [2,5,8],
    [5,8,9],
    [2,5,4]
]


def operar(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b

operacion = '+'
 
for fila in range(0,3):
   x = numeros[fila][fila]
   result = operar(x,x,"+")
   numeros[fila][fila] = result
  
for x in range(1,4,2):
    y= numeros[x-1][-x]
    result_2 = operar(y,y,"+")
    numeros[x-1][-x] = result_2


# Cadena con el símbolo de la operación a realizar. El símbolo puede ser '+', '-', '*' o '/'.

print(numeros)



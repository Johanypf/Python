
#None actúa como un marcador temporal hasta que aparece el primer valor válido.
numeros = [3,4,5,6,7,8,-1]

menor = None
for i in numeros:
    if menor is None or i < menor:
        menor = i

print(menor)

numbers = [1,2,3,4,5]

cuadrado = []

for num in numbers:
    cuadrado.append(num ** 2)

print(numbers)
print(cuadrado)


def cuadrado( num: int) -> int:
    return num ** 2
    
cuadrados_map = list(map(cuadrado,numbers))
print(cuadrados_map)
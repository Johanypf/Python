numeros = [
    [2,5,8],
    [5,8,9],
    [2,5,4]
]


vector_1 = (5,8,9)
vector_2 = (5,8,9)
total = []
for i in range(3):
    x = vector_1[i]
    y = vector_2[i]
    total.append(vector_1[i]+ vector_2[i])

total_tupla = tuple(total)

print(total_tupla)

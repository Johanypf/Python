nums = [1,3,3,3,2,1,3]

def most_common(nums):

    counts = {}
    max_count = 0 
    result = None

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

        if counts[num] > max_count:
            max_count = counts[num]
            result = num
    return result



print(most_common(nums))
print("#" * 5, "Task_1")

"""
from collections import Counter
def most_common(nums):
    counts = Counter(nums)
    return counts.most_common(1)[0][0]

print(most_common(nums))
"""


A = [1,3,2]

def missing_num(nums):
    
    num = set(nums)
    n = len(nums)
    
    for i in range(1,n + 2 ):
        print(i)
        if i not in num:
            return i


def missing_num2(nums):    
    num = set(nums)
    i = 1
    while True:
        if i not in num:
            return i
        i +=1

print(missing_num(A))
#print(missing_num2(A))


datos =  [1, 3, 6, 4, 1, 2]

# def encontrar_impar(lista):
#     resultado = 0
#     for numero in lista:
#         resultado ^= numero
#     return resultado


## conteo de numeros
counts = {}
for num in datos:
    counts[num] = counts.get(num, 0) + 1

print(counts)


## eliminar numeros repetidos
resu = 0
for num in datos:
    resu ^= num
    print(resu)
    


## 
numeros = set(datos)
print(numeros)

def menor_entero_positivo(lista):
    numeros = set(lista)
    i = 1
    while True:
        if i not in numeros:
            return i
        i += 1


print(menor_entero_positivo(datos))

s = "swiss"

counts = {}
for char in s:
    counts[char] = counts.get(char, 0) + 1
print(counts)

for char, count in counts.items():
    if count == 1:
        print(char)
        break       



nums = [2,7,11,15]

target = 40
seen = {}

for i, num in enumerate(nums):
        diff = target - num
        print(diff)
        
        if diff in seen:
            print([seen[diff], i])
        
        seen[num] = i

print(seen)


from collections import Counter

def most_common(nums):
    counts = Counter(nums)
    return counts.most_common(1)[0][0]

print(most_common(datos))

def move_zeros(nums):
    pos = 0

    for num in nums:
        if num != 0:
            nums[pos] = num
            pos += 1

    for i in range(pos, len(nums)):
        nums[i] = 0

    return nums

def max_subarray(nums):
    current = nums[0]
    best = nums[0]

    for n in nums[1:]:
        current = max(n, current + n)
        best = max(best, current)

    return best

def max_profit(prices):
    min_price = float('inf')
    profit = 0

    for p in prices:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)

    return profit

# left = 0

# for right in range(len(nums)):

#     while condition:
#         left += 1

        




    
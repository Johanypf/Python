import random

voc = ["a","e","i","o","u"]


random.shuffle(voc)
print("letras shuffle :" ,voc)

print(random.choice(voc))

num = [ i for i in range(1,100) ]
print(num)
print(random.choice(num))

import statistics

num = [1,2,3,4,6,7,8]
print(statistics.mean(num))
word = "norma Hola"

cant_words = {}

for i in word:
    if  i in cant_words:
        cant_words[i] += 1
    else:
        cant_words[i] = 1

print(cant_words)
mayor =  0  
for x in cant_words:
    if cant_words[x] >= mayor:
        mayor = cant_words[x]

print(mayor)
max_word = []

for i in cant_words:
    if cant_words[i] >= mayor:
        max_word.append(i)

print(max_word)
a= sorted(max_word)
print(sorted(a[0]))
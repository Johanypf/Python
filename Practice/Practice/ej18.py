
vowels_1= [ "hello", "Python","world","platzi"]

# ["text", "test", "python", "example"]
# [ "hello", "Python","world","platzi"]
#Output: ["hello", "platzi"]

#nueva_lista = [expresion for elemento in lista_original if condicion]
two_words = []
vowels = "AEIOUaeiou"

# for i in vowels_1:
#     cont_vowels= 0 
#     for letter in i:
#         if letter in vowels:
#             cont_vowels += 1        
#     if cont_vowels == 2 :
#                   two_words.append(i)

two_words = [i for i in vowels_1 if sum(1 for letter in i if letter in vowels) == 2]
print(two_words)


def find_words_with_two_vowels(words):
  # Tu código aquí 👈
  two_words = []
  vowels = "AEIOUaeiou"

  two_words = [i for i in words if sum(1 for letter in i if letter in vowels) == 2]

  return two_words


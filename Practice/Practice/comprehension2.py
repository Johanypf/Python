#Dado nums = [1,2,3,4,5,6,7,8,9,10], 
# crea una lista con "par" o "impar" según cada número

nums = [1,2,3,4,5,6,7,8,9,10]

valor = ["par" if i % 2 == 0 else "impar" for i in nums]
print(valor)


#Dada frase = "hola mundo python es genial", 
# obtén una lista con la longitud de cada palabra.

frase = "hola mundo python es genial"
longitud_word = [len(word) for word in frase.split()]
print(longitud_word)

#Dado nums = [-3,-1,0,2,4,-5,7], 
# crea una lista con el valor absoluto solo de los números negativos.
nums = [-3,-1,0,2,4,-5,7]
valor_abs = [ abs(i) for i in nums if i<0]
print(valor_abs)
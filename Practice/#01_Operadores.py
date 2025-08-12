# /*
#  * EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  *
#  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#  */

# OPERADORES 

#Arithmetic Operators
task_1 = 5 + 3 # addition +     
task_2 = 10 - 2 # Subtraction -
task_3 = 10 / 2 # Divsion (Float) / 
task_4 = 10 // 3 # Floor Division
task_5 = 4 * 3 # Multiplication *
task_6 = 5 % 2 # modulus
task_7 = 5 ** 2 # Exponentiation


# Comparison Operators
task_8 =  5 == 5    # ==	Equal to
task_9 =  5!= 3     # !=	Not equal to
task_10 =  5 > 3    # >	Greater than
task_11 =  3 < 10   # <	Less than	
task_12 =  5 >= 3   # >=	Greater than or equal to
task_13 =  7 <= 3   #<=	Less than or equal to


#Logical Operators

task_14 = (5 > 3) and (2 < 4)	# and	True if both are true	
task_15 = (5 > 3) or (2 > 4)	# or	True if at least one is true
task_15 = not True              #not	Reverses the logical value	



#Conditional Statements (Decision Making) Used to execute code only when certain conditions are met.
#if statement
age = 18
if age >= 18:
    print("You are an adult.")

# if...else
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


#if...elif...else (multiple conditions)

score = 4

if score >= 4.5:
    print("E grade")
elif score >= 4:
    print("S grade")
elif score >= 3:
    print('A grade')
else:
    print("I grade")


# Loops (Repetition) Used to repeat code

#for loop (iterate over a sequence)
print('\nFor loop')
for i in range(3):
    print(i) # prints  0 to 3


#while loop (repeat while condition is true)  


print("****" * 5) 
print('\nWhile loop')
start = 0
while start>3:
    print(start)
    start += 1

# Loop Control Keywords Modify the behavior of loops.

# break	-Ends the loop immediately
print("****" * 5)
print('\n Break control')
for i in range(5):
    if i == 3:
        break
    print(i)  # prints 0,1,2


#continue  - Skips the rest of the code in the loop for the current iteration 
print("****" * 5)
print('\n continue control')
for i in range(5):
    if i == 2:
        continue
    print(i)  # prints 0,1,3,4

#pass | Does nothing (placeholder) |
print("****" * 5)
print('\n pass control')
for i in range(3):
    pass  # useful for empty blocks


#match...case ( Acts like a switch in other languages)
print("****" * 5)
print('\n Match case')
command = "start"

match command:
    case "start":
        print("System starting...")
    case "stop":
        print("System stopping...")
    case _:
        print("Unknown command.")


# DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  *


for i in range(10,56):
    #Determine if is Even
    if ( i % 2 == 0 and  i % 3 != 0 and  i!=16 ):
            print(i)
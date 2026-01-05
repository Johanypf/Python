""""
Exercises: Level 2


12.The radius of a circle is 30 meters.
13.Calculate the area of a circle and assign the value to a variable name of area_of_circle
14.Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
15.Take radius as user input and calculate the area.
16.Use the built-in input function to get first name, last name, country and age from a user and store the value to their 
corresponding variable names
17.Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

"""
# 1.
import math
radius = 30
area_of_circle = round(math.pi * (radius * radius),2)
print(f" El area de circulo de  radio {radius} es de : {area_of_circle}")


circum_of_circle = round(2 * math.pi * (radius),2)
print(f" La circuferencia del circulo de radio {radius} es de {circum_of_circle}")

print("#" * 10)

user_radius = float(input("Digite el radio de la circuferencia : \n"))
area_of_circle_2 = round(math.pi * (user_radius * user_radius),2)
print(f" El area de circulo de  radio {user_radius} es de : {area_of_circle_2}")

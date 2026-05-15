name = "Ana"
text = f"Hola{name}"
year = 1996

print(text)

text_suma = f"Hola, la suma es: {1+1}"
print(text_suma)


text_suma = f"Hola, {name}, tu edad es:{2025 - year}"
print("======")
#print(text_suma)
#print("======")
text_func = f"Hola {name.upper()}"
print(text_func)
#print("======")
edad = 20
text_if = f"Hola {name}, eres {'mayor' if edad >= 18 else 'menor' } de edad "
#print(text_if)


print("======")
bank_balance = 2300000
print(f"tu saldo en la cuenta bancaria es: {bank_balance:,}")

print("=====")
stock_price = 1.405
print(f"El valor del stock es: {stock_price:.1f}")

user_id = 1
print(f"Su id es: {user_id:03d}")


producto = "Laptop"
price = 2300
text = f"Producto {producto:<10} | Price {price:>10}"
print(f"{text}\n{text}")

from datetime import datetime
date = datetime(2026,5,11)
text_2 = f" la fecha completa es {date: %A %d de %B de %Y a las %I:%M %p}"
print(text_2)

text_4 = 64
print(f"Unicode character : {text_4:c}")

print(f"Numero en formato Cientifico : {price:E}")
num = 0.80
print(f"numero en formato Percentage {num:.0%}")




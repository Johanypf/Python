## los cuadrados de los números pares de la siguiente lista.
numeros = [1, 2, 3, 4, 5]
cuadrados = [ i ** 2 for i in numeros if i % 2 == 0 ]
print("\n")
print("#" * 15)
print(numeros)
print(cuadrados)

print("\n")
print("#" * 15)

#### dictionary- convertir los nombres de tus productos a MAYÚSCULAS:
productos = {'pera': 45, 'tomate': 453}
print(productos)
productos = {name.upper() : precio for name,precio in productos.items()}
print(productos)


##Dada la lista nombres = ["ana", "pedro", "andres", "juan", "alberto"],
#  crea una nueva lista que contenga solo los nombres que empiezan con la letra "a".
print("\n")
print("#" * 15)
nombres = ["ana", "pedro", "andres", "juan", "alberto"]
print(nombres)
nuevos_nombres = [ name for name in nombres if name[0].lower() == "a"]
print(f" Nombres Con inicial 'A' :{nuevos_nombres}")



##Tienes este inventario: stock = {"laptop": 10, "mouse": 0, "teclado": 5, "monitor": 0}.
# Crea un nuevo diccionario que contenga solo los productos que sí tienen stock
#  (es decir, que su valor sea mayor a 0).
print("\n")
print("#" * 15)
stock = {"laptop": 10, "mouse": 0, "teclado": 5, "monitor": 0}
print(f"Old stock : {stock}")
new_stock = {name :cant  for name,cant in  stock.items() if cant > 0 }
print(f"Nuevo stock : {new_stock}")

#### Dada una lista de números precios = [100, 200, 300, 400],
# crea una lista nueva donde a cada precio se le sume el 15% de impuesto.

print("\n")
print("#" * 15)
precios = [100, 200, 300, 400]
print(precios)
new_prices = [ precio * 1.15  for precio in precios]
print(f" Nuevos precios con Aumento de 15 %: {new_prices}")
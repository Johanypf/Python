# Reto 11: Costo total de un carro de compras
# Catalina necesita llevar un mejor control de sus gastos cuando hace mercado.
#  Para esto, ha decidido construir una aplicación para registrar cada producto 
# que agregue en su carrito de compras. Estos datos son guardados en un diccionario 
# cuyas llaves corresponden a los nombres de los productos. El valor asociado a cada 
# lave es el precio del producto correspondiente.

# Cree una función que retorne el valor total del carrito de compras. Esto es, la suma 
# de los precios individuales de todos los productos que están en el carrito.  

# Su solución debe tener una función de acuerdo con la siguiente especificación: 

# Nombre de la función: valor_carrito_compras  
products = {
    "Manzana": 92000,
    "Banano": 8000,
    "Leche": 35000,
    "Pan": 25000,
    "Huevos": 15000,
    "Arroz": 800000,
    "Aceite": 18000,
    "Queso": 92000,
    "Café": 13500,
    "Pollo": 22000
}

def valor_carrito_compras(carrito_compras:dict)->float:
    if not valor_carrito_compras:
        return (0)
    total = 0
    for i in carrito_compras.values():
        total += i

    return total

print(valor_carrito_compras(products))
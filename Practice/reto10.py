# Reto 10: Producto más caro de un carro de compras
# Catalina necesita llevar un mejor control de sus gastos cuando hace mercado.
#  Para esto, ha decidido construir una aplicación para registrar cada producto 
# que agregue en su carrito de compras. Estos datos son guardados en un diccionario 
# cuyas llaves corresponden a los nombres de los productos. El valor asociado a cada 
# llave es el precio del producto correspondiente.

# Cree una función que retorne el nombre del producto más costoso del carrito de compras.
#  Si se encuentran dos productos igual de costosos (siendo los más costosos del carro), 
# la función retorna el menor alfabéticamente. Por ejemplo, si los 'bananos' que compra
#  Catalina costaran los mismo que las 'chocolatinas', la función retornaría 'bananos'  

# Su solución debe tener una función de acuerdo con la siguiente especificación: 

# Nombre de la función: producto_mas_costoso
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

def producto_mas_costoso(carrito_compras:dict)->str:
    
    if not carrito_compras:
        return ("No hay productos en el carrito")

    expensive = max(carrito_compras.values())
    lista_productos = []
    for i,y in carrito_compras.items():
        if y == expensive:
            lista_productos.append(i)
            

    new_list = sorted(lista_productos)
     
    return new_list[0] 

    
print(producto_mas_costoso(products))
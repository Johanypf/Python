# Reto 9: El novio tacaño
# Nicolás es un novio muy amoroso, pero tiene fama de ser tacaño. Para el cumpleaños 
# de su novia ha pedido un catálogo de artículos para escoger el regalo más barato 
# disponible. El catálogo es un diccionario que tiene varias llaves que corresponden al
#  nombre de los productos. El valor asociado a cada llave es el precio del producto.
# Cree una función que retorne el nombre del artículo más barato en el catálogo.
# Si Nicolás encuentra dos artículos igual de baratos, comprará el que tenga el nombre 
# alfabéticamente menor (el que aparecería antes en el diccionario ignorando las mayúsculas y minúsculas).
# Si el artículo más barato vale más de 10.000 pesos, Nicolás no comprará nada e invitará 
# a su novia a ver una película en su casa.  

# Su solución debe tener una función de acuerdo con la siguiente especificación:

# Nombre de la función: producto_mas_barato  
products = {
    "Manzana": 12000,
    "Banano": 8000,
    "Leche": 35000,
    "Pan": 25000,
    "Huevos": 15000,
    "Arroz": 8000,
    "Aceite": 18000,
    "Queso": 92000,
    "Café": 13500,
    "Pollo": 22000
}
def producto_mas_barato(catalogo:dict)->str:
    if not catalogo:
        return ("No hay productos para escoger")
    
    menor_precio = min(catalogo.values())

    if menor_precio > 10000:
        return None
    else:
        lista_products = []
        for i,y in catalogo.items():
            if y == menor_precio:
                lista_products.append(i)
    
    new_list = sorted(lista_products)
    return new_list[0]

print(producto_mas_barato(products))
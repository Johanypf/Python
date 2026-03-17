products = {'Pear':45, "tomato":453, "Apple":234,"banana":32,"Kiwi":456}

for nombre, precio in products.items():
     if precio >= 50:
           print(nombre)


def aplicar_descuento(productos):
     
     for producto, precio in productos.items():
        productos[producto] = round( precio - (precio * 0.10) , 2 )

     return productos



aplicar_descuento(products)
print(products)
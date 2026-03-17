from traceback import print_exception


products = {'Pear':45, "tomato":453, "Apple":234,"banana":32,"Kiwi":456}

for nombre, precio in products.items():
     if precio >= 50:
           print(nombre)

nuevo_products = { produc: precio for produc,precio in products.items() if precio >= 50}
print(nuevo_products)


def aplicar_descuento(productos):
     
     for producto, precio in productos.items():
        productos[producto] = round( precio - (precio * 0.10) , 2 )

     return productos



aplicar_descuento(products)
print(products)

products = {'Pear':45, "tomato":453, "Apple":234,"banana":32,"Kiwi":456}
rebajados = {prod: round(pre * 0.9, 2) for prod, pre in products.items()}
print(rebajados)
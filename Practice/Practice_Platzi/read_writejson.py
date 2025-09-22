import json

file_path = 'products.json'

with open (file_path, mode ='r') as file:
    products = json.load(file)


for product in products:
    print(product)


new_product = {
    "name": "Wireless Charger_2",
    "price": 75,
    "quantity": 100,
    "brand": "ChargeMaster",
    "category": "Accessories",
    "entry_date": "2024-07-01"
}

products.append(new_product)

with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4)
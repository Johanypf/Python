import statistics
import csv

# data = [
#     ['Month','Sales'],
#     ["Enero",120],
#     ["Febrero",130],
#      ["Marzo",150],
#      ["Abril",170],
#      ["Mayo",160],
#      ["Junio",180],
#      ["Julio",190]
# ]

# with open("Datos_ventas.csv", "w" , newline="") as archivo_csv:
#     escritor_csv = csv.writer(archivo_csv)
#     escritor_csv.writerows(data)

month_sales = {}
with open("Datos_ventas.csv", mode= 'r' ) as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['Month']
        sales = int(row["Sales"])
        month_sales[month]= sales


print(month_sales)

sales = list(month_sales.values())
print(sales)

mean_sales = statistics.mean(sales)
print(f"la medio de Sales es: {mean_sales}")

moda_sales = statistics.mode(sales)
print(f"La mode de Sales es : {moda_sales}")

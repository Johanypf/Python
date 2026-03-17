import matplotlib.pyplot as plt

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

temperatura_bog = [23.8, 23.5, 24.5, 24.2, 22.7, 22.5, 21.5, 21.6,
                   22.6, 22.7, 22.8, 22.9]


plt.figure(figsize=(12,5))
plt.plot(meses,temperatura_bog, label ="Temperatura")
plt.xlabel("Mese")
plt.ylabel("Temperatura")
plt.title("Temperatura Promedio Bogota (2007) ")
plt.legend()
plt.show()


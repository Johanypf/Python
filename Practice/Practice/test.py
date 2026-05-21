import requests
import numpy as np
import pandas as pd


data = {"data": "key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47"}

datos = data["data"]
df = pd.Series(datos.split(", key=")).str.extract(
    r"(?:key=)?(?P<key>\w+),\s*age=(?P<age>\d+)"
)

df = df.reset_index(drop=True)
df["age"] = pd.to_numeric(df["age"])
# mayores_50 = df[df["age"] > 50]
print(len(df[df["age"] > 50]))
# cantidad_mayores_50 = len(mayores_50)
# print(f"Cantidad de personas mayores de 50: {cantidad_mayores_50}")
# print(mayores_50)

# print(df_50)

import numpy as np

matriz = np.array([[0,0,1],[0,1,0],[1,0,0]])
inversa = np.linalg.inv(matriz)
print(matriz)
print(inversa)
print("*****"* 8)
matriz_2 = np.array([[1,0,0],[0,1,0],[0,0,1]])
inversa_2 = np.linalg.inv(matriz_2)
print(inversa_2)

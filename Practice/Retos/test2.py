list_b = []
for fila in range(4):
    for col in range(4):
          if fila == col or fila + col == 3:
               valor = "x"
               list_b[fila] =valor
          else:
                valor = ""
                list_b[fila] =valor





print(list_b)
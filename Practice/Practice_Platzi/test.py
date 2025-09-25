map = {}

# Agregar pares clave-valor al Map
map["key1"] = "value1"
map["key2"] = "value2"
map[3] = "value3"

print(map)
# Obtener el valor asociado a una clave
print(map.get("key1"))  # Output: "value1"

# Verificar si una clave existe en el Map
print("key2" in map)  # Output: True

# # Eliminar una clave del Map
# del map["key2"]

# # Verificar si una clave existe en el Map después de ser eliminada
# print("key2" in map)  # Output: False

# # Vaciar el Map
# map.clear()

# Verificar el tamaño del Map después de ser vaciado
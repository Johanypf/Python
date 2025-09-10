pokemones = [
    {
        "nombre": "Pikachu",
        "vida": 100,
        "ataque": 505,
        "defensa": 40,
        "ataque_especial": 50,
        "defensa_especial": 50,
        "velocidad": 90
    }
]

list_final = []
for i in pokemones:
    poderes = 0
    poderes += i["vida"]
    poderes += i["ataque"]
    poderes += i["defensa"]
    poderes += i["ataque_especial"]
    poderes += i["defensa_especial"]
    poderes += i["velocidad"]

    if poderes >= 600:
        list_final.append(i['nombre'])

print(list_final)
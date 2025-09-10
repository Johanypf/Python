# Reto 8: Ash y la liga Kalos
# Ash Ketchum, el personaje principal del anime Pokémon, está a
#  punto de luchar en la final de la liga Kalos. En estos eventos
#  compiten los mejores entrenadores del mundo en batallas donde 
# cada entrenador puede tener 3, 4, 5 o 6 criaturas. Ash quiere saber, 
# para una cantidad de criaturas específica, si él podrá formar un equipo 
# únicamente con Pokémon seudolegendarios para competir en la final. Un pokemon 
# seudolegendario es aquel que en la suma de sus estadísticas de combate tiene 600 puntos o más.

# Las estadísticas de combate de cada pokemon son 6:  
# "ataque"
# "defensa"
# "ataque_especial"
# "defensa_especial"
# "velocidad"
# "vida"  
# Escriba una función que, dada una lista de diccionarios (cada uno representando un pokémon) 
# con las anteriores estadísticas, determine si Ash podrá formar un equipo de pokémon seudolegendarios 
# para afrontar la final de la liga. En caso que Ash pueda formar un equipo, retorne una lista con los 
# nombres de las criaturas que Ash utilizaría en la batalla. Si es imposible generar un equipo que 
# cumpla con las condiciones, retorne None.
# Se garantiza que en caso de poder formar un equipo válido, solamente habrá una configuración posible.  
# La lista de retorno debe componerse únicamente de cadenas de caracteres y debe tener el mismo 
# orden de la lista que llega por parámetro.  

# Su solución debe tener una función de acuerdo con la siguiente especificación: 

# Nombre de la función: construir_equipo_pokemon
pokemones = [
    {
        "nombre": "Pikachu",
        "vida": 35,
        "ataque": 550,
        "defensa": 40,
        "ataque_especial": 50,
        "defensa_especial": 50,
        "velocidad": 90
    },
    {
        "nombre": "Charizard",
        "vida": 780,
        "ataque": 84,
        "defensa": 78,
        "ataque_especial": 109,
        "defensa_especial": 85,
        "velocidad": 100
    },
    {
        "nombre": "Bulbasaur",
        "vida": 450,
        "ataque": 49,
        "defensa": 49,
        "ataque_especial": 65,
        "defensa_especial": 65,
        "velocidad": 45
    },
    {
        "nombre": "Squirtle",
        "vida": 44,
        "ataque": 48,
        "defensa": 65,
        "ataque_especial": 50,
        "defensa_especial": 64,
        "velocidad": 43
    },
    {
        "nombre": "Snorlax",
        "vida": 160,
        "ataque": 110,
        "defensa": 65,
        "ataque_especial": 65,
        "defensa_especial": 110,
        "velocidad": 30
    }
]

def construir_equipo_pokemon(Cantidad:int,Lista_pkmn:list)->list:
    list_final = []
    for i in Lista_pkmn:
        poderes = 0
        poderes += i["vida"]
        poderes += i["ataque"]
        poderes += i["defensa"]
        poderes += i["ataque_especial"]
        poderes += i["defensa_especial"]
        poderes += i["velocidad"]

        if poderes >= 600:
            list_final.append(i['nombre'])
    
    if len(list_final) >= Cantidad:

        return list_final[0:len(list_final)]
    else: 
        return None

print(construir_equipo_pokemon(3,pokemones))






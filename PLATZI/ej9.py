
estudiante_1 = {
    "nombre": "Lucía Sánchez",
    "matematicas": 5.0,
    "español": 3.9,
    "ciencias": 4.0,
    "literatura": 4.1,
    "arte": 3.8
}


estudiante_2 = {
    "nombre": "Mateo Ríos",
    "matematicas": 4.8,
    "español": 5.0,
    "ciencias": 3.9,
    "literatura": 3.6,
    "arte": 5.0
}

estudiante_3 = {
    "nombre": "Isabella Torres",
    "matematicas": 4.8,
    "español": 4.6,
    "ciencias": 4.7,
    "literatura": 5.0,
    "arte": 4.5
}

estudiante_4 = {
    "nombre": "Tomás Herrera",
    "matematicas": 2.9,
    "español": 5.0,
    "ciencias": 3.0,
    "literatura": 3.2,
    "arte": 2.8
}

estudiante_5 = {
    "nombre": "Emma Castro",
    "matematicas": 3.8,
    "español": 4.0,
    "ciencias": 5.0,
    "literatura": 4.2,
    "arte": 3.9
}
def mejor_de_cada_curso (estudiante1:dict,estudiante2:dict ,estudiante3:dict, estudiante4:dict,estudiante5:dict)-> dict :

    Matemathic = {}
    Espanol  = {}
    Ciencias = {}
    Literatura = {}
    Arte = {}

    


    Matemathic = {}
    for mathe in estudiante1,estudiante2,estudiante3,estudiante4,estudiante5:
        Matemathic[mathe["nombre"]] = mathe["matematicas"]
    best_mathe = []
    mayor_actual = 0
    for  best in Matemathic:
            nota = Matemathic[best]
            if mayor_actual is None or nota > mayor_actual:
                mayor_actual = nota
                best_mathe = [best]
            elif nota == mayor_actual:
                best_mathe.append(best)
    best_mathe = [nombre.lower() for nombre in best_mathe]
    best_mathe = sorted(best_mathe)
        
    
    Espanol  = {}
    for esp in estudiante1,estudiante2,estudiante3,estudiante4,estudiante5:
        Espanol[esp["nombre"]] = esp["español"]
    best_esp = []
    mayor_actual_1 = 0
    for  best in Espanol:
            nota = Espanol[best]
            if mayor_actual_1 is None or nota > mayor_actual_1:
                mayor_actual_1 = nota
                best_esp = [best]
            elif nota == mayor_actual_1:
                best_esp.append(best)
    best_esp = [nombre.lower() for nombre in best_esp]
    best_esp = sorted(best_esp)


    Ciencias = {}
    for cienc in estudiante1,estudiante2,estudiante3,estudiante4,estudiante5:
        Ciencias[cienc["nombre"]] = cienc["ciencias"]
       
    best_cienc = []
    mayor_actual_2 = 0
    for  best in Ciencias:
            nota = Ciencias[best]
            if mayor_actual_1 is None or nota > mayor_actual_2:
                mayor_actual_2 = nota
                best_cienc= [best]
            elif nota == mayor_actual_2:
                best_cienc.append(best)
    best_cienc= [nombre.lower() for nombre in best_cienc]
    best_cienc = sorted(best_cienc)


    Literatura = {}
    for lit in estudiante1,estudiante2,estudiante3,estudiante4,estudiante5:
        Literatura[lit["nombre"]] = lit["literatura"]
    best_lit= []
    mayor_actual_3 = 0
    for  best in Literatura:
            nota = Literatura[best]
            if mayor_actual_3 is None or nota > mayor_actual_3:
                mayor_actual_3 = nota
                best_lit= [best]
            elif nota == mayor_actual_3:
                best_lit.append(best)
    best_lit= [nombre.lower() for nombre in best_lit]
    best_lit = sorted(best_lit)


    Arte = {}
    for Art in estudiante1,estudiante2,estudiante3,estudiante4,estudiante5:
        Arte[Art["nombre"]] = Art["arte"]
       
    best_art= []
    mayor_actual_4 = 0
    for  best in Arte:
            nota = Arte[best]
            if mayor_actual_4 is None or nota > mayor_actual_4:
                mayor_actual_4 = nota
                best_art = [best]
            elif nota == mayor_actual_4:
                best_art.append(best)
    best_art= [nombre.lower() for nombre in best_art]
    best_art = sorted(best_art)

    Best_course = {
    "matematicas": best_mathe[0],
    "español": best_esp[0],
    "ciencias": best_cienc[0],
    "literatura": best_lit[0],
    "arte": best_art[0]}
            




    return Best_course



print(mejor_de_cada_curso(estudiante_1,estudiante_2,estudiante_3,estudiante_4,estudiante_5))



def mejor_de_cada_curso(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5):
    estudiantes = [estudiante1, estudiante2, estudiante3, estudiante4, estudiante5]

    mejores = {
        "matematicas": ("", -1),
        "español": ("", -1),
        "ciencias": ("", -1),
        "literatura": ("", -1),
        "arte": ("", -1),
    }

    for estudiante in estudiantes:
        nombre = estudiante["nombre"]
        for curso in mejores:
            nota_actual = estudiante[curso]
            nombre_mejor, nota_mejor = mejores[curso]

            # Comparamos la nota y si es igual, comparamos nombre alfabéticamente (insensible a mayúsculas)
            if (nota_actual > nota_mejor) or (
                nota_actual == nota_mejor and nombre.lower() < nombre_mejor.lower()
            ):
                mejores[curso] = (nombre, nota_actual)

    # Devolver solo los nombres de los mejores
    return {curso: nombre for curso, (nombre, _) in mejores.items()}




def mejor_de_cada_curso(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5):
    estudiantes = [estudiante1, estudiante2, estudiante3, estudiante4, estudiante5]
    cursos = ["matematicas", "español", "ciencias", "literatura", "arte"]
    resultado = {}

    for curso in cursos:
        mejor_nota = -1
        mejores_nombres = []

        for estudiante in estudiantes:
            nota = estudiante[curso]
            nombre = estudiante["nombre"]

            if nota > mejor_nota:
                mejor_nota = nota
                mejores_nombres = [nombre]
            elif nota == mejor_nota:
                mejores_nombres.append(nombre)

        # Elegir el nombre menor alfabéticamente (sin importar mayúsculas)
        resultado[curso] = sorted(mejores_nombres, key=lambda x: x.lower())[0]

    return resultado



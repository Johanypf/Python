"""
expliacion
de docstring
mirar como funciona Docstring

"""


def ejemplo():
    return ("Hola mundo")

def ejemplo_docstring() -> str:
    """
    DESCRIPTION
    ARGS
    RETURNS
    EXCEPTIONS
    EJEMPLOS


    Esta funcion devuelve un saludo.

    Returns:
        str: Un saludo en español.

    """
    return "Hola, Mundo"

print(ejemplo_docstring.__doc__)
#help(ejemplo_docstring)
print(f"{'x' * 15}")
print(ejemplo.__doc__)


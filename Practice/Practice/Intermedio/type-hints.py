"""  Typing con Python"""

from doctest import Example


variable: int | str =  42
print(f'Variable {variable}, del tipo {type(variable)}')


variable = 'Texto de prueba'
print(f'Variable {variable}, del tipo {type(variable)}')

variable_2 : int = 44
print(f'Variable {variable_2}, del tipo {type(variable_2)}')


def suma_clara(a: int, b: int)->  int:
    """
    Retorna la suma de dos números enteros.

    Parámetros
    ----------
    a : int
        Primer sumando.
    b : int
        Segundo sumando.
    Retorna
    -------
    int
        Resultado de a + b.

    Ejemplos
    --------
    >>> suma_clara(3, 5)
    8
    >>> suma_clara(-1, 1)
    0
    """
    return a + b 

print(suma_clara(2,3))

articles: list[list] = [ 
    [1,3],
    ["test"] 
    ]

print(articles)

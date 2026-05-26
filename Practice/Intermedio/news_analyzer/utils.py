"""Utilidades varias para la aplicación."""

def clean_text(text: str) -> str:
    """
    Limpia y normaliza una cadena de texto eliminando espacios y convirtiéndola a minúsculas.

    Recibe una cadena de texto y aplica dos transformaciones sucesivas:
    primero elimina los espacios en blanco al inicio y al final, luego
    convierte todos los caracteres a minúsculas. Si la cadena está vacía
    o es falsy (None, ""), retorna una cadena vacía sin aplicar
    transformaciones.

    Parámetros
    ----------
    text : str
        Cadena de texto a limpiar. Puede contener espacios en blanco
        al inicio o al final, caracteres en mayúsculas o combinaciones
        de ambos. Si se pasa None o una cadena vacía, se retorna ""
        directamente.

    Retorna
    -------
    str
        Cadena de texto sin espacios en los extremos y en minúsculas.
        Retorna "" si la entrada es falsy.

    Excepciones
    -----------
    TypeError
        Si `text` no es de tipo str. Por ejemplo, si se pasa un entero
        o una lista, el método `.strip()` lanzará esta excepción.

    Ejemplos
    --------
    Caso básico con espacios y mayúsculas:

    >>> clean_text("  Hola Mundo  ")
    'hola mundo'

    Texto ya limpio, sin cambios visibles:

    >>> clean_text("python")
    'python'

    Cadena vacía retorna cadena vacía:

    >>> clean_text("")
    ''

    Cadena con solo espacios retorna cadena vacía:

    >>> clean_text("   ")
    ''

    Entrada None retorna cadena vacía:

    >>> clean_text(None)
    ''

    Tipo incorrecto lanza TypeError:

    >>> clean_text(123)
    TypeError: 'int' object has no attribute 'strip'
    """
    if not text:
        return ""
    return text.strip().lower()

def get_sources(articles):
    return set(article.get("source").get("name") for article in articles if article.get("source") and article.get("source").get("name"))

def get_articles_by_source(articles : list[dict], source : str ) -> list[dict]:

    return list(filter(
        lambda article : article['source']['name'].lower() == source.lower(),articles))


def get_reading_time(article: dict) -> dict:
    "calcula tiempo de lectura"

    minutes = len(article["content"]) // 200 + 1
    article["reading_time"] = minutes
    return article


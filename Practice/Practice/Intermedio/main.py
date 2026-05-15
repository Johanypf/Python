"""
Sistema de análisis de noticias con APIs múltiples.
"""

# PEP 8: Configuración centralizada - constantes en MAYÚSCULAS con guiones bajos
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = "es"  # PEP 8: Comillas dobles para strings


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


# PEP 8: Doble líneas en blanco entre funciones para separar lógicamente
def validate_api_key(api_key):
    """Valida que la API key tenga formato correcto."""
    return len(api_key) > 10 and api_key.isalnum()


# PEP 8: Funciones principales - agrupadas después de utilidades
def fetch_news_from_api(api_name, query):
    """Obtiene noticias de una API específica."""
    pass


def process_article_data(raw_data):
    """Procesa datos crudos de artículo."""
    pass


# Longitud de línea: Máximo 88 caracteres (Ruff default)
# Indentación: 4 espacios, nunca tabs
# Nombres descriptivos: snake_case para funciones y variables
# Imports ordenados: estándar → terceros → locales
# Líneas en blanco: Separar funciones y clases lógicamente
# Comillas consistentes: Usar comillas dobles para strings



def guardian_client():
    pass




import json
from urllib.error import HTTPError
import urllib.request
import urllib.parse
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")


class NewsSystemError(Exception):
    "Error general en la app"
    pass

class APIKeyError(NewsSystemError):
    "Error cuando la API KEY es invalida"
    pass


BASE_URL = 'https://newsapi.org/v2/everything'

def newsapi_client(api_key,query, timeout=30, retries=3):

    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"
    try:
        with urllib.request.urlopen(url,timeout = timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)

    except urllib.error.HTTPError:
        raise APIKeyError("Ocurrió un error, no se pudo conectar con la API")

    except Exception as e:
        return f"Error: {e}"
        

        return f"NewsAPI: {query} con timeout : {timeout}"



def fetch_news(api_name, *args, **kwargs):
    """
    Docstring for fetch_news
    
    :param api_name: Description
    :param args: Description
    :param kwargs: Description
    """

    base_config = {
        "timeout": 30,
        "retries":3
    }

    config = {
        **base_config,
        **kwargs
    }

    api_clients = {
        "newapi": newsapi_client,
        "guardian": guardian_client
    }
    client = api_clients[api_name]
    return client(*args, **config)

response_data = None
try:
    response_data = fetch_news("newapi", api_key = API_KEY, query="Python")
except APIKeyError as e:
    print(f" Error : {e}")

if response_data:
    for article in response_data["articles"]:
        print(article["title"])









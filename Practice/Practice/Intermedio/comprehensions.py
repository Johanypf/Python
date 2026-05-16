
from sample_data import sample_articles

def extract_titles_traditional(articles):
    """Extrae solo los títulos usando un for."""
    titles = []
    for article in articles:
        titles.append(article["title"])  
    return titles





def extract_tittle(articles):
    """Extra solo los titulos usando comprenhesion """
    return [articule["title"] for articule in articles]
     



def extract_tittle_10(articles : list[dict]) -> list[str]:
    """Extra solo los titulos usando comprenhesion """

    """
    Extrae títulos con más de 10 caracteres de una lista de artículos.

    Parámetros
    ----------
    articles : list[dict]
        Lista de diccionarios, cada uno debe tener la clave ``"title"``
        con un valor de tipo str.

    Retorna
    -------
    list[str]
        Títulos cuya longitud supera los 10 caracteres.

    Excepciones
    -----------
    KeyError
        Si algún diccionario no contiene la clave ``"title"``.

    Ejemplos
    --------
    >>> articles = [
    ...     {"title": "Hola"},
    ...     {"title": "Inteligencia Artificial"},
    ... ]
    >>> extract_title_10(articles)
    ['Inteligencia Artificial']
    """
    return [articule["title"] for articule in articles if len(articule['title']) > 10]
    

def title_description(articles):
    new_dict = {}
    for articule in articles:
        new_dict[articule['title']] = articule['description']
    return new_dict

def title_description_2(articles):
    return { articule['title']: articule['description'] for articule in articles}


def extract_source(articles):
    source = set()
    for articule in articles:
        source.add(articule["source"]["name"])
    return source

def extract_source_2(articles):
    return set(articule["source"]["name"]for articule in articles)


def get_sources_tradi(articles):
    sources = set()
    for article in articles:
        if article.get("source") and article.get("source").get("name"):
            sources.add(article.get("source").get("name"))

    return sources

def get_sources(articles):
    return set(article.get("source").get("name") for article in articles if article.get("source") and article.get("source").get("name"))



print(extract_titles_traditional(sample_articles))
print("===========")
print(extract_tittle(sample_articles))
print("========")
print(extract_tittle_10(sample_articles))


print('=======')
print(title_description(sample_articles))    
print('=======')
print(title_description_2(sample_articles))    

print('=======')
print(extract_source(sample_articles))

print('=======')
print(extract_source_2(sample_articles))

print('=======')
print(get_sources_tradi(sample_articles))

print('=======')
print(get_sources(sample_articles))


def categorize_traditionl(articles):
    sources = get_sources(articles)
    results = {}
    for source in sources:
        if source not in results:
            results[source] = []
        for article in articles:
            if source == article.get("source").get("name"):
                results[source].append(article)

    return results


def categorize(articles):
    sources = get_sources(articles)
    return { 
        source : [
            article 
            for article in articles
            if source == article.get("source").get("name")
        ]
        for source in sources
    }

print("======")
print(categorize_traditionl(sample_articles))

print("=======")
print(categorize(sample_articles))


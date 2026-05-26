from sample_data import sample_articles

for article in sample_articles:
    print(article)


for posicion, article in enumerate(sample_articles):
    print(f"El articulo {article["title"]} esta en la posicion {posicion + 1} ")
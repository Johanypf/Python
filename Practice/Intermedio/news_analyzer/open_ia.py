from news_analyzer.config import OPEN_KEY
import os
from openai import OpenAI




def analyze_news_with_ia(articles: list[dict], query: str) -> str | None:
    

    client = OpenAI(
        
         api_key= OPEN_KEY
    )

    context = "\n".join(
        [
            f" - {article['title']} : {article.get('description','')[:1000] } ...."
            for article in articles[:1]
        ]
    )

    prompt = f""" Basandote en estas noticias : 
        {context}

        Pregunta: {query}
        Responda de forma concisa en español.
    """

    response = client.responses.create(
        model="gpt-4",
        instructions="Eres un agente que lee contexto y responde de manera breve",
        input=prompt,
    )

    print(response.output_text)

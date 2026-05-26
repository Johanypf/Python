#Analytics Chatbot

Sistema de análisis inteligente para operaciones Rappi con chatbot 
conversacional e insights automáticos.

## Demo en nube
- Prueba de Chatbot - 

## Descripción


## Arquitectura
- **Streamlit**: Interfaz visual del chatbot
- **Pandas**: Análisis de datos local (nunca se manda el Excel completo al LLM)
- **Groq (Llama 3)**: Generación de código pandas y redacción de respuestas
- **El flujo**: Usuario pregunta → LLM genera código → Pandas ejecuta contra datos reales → LLM redacta respuesta

## Funcionalidades
### Pestaña 1: Chatbot


## Instalación local
1. Clona el repositorio
2. Crea un archivo `.env` con tu API key:
```
GROQ_API_KEY=ClaveAqui
```
3. Instala las dependencias:
```
pip install -r requirements.txt
```
4. Corre la aplicación:
```
streamlit run app.py
```


## 🔧 Stack tecnológico
- Python 3.12
- Streamlit
- Pandas
- Groq (Llama 3.3 70b)
```

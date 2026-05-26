# Analytics Chatbot

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
- Preguntas de filtrado, comparación, tendencias y agregaciones
- Memoria conversacional
- Respuestas en lenguaje natural con tablas


## Instalación local




## 🔧 Stack tecnológico
- Python 3.12
- Streamlit
- Pandas
- Groq (Llama 3.3 70b)
```

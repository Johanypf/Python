import streamlit as st
import pandas as pd
from groq import Groq
from dotenv import load_dotenv
import os
import datetime


fecha_actual = datetime.date.today().strftime("%A, %d de %B de %Y")

# Cargar API key
load_dotenv()
cliente = Groq(api_key=os.getenv("GROQ_API_KEY"))


# Cargar Excel con @st.cache_data para optimizar rendimiento
@st.cache_data
def cargar_datos():
    df_tax = pd.read_excel(
        "Latinoamerica.xlsx",
        sheet_name="Paises",
    )
    return df_tax


df_paises = cargar_datos()

# Contexto que le damos al LLM sobre los datos
contexto_datos = f"""
    Hoy es {fecha_actual},
    Tienes acceso a los datos de los países con estas características:
    DATASET PAISES (df_paises) - {len(df_paises)} filas:
    Columnas: País,	Ciudad,	Población, 

    IMPORTANTE: Siempre usa los nombres técnicos reales de las columnas (País,	Ciudad,	Población)
    para filtrar y calcular
    
    Cuando el usuario haga una pregunta, genera ÚNICAMENTE código Python usando pandas
    para responder. El código debe:
    1. Usar df_paises según corresponda
    2. Guardar el resultado en una variable llamada 'resultado'
    3. No usar print(), solo asignar a 'resultado'
    4. Ser conciso y directo

    Solo responde con el código Python, sin explicaciones, sin ```python, sin nada más.
    """


# Historial del chat
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Interfaz
st.title("Chatboot Analytics")
st.caption(f"Datos cargados: {len(df_paises):,} filas de países")

# Mostrar historial
for msg in st.session_state.mensajes:
    with st.chat_message(msg["rol"]):
        st.write(msg["contenido"])

# Input del usuario
pregunta = st.chat_input("Haz una pregunta sobre los datos de los países...")

if pregunta:
    # Mostrar pregunta del usuario
    with st.chat_message("user"):
        st.write(pregunta)
    st.session_state.mensajes.append({"rol": "user", "contenido": pregunta})

    with st.chat_message("assistant"):
        with st.spinner("Analizando datos..."):
            try:
                # Pedir código al LLM
                prompt = f"{contexto_datos}\n\nPregunta del usuario: {pregunta}"
                respuesta_llm = cliente.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}],
                )
                codigo = respuesta_llm.choices[0].message.content.strip()
                print("Código generado por LLM:")
                print(codigo)

                entorno = {"df_paises": df_paises, "pd": pd}
                exec(codigo, entorno)
                resultado = entorno.get("resultado", "No se pudo calcular")

                # Pedir al LLM que redacte respuesta bonita
                prompt_final = f"""
                El usuario preguntó: {pregunta}
                El resultado del análisis es: {resultado}
                Redacta una respuesta clara y concisa en español para una persona interesada en conocer información de los países de acuerdo al resultado y el contexto y dataset {df_paises}.
                Si hay números, formatéalos bien. Máximo 3 párrafos..
                """
                respuesta_final = cliente.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt_final}],
                )
                respuesta_texto = respuesta_final.choices[0].message.content

                st.write(respuesta_texto)

                if hasattr(resultado, "to_frame") or hasattr(resultado, "columns"):
                    st.dataframe(resultado)

                st.session_state.mensajes.append(
                    {"rol": "assistant", "contenido": respuesta_texto}
                )

            except Exception as e:
                error_msg = f"No pude procesar esa pregunta. Intenta reformularla. (Error: {str(e)})"
                st.write(error_msg)
                st.session_state.mensajes.append(
                    {"rol": "assistant", "contenido": error_msg}
                )

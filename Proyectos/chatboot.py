import streamlit as st
from google import genai

client = genai.Client(api_key="-------")

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")


st.title("  Chatbot ")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "Eres un asistente útil y claro."}
    ]


user_input = st.text_input("Escribe tu mensaje", key="user_input")


def chat_gemini(messages):
    # Converti mensajes a un solo prompt de texto
    prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])

    response = client.models.generate_content(
        model="gemini-3-flash-preview",  #
        contents=prompt,
    )

    return response.text


if st.button("Enviar"):
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.spinner("Pensando..."):
            reply = chat_gemini(st.session_state.messages)

        st.session_state.messages.append({"role": "assistant", "content": reply})

# Mostrar historial
for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.markdown(f"**🧑 Tú:** {msg['content']}")
    else:
        st.markdown(f"**🤖 Gemini:** {msg['content']}")

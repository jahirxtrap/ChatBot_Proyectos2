import streamlit as st
import pickle
import os

# Configuración de la página
st.set_page_config(layout="wide", page_icon="./media/logo.png", page_title="Chatbot PT2")

# Inicialización de sesiones/variables
def initialize_session_state():
    data_dir = "./data/"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    file_path = os.path.join(data_dir, "chats")
    try:
        with open(file_path, "rb") as file:
            session_state_data = pickle.load(file)
            if "chat_history" in session_state_data:
                st.session_state.chat_history = session_state_data["chat_history"]
            if "current_chat" not in st.session_state:
                st.session_state.current_chat = 1
            if "chat_number" in session_state_data:
                st.session_state.chat_number = session_state_data["chat_number"]
    except FileNotFoundError:
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        if "current_chat" not in st.session_state:
            st.session_state.current_chat = 1
        if "chat_number" not in st.session_state:
            st.session_state.chat_number = 1

initialize_session_state()

def save_session_state():
    session_state_data = {
        "chat_history": st.session_state.chat_history,
        "chat_number": st.session_state.chat_number
    }
    with open("./data/chats", "wb") as file:
        pickle.dump(session_state_data, file)

# Respuestas del Chatbot
def get_bot_response(prompt):
    # lógica del chatbot
    # Por ahora, simplemente devolveremos una respuesta estática
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In feugiat metus risus, et mollis nunc blandit eu. Duis sit amet ligula id elit mollis commodo sed a massa. Integer rhoncus pharetra ex, non condimentum justo tempor et. Sed sed diam."

# Función para enviar mensaje
def message(chat, prompt):
    st.session_state.chat_history.append((chat, "user", prompt))
    bot_response = get_bot_response(prompt)
    st.session_state.chat_history.append((chat, "ai", bot_response))
    save_session_state()

# Barra lateral
st.sidebar.image("./media/banner.png", use_column_width=True)
st.sidebar.header("Chatbot PT2")

# Botón nuevo chat
if st.sidebar.button("Nuevo chat", use_container_width=True):
    st.session_state.chat_number += 1
    st.session_state.current_chat = st.session_state.chat_number
    save_session_state()
st.sidebar.divider()

# Historial de chats
st.sidebar.header("Historial")
for n in range(st.session_state.chat_number):
    chat_title = "Chat {}".format(n + 1)
    if st.sidebar.button(chat_title, use_container_width=True):
        st.session_state.current_chat = n + 1
st.sidebar.divider()

# Botón eliminar historial
if st.sidebar.button("Eliminar Historial", use_container_width=True):
    if os.path.exists("./data/chats"):
        st.session_state.chat_history = []
        st.session_state.chat_number = 1
        os.remove("./data/chats")
        st.experimental_rerun()
st.header("Chat {}".format(st.session_state.current_chat))
st.divider()

# Bienvenida
with st.chat_message("ai"):
    st.write("¡Hola! Soy un chatbot. ¿En qué puedo ayudarte hoy?")

# Preguntas recomendadas
col1, col2, col3 = st.columns(3)
q1 = "Pregunta 1"
q2 = "Pregunta 2"
q3 = "Pregunta 3"
st.divider()

# Entrada del usuario
user_input = st.chat_input("Mensaje Chatbot...", max_chars=100)

# Enviar mensajes
if col1.button(q1, use_container_width=True):
    message(st.session_state.current_chat, q1)
if col2.button(q2, use_container_width=True):
    message(st.session_state.current_chat, q2)
if col3.button(q3, use_container_width=True):
    message(st.session_state.current_chat, q3)
if user_input:
    message(st.session_state.current_chat, user_input)

# Mostrar mensajes
for n, sender, message in st.session_state.chat_history:
    if n == st.session_state.current_chat:
        with st.chat_message(sender):
            st.write(message)
import streamlit as st
import requests
import os
import pickle
from dotenv import load_dotenv

load_dotenv()

# Configuración de la página
st.set_page_config(layout="wide", page_icon="./media/logo.png", page_title="Asistente de Titulación UNL")

if os.path.exists(".env"):
    api_url= os.getenv('STACK_API_URL')
    auth= os.getenv('STACK_AUTH')
else:
    api_url= st.secrets['STACK_API_URL']
    auth= st.secrets['STACK_AUTH']


# API de conexión
API_URL = api_url
headers = {
    'Authorization': auth,
    'Content-Type': 'application/json'
}

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
    payload = {
        "in-0": prompt,
        "user_id": str(st.session_state.current_chat)  # Utilizando el ID de chat actual como user_id
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            # Ahora accedemos primero a 'outputs' y luego a 'out-0'
            bot_response = data['outputs']['out-0'] if 'outputs' in data and 'out-0' in data['outputs'] else "No se encontró respuesta."
            return bot_response
        else:
            return f"Error al conectar con la API: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error al procesar la respuesta: {str(e)}"

# Función para enviar mensaje
def message(chat, prompt):
    st.session_state.chat_history.append((chat, "user", prompt))
    bot_response = get_bot_response(prompt)
    st.session_state.chat_history.append((chat, "ai", bot_response))
    save_session_state()

# Barra lateral
with st.sidebar:
    st.image("./media/banner.png", use_column_width=True)
    st.header("Asistente de Titulación UNL")

    # Botón nuevo chat
    if st.button("Nuevo chat", use_container_width=True):
        st.session_state.chat_number += 1
        st.session_state.current_chat = st.session_state.chat_number
        save_session_state()
    st.divider()

    # Historial de chats
    st.header("Historial")
    for n in range(st.session_state.chat_number):
        chat_title = "Chat {}".format(n + 1)
        if st.button(chat_title, use_container_width=True):
            st.session_state.current_chat = n + 1
    st.divider()

    # Botón eliminar historial
    if st.button("Eliminar Historial", use_container_width=True):
        if os.path.exists("./data/chats"):
            st.session_state.chat_history = []
            st.session_state.chat_number = 1
            os.remove("./data/chats")
            st.rerun()

# Bienvenida
st.divider()
with st.chat_message("ai", avatar="./media/bot_icon.png"):
    st.write("Hola, soy un Bot de ayuda para consultas sobre temas de proyectos de integración curricular. ¿En qué puedo ayudarte hoy?")

# Preguntas recomendadas y entrada de usuario
col1, col2, col3 = st.columns(3)
q1 = "¿Qué es el PIS o proyectos de integración de saberes?"
q2 = "¿Cuál es el propósito de la guía para la escritura y presentación del informe del trabajo de integración curricular o de titulación?"
q3 = "¿Cuál es la estructura del proyecto de investigación de integración curricular o de titulación?"
with col1:
    if st.button(q1):
        message(st.session_state.current_chat, q1)
with col2:
    if st.button(q2):
        message(st.session_state.current_chat, q2)
with col3:
    if st.button(q3):
        message(st.session_state.current_chat, q3)

user_input = st.text_input("Escribe tu pregunta aquí...")
if st.button("Enviar"):
    if user_input:
        message(st.session_state.current_chat, user_input)

# Mostrar mensajes
st.write("Historial de chat actual:")
for n, sender, message in st.session_state.chat_history:
    if n == st.session_state.current_chat:
        if sender == "ai":
            with st.chat_message("ai", avatar="./media/bot_icon.png"):
                st.write(message)
        elif sender == "user":
            with st.chat_message("user"):
                st.write(message)

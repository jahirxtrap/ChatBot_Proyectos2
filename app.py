import streamlit as st
from judini.codegpt import CodeGPTPlus
from dotenv import load_dotenv
import random
import pickle
import os
load_dotenv()

# Configuración de la página
st.set_page_config(layout="wide", page_icon="./media/logo.png", page_title="Asistente de Titulación UNL")

# Cargar o crear directorio de datos
data_dir = "./data/"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Conectar con CodeGPT
if os.path.exists(".env"):
    api_key= os.getenv('CODEGPT_API_KEY')
    agent_id= os.getenv('CODEGPT_AGENT_ID')
    org_id= os.getenv('ORG_ID')
else:
    api_key= st.secrets['CODEGPT_API_KEY']
    agent_id= st.secrets['CODEGPT_AGENT_ID']
    org_id= st.secrets['ORG_ID']
codegpt = CodeGPTPlus(api_key=api_key, org_id=org_id)

# Recomendaciones aleatorias
def random_questions():
    try:
        with open(os.path.join(data_dir, "questions"), "rb") as file:
            lines = file.readlines()
            lines = [line.decode('utf-8').strip() for line in lines]
            random.shuffle(lines)
            return lines[:3]
    except FileNotFoundError:
        return [
            "¿Cuál es el fundamento de los proyectos de integración de saberes?",
            "¿Cuál es el propósito de la guía para la escritura y presentación del informe del trabajo de integración curricular o de titulación?",
            "¿Cuál es la estructura del proyecto de investigación de integración curricular o de titulación?"
        ]

# Inicialización de sesiones/variables
def initialize_session_state():
    try:
        with open(os.path.join(data_dir, "chats"), "rb") as file:
            session_state_data = pickle.load(file)
            if "chat_history" in session_state_data:
                st.session_state.chat_history = session_state_data["chat_history"]
            if "current_chat" not in st.session_state:
                st.session_state.current_chat = 1
            if "chat_number" in session_state_data:
                st.session_state.chat_number = session_state_data["chat_number"]
            if "questions" in session_state_data:
                st.session_state.questions = session_state_data["questions"]
    except FileNotFoundError:
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        if "current_chat" not in st.session_state:
            st.session_state.current_chat = 1
        if "chat_number" not in st.session_state:
            st.session_state.chat_number = 1
        if "questions" not in st.session_state:
            st.session_state.questions = random_questions()

initialize_session_state()

def save_session_state():
    session_state_data = {
        "chat_history": st.session_state.chat_history,
        "chat_number": st.session_state.chat_number,
        "questions": st.session_state.questions
    }
    with open("./data/chats", "wb") as file:
        pickle.dump(session_state_data, file)

# Respuestas del Chatbot
def get_bot_response(prompt):
    try:
        messages = [{"role": "user", "content": msg} for _, role, msg in st.session_state.chat_history if role == "user"]
        messages.append({"role": "user", "content": prompt})
        response_completion = codegpt.chat_completion(agent_id=agent_id, messages=messages, stream=False)
        full_response = response_completion if response_completion else "Disculpa, no pude procesar tu mensaje."
    except Exception as e:
        full_response = "Error al procesar la respuesta: {}".format(str(e))
    return full_response

# Función para mostrar mensajes
def show_messages():
    for n, sender, message in st.session_state.chat_history:
        if n == st.session_state.current_chat:
            if sender == "ai":
                st.chat_message(sender, avatar="./media/bot_icon.png").write(message)
            elif sender == "user":
                st.chat_message(sender).write(message)

# Función para enviar mensaje
def message(chat, prompt):
    st.session_state.chat_history.append((chat, "user", prompt))
    show_messages()
    bot_response = get_bot_response(prompt)
    st.session_state.chat_history.append((chat, "ai", bot_response))
    save_session_state()
    st.rerun()

# Barra lateral
with st.sidebar:
    st.image("./media/banner.png", use_column_width=True)
    st.header("Asistente de Titulación UNL")

    # Botón nuevo chat
    if st.button("Nuevo chat", use_container_width=True):
        st.session_state.chat_number += 1
        st.session_state.current_chat = st.session_state.chat_number
        st.session_state.questions = random_questions()
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

# Recomendaciones
col1, col2, col3 = st.columns(3)
st.divider()

# Entrada del usuario
user_input = st.chat_input("Mensaje Chatbot...", max_chars=500)

# Enviar mensajes
if col1.button(st.session_state.questions[0], use_container_width=True):
    message(st.session_state.current_chat, st.session_state.questions[0])
if col2.button(st.session_state.questions[1], use_container_width=True):
    message(st.session_state.current_chat, st.session_state.questions[1])
if col3.button(st.session_state.questions[2], use_container_width=True):
    message(st.session_state.current_chat, st.session_state.questions[2])
if user_input:
    message(st.session_state.current_chat, user_input)

show_messages()
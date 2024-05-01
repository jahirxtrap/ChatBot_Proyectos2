import streamlit as st

st.set_page_config(layout="wide", page_icon="./media/logo.png", page_title="Chatbot PT2")

# Sesiones/variables
def initialize_session_state():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        st.session_state.current_chat = 1
        st.session_state.chat_number = 1
initialize_session_state()

# Respuestas del Chatbot
def get_bot_response(prompt):
    # lógica del chatbot
    # Por ahora, simplemente devolveremos una respuesta estática
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In feugiat metus risus, et mollis nunc blandit eu. Duis sit amet ligula id elit mollis commodo sed a massa. Integer rhoncus pharetra ex, non condimentum justo tempor et. Sed sed diam."

# Mensaje
def message(chat, prompt):
    st.session_state.chat_history.append((chat, "user", prompt))
    bot_response = get_bot_response(prompt)
    st.session_state.chat_history.append((chat, "ai", bot_response))

# Barra lateral
st.sidebar.image("./media/banner.png", use_column_width=True)
st.sidebar.header("Chatbot PT2")
if st.sidebar.button("Nuevo chat", use_container_width=True, key="new_chat"):
    st.session_state.chat_number += 1
    st.session_state.current_chat = st.session_state.chat_number
st.sidebar.divider()
st.sidebar.header("Historial")
for n in range(st.session_state.chat_number):
    chat_title = "Chat {}".format(n + 1)
    if st.sidebar.button(chat_title, use_container_width=True):
        st.session_state.current_chat = n + 1
st.header("Chat {}".format(st.session_state.current_chat))
# Mensaje de bienvenida
with st.chat_message("ai"):
    st.write("¡Hola! Soy un chatbot. ¿En qué puedo ayudarte hoy?")
# Preguntas recomendadas
col1, col2, col3 = st.columns(3)
button_1 = "Pregunta 1"
button_2 = "Pregunta 2"
button_3 = "Pregunta 3"
st.divider()
# Entrada del usuario
user_input = st.chat_input("Mensaje Chatbot...", max_chars=100)

# Enviar mensajes
if col1.button(button_1, use_container_width=True):
    message(st.session_state.current_chat, button_1)
if col2.button(button_2, use_container_width=True):
    message(st.session_state.current_chat, button_2)
if col3.button(button_3, use_container_width=True):
    message(st.session_state.current_chat, button_3)
if user_input:
    message(st.session_state.current_chat, user_input)

# Historial
for n, sender, message in st.session_state.chat_history:
    if n == st.session_state.current_chat:
        with st.chat_message(sender):
            st.write(message)
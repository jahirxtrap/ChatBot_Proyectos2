import streamlit as st
st.set_page_config(layout="wide", page_icon="./media/logo.png", page_title="Chatbot PT2")

# Respuestas del Chatbot
def get_bot_response(prompt):
    # lógica del chatbot
    # Por ahora, simplemente devolveremos una respuesta estática
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In feugiat metus risus, et mollis nunc blandit eu. Duis sit amet ligula id elit mollis commodo sed a massa. Integer rhoncus pharetra ex, non condimentum justo tempor et. Sed sed diam."

# Mensaje
def message(prompt):
    st.session_state.chat_history.append(("user", prompt))
    bot_response = get_bot_response(prompt)
    st.session_state.chat_history.append(("ai", bot_response))

# Inicializar el estado de la sesión
def initialize_session_state():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
initialize_session_state()

# Barra lateral
st.sidebar.image("./media/banner.png", use_column_width=True)
st.sidebar.header("Chatbot PT2")
st.sidebar.button("Nuevo chat", use_container_width=True)
st.sidebar.divider()
st.sidebar.header("Historial")
st.sidebar.button("Chat 1", use_container_width=True)
st.sidebar.button("Chat 2", use_container_width=True)
st.sidebar.button("Chat 3", use_container_width=True)
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
    message(button_1)
if col2.button(button_2, use_container_width=True):
    message(button_2)
if col3.button(button_3, use_container_width=True):
    message(button_3)
if user_input:
    message(user_input)

# Historial
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.write(message)
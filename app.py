import streamlit as st

# Respuestas del Chatbot
def get_bot_response(prompt):
    # Aquí puedes poner la lógica de tu chatbot
    # Por ahora, simplemente devolveremos una respuesta estática
    return "¡Hola! Soy un chatbot. ¿En qué puedo ayudarte hoy?"

# Mensaje
def message(prompt):
    st.session_state.chat_history.append(("Tú", prompt))
    bot_response = get_bot_response(prompt)
    st.session_state.chat_history.append(("Bot", bot_response))

# Inicializar el estado de la sesión
def initialize_session_state():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
initialize_session_state()

# Título
st.title("Chatbot PT2")
# Barra lateral
st.sidebar.button("Nuevo chat +")
st.sidebar.title("Historial")
st.sidebar.button("Chat 1")
st.sidebar.button("Chat 2")
st.sidebar.button("Chat 3")
# Mensaje de bienvenida
st.write("¡Hola! Soy un chatbot. ¿En qué puedo ayudarte hoy?")
# Preguntas recomendadas
col1, col2, col3 = st.columns(3)
button_1 = "Pregunta 1"
button_2 = "Pregunta 2"
button_3 = "Pregunta 3"
# Entrada del usuario
user_input = st.chat_input("Mensaje Chatbot...")

# Enviar mensajes
if col1.button(button_1):
    message(button_1)
if col2.button(button_2):
    message(button_2)
if col3.button(button_3):
    message(button_3)
if user_input:
    message(user_input)

# Historial
for sender, message in st.session_state.chat_history:
    st.text("{}: {}".format(sender, message))
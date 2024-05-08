# Chatbot utilizando la API de Stack AI

## Requerimientos

### Instalación de Dependencias

Para instalar las dependencias necesarias, ejecute el siguiente comando:

pip install -r requirements.txt

### Configuración de las Claves de API

Para utilizar la API de Stack AI, necesitará configurar las siguientes claves de API y credenciales:

1. Cree un archivo llamado `.env` en la raíz del proyecto e incluya las siguientes variables:
   STACK_AI_API_KEY=Tu_Clave_De_API
   STACK_AI_RUN_ID=Tu_ID_De_Ejecución

   * `STACK_API_URL` es su clave de API pública para el despliegue.
   * `STACK_AUTH` es el identificador de la ejecución de la API que desea utilizar.

   Si aún no tiene las claves necesarias, puede obtenerlas registrándose en Stack AI - The Platform for Enterprise AI: https://api.stack-ai.com.

## Ejecución

Para ejecutar la aplicación, utilice el siguiente comando:

streamlit run app.py

Este comando lanzará la aplicación y estará lista para su uso en su navegador web predeterminado.

## Interacción con el Chatbot

Una vez lanzada la aplicación, interactúe con el chatbot mediante la interfaz de Streamlit. Ingrese sus preguntas en el campo de texto y el bot responderá utilizando el poder computacional de Stack AI para generar respuestas basadas en los datos proporcionados.

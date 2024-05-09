# Chatbot usando CodeGPT y StackAI API

### Requerimientos

1. Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

2. Configurar su clave de API de CodeGPT:
   * Cree un archivo llamado `.env` en la raíz del proyecto e incluya las siguientes variables:
   ```makefile
   CODEGPT_API_KEY=
   CODEGPT_AGENT_ID=
   ORG_ID=
   ```
   * Complete el archivo con su clave de API, ID de Agente e ID de Organización de CodeGPT. Si aún no tiene una, puede generarla [aquí](https://app.codegpt.co/es/apikeys).

3. Configurar su clave de API de StackAI:
   * En el archivo `.env` ubicado en la raíz del proyecto incluya las siguientes variables:
   ```makefile
   STACK_API_URL=
   STACK_AUTH=
   ```
   * Complete el archivo con su url de API y token de Autenticación de StackAI. Si aún no tiene una, puede generarla [aquí](https://www.stack-ai.com/dashboard).

### Ejecución

Para ejecutar la aplicación, utilice el siguiente comando:

```powershell
streamlit run app.py
```

Este comando lanzará la aplicación y estará lista para su uso en su navegador web predeterminado.
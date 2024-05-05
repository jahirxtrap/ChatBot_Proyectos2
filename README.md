# Chatbot usando CodeGPT API

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

### Ejecución

Para ejecutar la aplicación, utilice el siguiente comando:

```powershell
streamlit run app.py
```

Este comando lanzará la aplicación y estará lista para su uso en su navegador web predeterminado.
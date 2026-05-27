# Analytics Chatbot

Sistema de análisis inteligente de datos de países con chatbot conversacional e insights automáticos. Permite hacer preguntas en lenguaje natural sobre datos geográficos y obtener respuestas basadas en análisis automático con Pandas.

## 🎯 Descripción

**Analytics Chatbot** es una aplicación interactiva que combina la potencia de un LLM (Groq/Llama 3.3) con análisis de datos en tiempo real. El chatbot entiende preguntas en español sobre datos de países (población, ciudades, etc.) y genera automáticamente código Python con Pandas para ejecutar análisis sobre el dataset real.

### Características principales:
- 💬 **Chatbot conversacional**: Haz preguntas en lenguaje natural sobre los datos
- 🔄 **Procesamiento seguro**: Los datos nunca se mandan al LLM completos
- 📊 **Análisis automático**: El LLM genera código Pandas que se ejecuta localmente
- 💾 **Memoria conversacional**: El chatbot mantiene contexto del historial
- 📈 **Visualización de resultados**: Respuestas claras con tablas y gráficos

## 🏗️ Arquitectura

```
Usuario pregunta en lenguaje natural
    ↓
Groq (Llama 3.3 70b) genera código Pandas
    ↓
Código se ejecuta localmente contra datos
    ↓
LLM redacta respuesta clara en español
    ↓
Resultado + visualización en interfaz Streamlit
```

### Componentes:
- **Streamlit**: Interfaz visual y gestión de sesión
- **Pandas**: Análisis de datos local y transformaciones
- **Groq (Llama 3.3 70b)**: Generación de código y redacción de respuestas
- **OpenPyXL**: Lectura de archivos Excel

## 📋 Funcionalidades

### Chatbot Analytics
- ✅ Preguntas de filtrado, comparación y agregaciones
- ✅ Análisis de tendencias en datos
- ✅ Memoria conversacional
- ✅ Respuestas en lenguaje natural con tablas incrustadas
- ✅ Manejo de errores con sugerencias

**Ejemplo de preguntas:**
- "¿Cuántos países hay en el dataset?"
- "¿Cuál es la población total de América Latina?"
- "¿Cuál es el país con mayor población?"
- "¿Cuántas ciudades hay por país?"

## 🚀 Instalación y uso

### Requisitos previos
- Python 3.12+
- Clave API de Groq ([obtener aquí](https://console.groq.com))

### Instalación local

1. **Clonar o descargar el proyecto**
   ```bash
   cd Analytics_Chatbot
   ```

2. **Crear entorno virtual** (recomendado)
   ```bash
   python -m venv venv
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   Crear archivo `.env` en la raíz del proyecto:
   ```
   GROQ_API_KEY=tu_clave_api_aqui
   ```

5. **Ejecutar la aplicación**
   ```bash
   streamlit run app.py
   ```

   La aplicación se abrirá en `http://localhost:8501`

## 📦 Stack tecnológico

- **Python 3.12**: Lenguaje principal
- **Streamlit**: Framework para interfaz web interactiva
- **Pandas**: Análisis y manipulación de datos
- **Groq API**: LLM (Llama 3.3 70b) para procesamiento de lenguaje natural
- **OpenPyXL**: Lectura de archivos Excel
- **python-dotenv**: Gestión de variables de entorno

## 📊 Datos

El proyecto incluye `Latinoamerica.xlsx` con información de países:
- **Hoja**: Paises
- **Columnas**: País, Ciudad, Población
- **Filas**: Múltiples registros de países latinoamericanos

## 🔐 Flujo de seguridad

```
1. Se carga el Excel localmente (no en la nube)
2. Se envía contexto + estructura de datos al LLM (no los datos completos)
3. LLM genera código Pandas seguro
4. Código se ejecuta en el entorno local con sandbox
5. Solo el resultado se envía al LLM para redacción
```

## ⚙️ Configuración

Editar `app.py` para:
- Cambiar el archivo Excel: modificar línea `sheet_name` en `cargar_datos()`
- Personalizar columnas: actualizar `contexto_datos`
- Cambiar modelo LLM: modificar `model="llama-3.3-70b-versatile"`

## 🐛 Solución de problemas

| Problema | Solución |
|----------|----------|
| `GROQ_API_KEY not found` | Verificar que `.env` existe y contiene la clave API |
| `ModuleNotFoundError` | Ejecutar `pip install -r requirements.txt` |
| `No se pudo procesar esa pregunta` | Reformular la pregunta de forma más específica |
| `FileNotFoundError: Latinoamerica.xlsx` | Verificar que el archivo Excel esté en la raíz del proyecto |

## 📝 Ejemplo de uso

```
Usuario: "¿Cuál es la población total de todos los países?"

Chatbot:
1. Genera código: df_paises['Población'].sum()
2. Ejecuta localmente: resultado = 450,000,000
3. Redacta: "La población total de todos los países en el dataset es de 450 millones de habitantes..."
4. Muestra tabla con los datos
```

## 📄 Licencia

Proyecto educativo - Sin licencia específica

## 👤 Autor

Johany Peña Flórez

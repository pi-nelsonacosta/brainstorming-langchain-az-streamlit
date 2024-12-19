import streamlit as st
from methods.big_mind_mapping import bmm
from methods.reverse_brainstorm import rb
from methods.role_storming import rs
from methods.scamper import sc
from methods.six_hats import sh
from methods.starburtsting import sb
from langchain_openai import AzureChatOpenAI


# Configuración de página
st.set_page_config(page_title="🧠💡 Tormentas de Ideas", layout="wide")

# Sidebar for API key input
st.sidebar.title("⚙️ Configuración Azure OpenAI")

api_key = st.sidebar.text_input("Ingrese su AZURE_OPENAI_API_KEY:", type="password")
azure_deployment = st.sidebar.text_input("Ingrese su AZURE_OPENAI_DEPLOYMENT_NAME:", type="default")
azure_endpoint = st.sidebar.text_input("Ingrese su AZURE_OPENAI_ENDPOINT:", type="default")
api_version = st.sidebar.text_input("Ingrese su AZURE_OPENAI_API_VERSION:", value="2024-08-01-preview")


# Check if API key is provided
if api_key and azure_deployment and azure_endpoint and api_version:
    # Initialize the OpenAI model with the API key
    llm = AzureChatOpenAI(
        azure_deployment=azure_deployment,
        api_key=api_key,
        azure_endpoint=azure_endpoint,
        api_version=api_version
    )
    # App title and description
    st.title("🧠💡Tormentas de Ideas", icon="🧠💡")
    st.write("Welcome! ¡Bienvenido! Elija un modo de tormenta de ideas para comenzar a inspirarse en sus proyectos..")

    # Define the brainstorming modes, their corresponding functions, and descriptions
    modes = {
        "Big Mind Mapping": {
            "function": lambda query: bmm(query, llm),
            "description": "Se trata de generar un árbol de ideas para explorar la máxima cantidad de posbilidades en un área muy amplia. "
                           "Esto es perfecto cuando estás indeciso y quieres reunir el máximo número de ideas."
        },
        "Reverse Brainstorming": {
            "function": lambda query: rb(query, llm),
            "description": "En lugar de centrarse en las soluciones, esta técnica implica identificar formas de encausar un problema o "
                           "conseguir el efecto contrario. Perfecto para detectar problemas potenciales y encontrar soluciones innovadoras."
        },
        "Role Storming": {
            "function": lambda query: rs(query, llm),
            "description": "Implica adoptar la perspectiva de otra persona para generar ideas. Excelente para recopilar información desde diferentes puntos de vista."
        },
        "SCAMPER": {
            "function": lambda query: sc(query, llm),  # Pass `llm` to `sc`
            "description": "SCAMPER significa Sustituir, Combinar, Adaptar, Modificar, Implementar de otra forma, Eliminar y Revertir. "
                           "Este método fomenta el pensamiento desde múltiples perspectivas para generar diversas ideas."
        },
        "Six Thinking Hats": {
            "function": lambda query: sh(query, llm),
            "description": "Este método, desarrollado por Edward de Bono, analiza un problema desde seis perspectivas diferentes: "
                           "Blanco (Datos), Rojo (Emociones), Negro (Riesgos), Amarillo (Beneficios), Verde (Creatividad) y Azul (Gestión de procesos)."
        },
        "Starbursting": {
            "function": lambda query: sb(query, llm),
            "description": "Focuses on generating questions rather than answers using the 5 W's and 1 H (Who, What, Where, When, Why, How). "
                           "Ideal para una exploración exhaustiva de temas."
        }
    }

    # Mode selection
    mode_choice = st.selectbox("Seleccione una opción para su tormeta de ideas :", list(modes.keys()))

    # Display the description of the selected mode
    if mode_choice:
        st.write(f"**Modo seleccionado:** {mode_choice}")
        st.write(modes[mode_choice]["description"])  # Display mode description

        # User input for idea description
        user_query = st.text_area("Describe tu idea en detalle para comenzar:",
                                  "Quiero ideas de proyectos que utilicen LangChain que involucren agentes de IA y que resuelvan problemas sociales.")

        # Button to start the brainstorming process
        if st.button("Genere su idea"):
            # Display a loading message
            with st.spinner("Generando ideas, por favor espere..."):
                # Call the function for the selected mode
                result = modes[mode_choice]["function"](user_query)
            
            # Display the result in markdown format
            st.markdown(result)
else:
    # Display a message asking for the API key
    st.title("🧠 Tormentas de Ideas")
    st.write("Desbloquee métodos creativos de Tormetas de Ideas como Big Mind Mapping, SCAMPER y Role Storming para generar nuevas ideas. ¡Simplemente agregue sus claves de Azure Open AI en la barra lateral para comenzar!")

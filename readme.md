# 🧠 Tormentas de Ideas

Creada con **LangChain**, **Streamlit** y **Azure Open AI**, esta herramienta mejora su experiencia al generar ideas, porque ofrece posibilidades seleccionadas y optimizadas basadas en técnicas efectivas del mundo real. En lugar de usar ChatGPT directamente, esta aplicación le permite participar con métodos estructurados, lo que lo guíara para explorar ideas de manera integral y maximizar los beneficios de una reunion inspiradora impulsada por LLM.

Esta aplicación proporciona varias técnicas de tormentas de ideas:
- **[Big Mind Mapping](https://arxiv.org/abs/2310.19275)**: Expande las ideas en un ámbito mas general, ideal para cuando necesitas reunir la máxima cantidad de ideas.
- **[Reverse Brainstorming](https://info.orchidea.dev/innovation-blog/guide-to-ai-powered-brainstorming-sessions)**: Identifica formas de crear un problema, revelando peligros potenciales y fomentando soluciones innovadoras.
- **[Role Storming](https://www.psychologytoday.com/us/blog/the-digital-self/202403/how-ai-can-transform-brainstorming)**: Fomenta la adopción de diferentes perspectivas para recopilar conocimientos diversos.
- **[SCAMPER](https://www.interaction-design.org/literature/article/learn-how-to-use-the-best-ideation-methods-scamper)**: Aplica la técnica SCAMPER (Sustituir, Combinar, Adaptar, Modificar, Implementar de otra forma, Eliminar, Revertir) para generar ideas únicas.
- **[Six Thinking Hats](https://www.groupmap.com/portfolio/six-thinking-hats)**: Basado en el método de Edward de Bono, examina ideas desde seis ángulos: datos, emociones, riesgos, beneficios, creatividad y gestión de procesos.
- **[Starbursting](https://lucidspark.com/blog/how-to-use-starbursting-for-brainstorming)**: Genera preguntas utilizando las 5 preguntas y la 1 H (quién, qué, dónde, cuándo, por qué y cómo), ofreciendo una exploración de temas en profundidad.

## Uso

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/pi-nelsonacosta/brainstorming-langchain-az-streamlit.git
   ```
2. **Ingrese al directorio**:
   ```bash
   cd brainstormers
   ```
3. **Genere un entorno virtual y activelo**
   ```bash
   python -m venv venv 
   ```
4. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```   
5. **Ejecute la app**:
   ```bash
   streamlit run ./app.py
   ```

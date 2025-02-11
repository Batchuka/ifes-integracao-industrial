import os
import time
import streamlit as st
import streamlit.components.v1 as components

from ihm_streamlit.graphics import generate_history, generate_indicator

# Configurar o Streamlit para sempre iniciar em Wide Mode
st.set_page_config(layout="wide", page_title="Meu Dashboard", page_icon="📊")

grafico_1_base64  = generate_indicator()
grafico_2_base64  = generate_history()

# Lê o arquivo HTML
html_path = os.path.join("ihm_streamlit", "resources", "ihm.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# html_content = html_content.replace('href="styles.css"', 'href="ihm_streamlit/resources/styles.css"')
# html_content = html_content.replace('src="scripts.js"', 'src="ihm_streamlit/resources/scripts.js"')
# html_content = html_content.replace('src="" alt="Indicador Atual"', f'src="data:image/png;base64,{grafico_1_base64}" alt="Indicador Atual"')
# html_content = html_content.replace('src="" alt="Histórico da Variável"', f'src="data:image/png;base64,{grafico_2_base64}" alt="Histórico da Variável"')

# Renderiza o HTML diretamente no Streamlit
st.title("Visualização do SVG no Streamlit")
st.markdown(html_content, unsafe_allow_html=True)

# Atualização automática a cada 5 segundos
time.sleep(5)
st.rerun()

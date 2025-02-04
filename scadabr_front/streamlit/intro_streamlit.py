import streamlit as st

st.set_page_config(
    page_icon='src/python_icon.png',
    # page_icon=':house:',
    page_title='Minha Aplicação Web',
    layout='wide'
)

st.title('Minha Primeira Aplicação Usando Streamlit')

st.write('Olá Mundo!')

st.header(
    'Minha Aplicação Web',
    divider='green'
)

st.subheader('Seção 2', divider='blue')
import streamlit as st
import requests
import json


def get_endereco(cep: str) -> str:    
    url_base = 'https://viacep.com.br/ws/CEP/json/'    
    url = url_base.replace('CEP', cep)    
    response = requests.get(url)    
    json_response = response.text    
    if 'Bad Request' in json_response or 'erro' in json_response:
        return None    
    json_response = json.loads(json_response)    
    endereco = ''    
    lista_campos = [
        'logradouro', 'bairro', 'localidade', 'uf', 'cep'
    ]    
    for campo in lista_campos:        
        if campo in json_response:
            endereco += f'{json_response[campo]}, '    
    return endereco.strip()[:-1]

    
if __name__ == '__main__':
    
    st.set_page_config(
        page_icon='src/python_icon.png',
        page_title='Minha Aplicação Web',
        layout='wide')
    
    st.header('Formulário de Cadastro', divider=True)

    # Criar o formulário
    with st.form(key="form_cadastro"):
        nome = st.text_input("Nome")
        idade = st.number_input("Idade", min_value=0, max_value=100, step=1)
        cpf = st.text_input("CPF")
        cep = st.text_input("CEP")

        # Botão de envio do formulário
        submit_button = st.form_submit_button(label="Enviar")

    # Validar o formulário após o envio
    if submit_button:
        # Validação simples de CPF e CEP, por exemplo
        if len(cpf) != 11:
            st.error("CPF deve conter 11 dígitos.")
        elif len(cep) != 8:
            st.error("CEP deve conter 8 dígitos.")
        else:
            endereco = get_endereco(cep)
            st.success("Formulário enviado com sucesso!")
            st.write("**Nome:**", nome)
            st.write("**Idade:**", idade)
            st.write("**CPF:**", cpf)
            st.write("**CEP:**", cep)
            st.write("**Endereço:**", endereco)

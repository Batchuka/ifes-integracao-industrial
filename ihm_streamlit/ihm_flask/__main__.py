import os

def iniciar_streamlit():
    script_path = os.path.abspath("ihm_streamlit/app.py")
    comando = f"streamlit run {script_path} --server.address=192.168.0.118 --server.port=8501"

    print(f"Iniciando Streamlit: {comando}")
    os.system(comando)  # Executa o comando no terminal

if __name__ == "__main__":
    iniciar_streamlit()

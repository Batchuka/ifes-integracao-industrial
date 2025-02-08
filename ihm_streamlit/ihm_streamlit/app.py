import streamlit as st
import time
import random
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Monitoramento da Planta", layout="wide")

# Inicializa estados globais na primeira execução
if "bomba_status" not in st.session_state:
    st.session_state.bomba_status = False

if "blower_status" not in st.session_state:
    st.session_state.blower_status = False


def gerar_dados_variaveis():
    """Gera dados simulados para variáveis do processo."""
    return {
        "temperatura": random.randint(900, 1100),
        "pressao": round(random.uniform(18, 22), 2),
        "fluxo_gases": random.randint(40, 60),
    }


def exibir_variaveis():
    """Exibe os indicadores das variáveis do processo."""
    st.subheader("Variáveis do Processo")

    col1, col2, col3 = st.columns(3)
    variaveis = gerar_dados_variaveis()

    with col1:
        st.metric(label="🔥 Temperatura da Câmara (°C)", value=variaveis["temperatura"], delta=random.randint(-5, 5))

    with col2:
        st.metric(label="⛽ Pressão do Vapor (bar)", value=variaveis["pressao"], delta=random.uniform(-0.2, 0.2))

    with col3:
        st.metric(label="💨 Fluxo de Gases Inertes (m³/h)", value=variaveis["fluxo_gases"], delta=random.randint(-3, 3))


def atualizar_bomba():
    """Callback para alternar o estado da bomba."""
    st.session_state.bomba_status = not st.session_state.bomba_status


def atualizar_blower():
    """Callback para alternar o estado do blower."""
    st.session_state.blower_status = not st.session_state.blower_status


def exibir_controles():
    """Exibe os controles dos equipamentos e permite interagir com eles."""
    st.subheader("Controle dos Equipamentos")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Alternar Bomba de Recirculação", on_click=atualizar_bomba):
            pass
        status_bomba = "✅ Ligada" if st.session_state.bomba_status else "⛔ Desligada"
        st.info(f"Bomba de Recirculação: {status_bomba}")

    with col2:
        if st.button("Alternar Blower", on_click=atualizar_blower):
            pass
        status_blower = "✅ Ligado" if st.session_state.blower_status else "⛔ Desligado"
        st.info(f"Blower: {status_blower}")


def gerar_dados_grafico():
    """Gera dados fictícios para exibição no gráfico."""
    return pd.DataFrame({
        "Tempo": list(range(1, 11)),
        "Temperatura (°C)": [random.randint(900, 1100) for _ in range(10)]
    })


def exibir_grafico():
    """Exibe o gráfico com dados simulados."""
    st.subheader("Histórico de Temperatura")
    df = gerar_dados_grafico()
    st.line_chart(df.set_index("Tempo"))


# ---- EXECUÇÃO DA INTERFACE ---- #
st.title("Monitoramento da Planta - Sistema CDQ")
st.markdown("Simulação de variáveis do processo de resfriamento do coque usando **Streamlit**.")

exibir_variaveis()
exibir_controles()
exibir_grafico()

st.markdown("A página atualiza automaticamente a cada 5 segundos.")
time.sleep(5)
st.rerun()

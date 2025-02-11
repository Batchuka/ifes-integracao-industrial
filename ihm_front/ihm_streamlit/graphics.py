import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO

def fig_to_base64(fig):
    """Converte um gráfico Matplotlib para uma string base64."""
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode()

def generate_indicator():
    """Gera um histograma de barra única para um indicador atual."""
    valor_atual = np.random.uniform(10, 100)  # Simula um valor aleatório

    fig, ax = plt.subplots(figsize=(3, 5))
    ax.bar(["Indicador"], [valor_atual], color="#1E88E5")
    ax.set_ylim(0, 100)
    ax.set_ylabel("Valor (%)")

    return fig_to_base64(fig)

def generate_history():
    """Gera um gráfico de linha + histograma mostrando o histórico da variável."""
    tempo = np.linspace(0, 60, 20)  # Simula 20 pontos no tempo
    valores = np.sin(tempo / 10) * 40 + 50  # Simula variações na variável

    fig, ax1 = plt.subplots(figsize=(5, 3))

    # Gráfico de Linha (Histórico)
    ax1.plot(tempo, valores, color="#1E88E5", label="Histórico")
    ax1.set_xlabel("Tempo (s)")
    ax1.set_ylabel("Valor (%)")
    ax1.set_ylim(0, 100)
    ax1.grid(True)

    return fig_to_base64(fig)

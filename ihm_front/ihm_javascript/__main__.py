import matplotlib
matplotlib.use('Agg')  # Usa backend não interativo (solução para Flask)

from flask import Flask, render_template
import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO

print(f"Backend atual do Matplotlib: {matplotlib.get_backend()}")

app = Flask(__name__, static_folder="resources", template_folder="resources")

def fig_to_base64(fig):
    """Converte um gráfico Matplotlib para uma string base64."""
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode()

def generate_indicator():
    """Gera um histograma de barra única para um indicador atual."""
    valor_atual = np.random.uniform(10, 100)

    fig, ax = plt.subplots(figsize=(2, 4))
    ax.bar(["Indicador"], [valor_atual], color="#1E88E5")
    ax.set_ylim(0, 100)
    ax.set_ylabel("Valor (%)")

    return fig_to_base64(fig)

def generate_history():
    """Gera um gráfico de linha mostrando o histórico da variável."""
    tempo = np.linspace(0, 60, 20)
    valores = np.sin(tempo / 10) * 40 + 50

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(tempo, valores, color="#1E88E5", label="Histórico")
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Valor (%)")
    ax.set_ylim(0, 100)
    ax.grid(True)

    return fig_to_base64(fig)

@app.route("/")
def index():
    """Renderiza o HTML e embute os gráficos diretamente nele."""
    grafico1_base64 = generate_indicator()
    grafico2_base64 = generate_history()

    return render_template(
        "ihm.html",
        grafico1_base64=grafico1_base64,
        grafico2_base64=grafico2_base64
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
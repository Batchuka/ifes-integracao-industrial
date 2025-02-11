document.addEventListener("DOMContentLoaded", function () {
  const ctx1 = document.getElementById("grafico1").getContext("2d");
  const ctx2 = document.getElementById("grafico2").getContext("2d");
  const toggleButton = document.getElementById("toggleMode");

  let modoDesenvolvimento = true; // Começa no modo Mock

  // Atualiza o texto do botão
  function atualizarBotao() {
    toggleButton.innerText = `Modo: ${
      modoDesenvolvimento ? "Mock" : "Produção"
    }`;
  }

  toggleButton.addEventListener("click", function () {
    modoDesenvolvimento = !modoDesenvolvimento;
    atualizarBotao();
  });

  // Criar gráfico do indicador
  const indicadorChart = new Chart(ctx1, {
    type: "bar",
    data: {
      labels: ["Indicador"],
      datasets: [
        {
          label: "Valor",
          data: [Math.random() * 100], // Mock inicial
          backgroundColor: "#1E88E5",
        },
      ],
    },
    options: {
      responsive: true,
      scales: {
        y: { beginAtZero: true, max: 100 },
      },
      barThickness: 40, // Ajusta a espessura da barra para melhor visibilidade
    },
  });

  // Criar gráfico do histórico
  const historicoChart = new Chart(ctx2, {
    type: "line",
    data: {
      labels: Array.from({ length: 60 }, (_, i) => i), // Mock tempo 0-59
      datasets: [
        {
          label: "Histórico",
          data: Array.from({ length: 60 }, () => Math.random() * 100), // Mock valores
          borderColor: "#1E88E5",
          fill: false,
        },
      ],
    },
    options: {
      responsive: true,
      scales: { y: { beginAtZero: true, max: 100 } },
    },
  });

  // Função para buscar dados do indicador
  function atualizarIndicador() {
    if (modoDesenvolvimento) {
      const novoValor = Math.random() * 100;
      indicadorChart.data.datasets[0].data = [novoValor];
      indicadorChart.update();
    } else {
      fetch("http://backend_ip:8000/api/indicator") // Substitua backend_ip pelo real
        .then((response) => response.json())
        .then((data) => {
          indicadorChart.data.datasets[0].data = [data.indicador];
          indicadorChart.update();
        });
    }
  }

  // Função para buscar dados do histórico
  function atualizarHistorico() {
    if (modoDesenvolvimento) {
      const novoHistorico = Array.from(
        { length: 60 },
        () => Math.random() * 100
      );
      historicoChart.data.datasets[0].data = novoHistorico;
      historicoChart.update();
    } else {
      fetch("http://backend_ip:8000/api/history")
        .then((response) => response.json())
        .then((data) => {
          historicoChart.data.labels = data.tempo;
          historicoChart.data.datasets[0].data = data.valores;
          historicoChart.update();
        });
    }
  }

  // Atualiza os gráficos a cada 5 segundos
  setInterval(atualizarIndicador, 5000);
  setInterval(atualizarHistorico, 10000);

  atualizarBotao(); // Define o nome inicial do botão
});

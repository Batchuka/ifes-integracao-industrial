class ChartService {
  static encontrarRectNoSVG(id) {
    const elementoSVG = document.querySelector(`[data-cell-id="${id}"]`);
    if (!elementoSVG) {
      console.error(`Elemento com ID ${id} não encontrado no SVG.`);
      return null;
    }

    const rect = elementoSVG.querySelector("rect");
    if (!rect) {
      console.error(`Nenhum <rect> encontrado dentro de ${id}`);
      return null;
    }

    return rect;
  }

  static criarCanvasDentroDoSVG(id, canvasId) {
    const rect = this.encontrarRectNoSVG(id);
    if (!rect) return null;

    if (document.getElementById(canvasId)) {
      console.warn(`Canvas ${canvasId} já existe. Retornando contexto.`);
      return document.getElementById(canvasId).getContext("2d");
    }

    const foreignObject = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "foreignObject"
    );
    foreignObject.setAttribute("x", rect.getAttribute("x"));
    foreignObject.setAttribute("y", rect.getAttribute("y"));
    foreignObject.setAttribute("width", rect.getAttribute("width"));
    foreignObject.setAttribute("height", rect.getAttribute("height"));

    const div = document.createElement("div");
    div.setAttribute("xmlns", "http://www.w3.org/1999/xhtml");
    div.style.width = "100%";
    div.style.height = "100%";
    div.style.display = "flex";
    div.style.alignItems = "center";
    div.style.justifyContent = "center";

    const canvas = document.createElement("canvas");
    canvas.id = canvasId;
    canvas.width = parseInt(foreignObject.getAttribute("width"));
    canvas.height = parseInt(foreignObject.getAttribute("height"));
    div.appendChild(canvas);

    foreignObject.appendChild(div);
    rect.parentElement.appendChild(foreignObject);

    return canvas.getContext("2d");
  }

  static toggleAlertaNoSVG(id, imagemSrc = "./attention.png") {
    const rect = this.encontrarRectNoSVG(id);
    if (!rect) return;

    const elementoSVG = rect.parentElement;
    let imagem = elementoSVG.querySelector(`image[data-alerta-id="${id}"]`);

    if (imagem) {
      imagem.remove();
      console.log(`Alerta removido do ID ${id}`);
    } else {
      imagem = document.createElementNS("http://www.w3.org/2000/svg", "image");
      imagem.setAttribute("data-alerta-id", id);
      imagem.setAttribute("href", imagemSrc);
      imagem.setAttribute("x", rect.getAttribute("x"));
      imagem.setAttribute("y", rect.getAttribute("y"));
      imagem.setAttribute("width", parseFloat(rect.getAttribute("width")) / 2);
      imagem.setAttribute(
        "height",
        parseFloat(rect.getAttribute("height")) / 2
      );
      imagem.setAttribute("preserveAspectRatio", "xMidYMid meet");

      elementoSVG.appendChild(imagem);
      console.log(`Alerta adicionado ao ID ${id}`);
    }
  }

  static criarGraficoBar(ctx, label) {
    return new window.Chart(ctx, {
      type: "bar",
      data: {
        labels: [label],
        datasets: [
          {
            label: label,
            data: [Math.random() * 100], // Mock inicial (será atualizado)
            backgroundColor: "#1E88E5",
            barPercentage: 0.9, // Ocupa quase todo o espaço disponível
            categoryPercentage: 1.0, // Evita espaços laterais
          },
        ],
      },
      options: {
        indexAxis: "x", // Faz o gráfico ser VERTICAL
        responsive: false,
        maintainAspectRatio: false,
        scales: {
          x: {
            display: false, // Oculta o eixo X para não atrapalhar
          },
          y: {
            beginAtZero: true,
            max: 100, // Define o limite do nível em 100%
            ticks: { font: { size: 10 } }, // Mantém os números pequenos
            grid: {
              display: false, // Remove linhas de grade
            },
          },
        },
        plugins: {
          legend: { display: false }, // Oculta legenda
        },
      },
    });
  }

  static criarGraficoLinha(ctx, label) {
    return new window.Chart(ctx, {
      type: "line",
      data: {
        labels: ["-50 min", "-40 min", "-30 min", "-20 min", "-10 min"],
        datasets: [
          {
            label: label,
            data: [],
            borderColor: "#1E88E5",
            backgroundColor: "rgba(30, 136, 229, 0.2)",
            fill: true, // Define se a área sob a linha deve ser preenchida
            tension: 0.3, // Suaviza a linha
          },
        ],
      },
      options: {
        responsive: false,
        plugins: {
          legend: false,
        },
        scales: {
          y: {
            beginAtZero: true,
          },
          x: {
            title: { display: true, text: "Tempo (min)" },
          },
        },
      },
    });
  }

  static criarGraficoMultiAxis(ctx, label) {
    return new window.Chart(ctx, {
      type: "line",
      data: {
        labels: ["-50 min", "-40 min", "-30 min", "-20 min", "-10 min"],
        datasets: [
          { label: "Gás A", data: [], borderColor: "#555", fill: false },
          { label: "Gás B", data: [], borderColor: "#777", fill: false },
          { label: "Gás C", data: [], borderColor: "#999", fill: false },
        ],
      },
      options: {
        responsive: false,
        plugins: {
          legend: false,
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 800,
            title: { display: true, text: "Fluxo de Gases (m³/h)" },
          },
        },
      },
    });
  }

  // ATUALIZA TEMPERATURA DA CAMARA
  static atualizarTemperaturaCamara(grafico, dados) {
    if (!dados || !dados.length) return;

    const ultimoDado = dados[dados.length - 1];
    const valor = ultimoDado.temperatura_camara || 0;

    grafico.data.datasets[0].data = [valor];
    grafico.update();
  }

  // ATUALIZA HISTORICO TEMPERATURA DA CAMARA
  static atualizarHistoricoTemperaturaCamara(grafico, dados) {
    if (!dados || !dados.length) return;

    grafico.data.datasets[0].data = dados.map(
      (item) => item.temperatura_camara || 0
    );
    grafico.update();
  }

  // ATUALIZA PRESSAO VAPOR
  static atualizarPressaoVapor(grafico, dados) {
    if (!dados || !dados.length) return;

    const ultimoDado = dados[dados.length - 1];
    const valor = ultimoDado.pressao_vapor || 0;

    grafico.data.datasets[0].data = [valor];
    grafico.update();
  }

  // ATUALIZA HISTORICO PRESSAO VAPOR
  static atualizarHistoricoPressaoVapor(grafico, dados) {
    if (!dados || !dados.length) return;

    grafico.data.datasets[0].data = dados.map(
      (item) => item.pressao_vapor || 0
    );
    grafico.update();
  }

  // ATUALIZA HISTORICO FLUXO DE GASES
  static atualizarHistoricoFluxoGases(grafico, dados) {
    if (!dados || !dados.length) return;

    grafico.data.datasets[0].data = dados.map((item) => item.fluxo_gas_a || 0);
    grafico.data.datasets[1].data = dados.map((item) => item.fluxo_gas_b || 0);
    grafico.data.datasets[2].data = dados.map((item) => item.fluxo_gas_c || 0);

    grafico.update();
  }

  // ATUALIZA ALERTA BLOWER
  static atualizarAlertaBlower(alertaBlower) {
    if (!alertaBlower || !alertaBlower.length) return;

    const ultimoAlerta = alertaBlower[alertaBlower.length - 1];

    if (ultimoAlerta.alerta_blower) {
      ChartService.toggleAlertaNoSVG("uymA8mR2chiWaQQWN4nk-5");
      ChartService.toggleAlertaNoSVG("uymA8mR2chiWaQQWN4nk-6");
    }
  }

  // ATUALIZA ESTADO DOS BLOWERS
  static atualizarEstadoBlowers(nivelCarga) {
    if (nivelCarga === undefined || nivelCarga === null) return;

    const ultimoNivel = nivelCarga[nivelCarga.length - 1].nivel_carga;

    if (ultimoNivel === undefined || ultimoNivel === null) return;

    const blower1 = document.querySelector(
      `[data-cell-id="mmvXM2lkerrvPEyJ5vpn-0"] image`
    );
    const blower2 = document.querySelector(
      `[data-cell-id="m-vX1g8O2LmBPl3S4rE0-0"] image`
    );

    if (!blower1 || !blower2) return;

    // Remove a classe de rotação antes de aplicar a nova lógica
    blower1.classList.remove("ventilador-ativo");
    blower2.classList.remove("ventilador-ativo");

    if (ultimoNivel >= 1) blower1.classList.add("ventilador-ativo");
    if (ultimoNivel >= 2) blower2.classList.add("ventilador-ativo");
  }
}

export default ChartService;

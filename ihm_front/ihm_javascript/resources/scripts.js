document.addEventListener("DOMContentLoaded", function () {
  const toggleButton = document.getElementById("toggleMode");
  let modoDesenvolvimento = true; // Começa no modo Mock

  function atualizarBotao() {
    toggleButton.innerText = `Modo: ${
      modoDesenvolvimento ? "Mock" : "Produção"
    }`;
  }

  toggleButton.addEventListener("click", function () {
    modoDesenvolvimento = !modoDesenvolvimento;
    atualizarBotao();
  });

  function criarCanvasDentroDoSVG(id) {
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
    canvas.width = parseInt(foreignObject.getAttribute("width"));
    canvas.height = parseInt(foreignObject.getAttribute("height"));
    div.appendChild(canvas);

    foreignObject.appendChild(div);
    elementoSVG.appendChild(foreignObject);

    return canvas.getContext("2d");
  }

  function criarGraficoBar(ctx, label) {
    return new Chart(ctx, {
      type: "bar",
      data: {
        labels: [label],
        datasets: [
          {
            label: label,
            data: [Math.random() * 100], // Mock inicial
            backgroundColor: "#1E88E5",
          },
        ],
      },
      options: {
        responsive: false,
        scales: { y: { beginAtZero: true, max: 100 } },
      },
    });
  }

  function criarGraficoCombo(ctx, label) {
    return new Chart(ctx, {
      type: "bar",
      data: {
        labels: [label],
        datasets: [
          {
            type: "bar",
            label: "Pressão Média",
            data: [Math.random() * 100],
            backgroundColor: "#1E88E5",
          },
          {
            type: "line",
            label: "Tendência",
            data: [Math.random() * 100],
            borderColor: "#D32F2F",
            fill: false,
          },
        ],
      },
      options: {
        responsive: false,
        scales: {
          y: { beginAtZero: true, max: 100 },
        },
      },
    });
  }

  function criarGraficoMultiAxis(ctx, label) {
    return new Chart(ctx, {
      type: "line",
      data: {
        labels: ["-50 min", "-40 min", "-30 min", "-20 min", "-10 min"], // Marcações a cada 10 min
        datasets: [
          {
            label: "Gás A",
            data: [], // Os dados virão de atualizarGrafico
            borderColor: "#555", // Cinza escuro
            borderDash: [5, 5], // Linha tracejada
            pointStyle: "circle", // Marcadores circulares
            borderWidth: 1, // Linha mais fina
            fill: false,
          },
          {
            label: "Gás B",
            data: [], // Os dados virão de atualizarGrafico
            borderColor: "#777", // Cinza médio
            borderDash: [10, 5], // Linha mais espaçada
            pointStyle: "triangle", // Marcadores triangulares
            borderWidth: 1, // Linha mais fina
            fill: false,
          },
          {
            label: "Gás C",
            data: [], // Os dados virão de atualizarGrafico
            borderColor: "#999", // Cinza claro
            borderDash: [], // Linha sólida normal
            pointStyle: "rectRot", // Marcadores quadrados girados
            borderWidth: 1, // Linha mais fina
            fill: false,
          },
        ],
      },
      options: {
        responsive: false,
        scales: {
          y: {
            beginAtZero: true,
            max: 80, // Define o máximo em 80 m³/h
            title: {
              display: true,
              text: "Fluxo de Gases (m³/h)", // Ajustado para a nova unidade
            },
          },
          x: {
            title: {
              display: true,
              text: "Tempo (min)", // Nome do eixo X
            },
          },
        },
        plugins: {
          legend: {
            labels: {
              usePointStyle: true, // Usa os símbolos na legenda
            },
          },
        },
      },
    });
  }

  function atualizarGraficoMultiAxis(grafico, novosDados) {
    if (!grafico) return;

    grafico.data.datasets[0].data = novosDados.gasA; // Atualiza Gás A
    grafico.data.datasets[1].data = novosDados.gasB; // Atualiza Gás B
    grafico.data.datasets[2].data = novosDados.gasC; // Atualiza Gás C

    grafico.update();
  }

  function atualizarGrafico(grafico) {
    if (modoDesenvolvimento) {
      grafico.data.datasets[0].data = [Math.random() * 100];
      grafico.update();
    } else {
      fetch("http://backend_ip:8000/api/dados")
        .then((response) => response.json())
        .then((data) => {
          grafico.data.datasets[0].data = [data.valor];
          grafico.update();
        });
    }
  }

  function adicionarImagemNoSVG(id, imagemSrc) {
    const elementoSVG = document.querySelector(`[data-cell-id="${id}"]`);
    if (!elementoSVG) {
      console.error(`Elemento com ID ${id} não encontrado no SVG.`);
      return;
    }

    const rect = elementoSVG.querySelector("rect");
    if (!rect) {
      console.error(`Nenhum <rect> encontrado dentro de ${id}`);
      return;
    }

    // Pegar as dimensões do <rect>
    const x = parseFloat(rect.getAttribute("x"));
    const y = parseFloat(rect.getAttribute("y"));
    const width = parseFloat(rect.getAttribute("width") / 2);
    const height = parseFloat(rect.getAttribute("height") / 2);

    // Criar elemento <image>
    const imagem = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "image"
    );
    imagem.setAttribute("href", imagemSrc); // Define a imagem
    imagem.setAttribute("x", x);
    imagem.setAttribute("y", y);
    imagem.setAttribute("width", width);
    imagem.setAttribute("height", height);
    imagem.setAttribute("preserveAspectRatio", "xMidYMid meet");

    elementoSVG.appendChild(imagem);
  }

  function animarVentiladores(nivel) {
    const ventilador1 = encontrarImagemPorId("mmvXM2lkerrvPEyJ5vpn-0");
    const ventilador2 = encontrarImagemPorId("m-vX1g8O2LmBPl3S4rE0-0");
    if (!ventilador1 || !ventilador2) {
      console.error(
        "Um ou ambos os ventiladores não foram encontrados no SVG."
      );
      return;
    }

    // Controlar quais ventiladores giram baseado no nível
    girarVentilador(ventilador1, nivel >= 1);
    girarVentilador(ventilador2, nivel >= 2);

    function encontrarImagemPorId(id) {
      const elementoSVG = document.querySelector(`[data-cell-id="${id}"]`);
      if (!elementoSVG) {
        console.error(`Elemento com ID ${id} não encontrado no SVG.`);
        return null;
      }

      const imagem = elementoSVG.querySelector("image");
      if (!imagem) {
        console.error(`Nenhuma <image> encontrada dentro de ${id}`);
        return null;
      }

      return imagem;
    }

    // Função para iniciar ou parar a rotação
    function girarVentilador(imagem, ativado) {
      if (!imagem) return;

      if (ativado) {
        let angulo = 0;
        const x = parseFloat(imagem.getAttribute("x"));
        const y = parseFloat(imagem.getAttribute("y"));
        const width = parseFloat(imagem.getAttribute("width"));
        const height = parseFloat(imagem.getAttribute("height"));
        const centroX = x + width / 2;
        const centroY = y + height / 2;

        function animar() {
          if (imagem.dataset.ativo === "true") {
            angulo = (angulo + 5) % 360;
            imagem.setAttribute(
              "transform",
              `rotate(${angulo} ${centroX} ${centroY})`
            );
            requestAnimationFrame(animar);
          }
        }

        imagem.dataset.ativo = "true";
        animar();
      } else {
        imagem.dataset.ativo = "false"; // Para a rotação
      }
    }
  }

  const ctx1 = criarCanvasDentroDoSVG("uymA8mR2chiWaQQWN4nk-3"); // Temperatura da Câmara
  const ctx2 = criarCanvasDentroDoSVG("uymA8mR2chiWaQQWN4nk-4"); // Pressão do Vapor
  const ctx5 = criarCanvasDentroDoSVG("uymA8mR2chiWaQQWN4nk-7"); // Temperatura do Coque

  const grafico1 = criarGraficoBar(ctx1, "Temperatura da Câmara");
  const grafico2 = criarGraficoMultiAxis(ctx2, "Nível de Gases Inertes");
  const grafico5 = criarGraficoCombo(ctx5, "Pressão Média de Vapor");

  setInterval(() => atualizarGrafico(grafico1), 5000);
  setInterval(() => atualizarGrafico(grafico2), 5000);
  setInterval(() => atualizarGrafico(grafico5), 5000);

  animarVentiladores(2);

  adicionarImagemNoSVG("uymA8mR2chiWaQQWN4nk-5", "attention.png"); // blower 1
  adicionarImagemNoSVG("uymA8mR2chiWaQQWN4nk-6", "attention.png"); // blower 2

  atualizarBotao();
});

import MockService from "./services/mockService.js";
import ApiService from "./services/apiService.js";
import ChartService from "./services/chartService.js";

window.service = new ApiService();

document.addEventListener("DOMContentLoaded", function () {
  const toggleButton = document.getElementById("toggleMode");
  const atualizarButton = document.getElementById("atualizarDados");
  let service = new MockService();

  function atualizarBotao() {
    toggleButton.innerText = `Modo: ${
      service instanceof MockService ? "Mock" : "Produção"
    }`;
  }

  toggleButton.addEventListener("click", function () {
    service =
      service instanceof MockService ? new ApiService() : new MockService();
    atualizarBotao();
  });

  const ctx1 = ChartService.criarCanvasDentroDoSVG(
    // Temperatura da Câmara
    "uymA8mR2chiWaQQWN4nk-3",
    "temperatura-camara"
  );

  const ctx2 = ChartService.criarCanvasDentroDoSVG(
    // Histórico da Câmara
    "Z7qlt6MgUxmOc-f7Zsr3-1",
    "historico-camara"
  );

  const ctx3 = ChartService.criarCanvasDentroDoSVG(
    // Fluxo de Gases
    "uymA8mR2chiWaQQWN4nk-4",
    "fluxo-gases"
  );

  const ctx4 = ChartService.criarCanvasDentroDoSVG(
    // Pressão do Vapor
    "uymA8mR2chiWaQQWN4nk-7",
    "pressao-vapor"
  );

  const ctx5 = ChartService.criarCanvasDentroDoSVG(
    // Pressão do Vapor
    "Z7qlt6MgUxmOc-f7Zsr3-0",
    "historico-vapor"
  );

  const grafico1 = ctx1
    ? ChartService.criarGraficoBar(ctx1, "Temperatura da Câmara")
    : null;
  const grafico2 = ctx2
    ? ChartService.criarGraficoLinha(ctx2, "Histórico Temperatura")
    : null;
  const grafico3 = ctx3
    ? ChartService.criarGraficoMultiAxis(ctx3, "Histórico de Gases")
    : null;
  const grafico4 = ctx4
    ? ChartService.criarGraficoBar(ctx4, "Pressão do Vapor")
    : null;
  const grafico5 = ctx5
    ? ChartService.criarGraficoLinha(ctx5, "Histórico do Vapor")
    : null;

  async function atualizarGraficos() {
    const dados = {
      temperatura: await service.getTemperaturaCamara(),
      pressaoVapor: await service.getPressaoVapor(),
      velocidadeBlower: await service.getVelocidadeBlower(),
      nivelCarga: await service.getNivelCarga(),
      alertaBlower: await service.getAlertaBlower(),
      fluxoGases: await service.getFluxoGases(),
    };

    if (grafico1)
      //  Temperatura da Câmara
      ChartService.atualizarTemperaturaCamara(grafico1, dados.temperatura);
    if (grafico2)
      //  Histórico Temperatura
      ChartService.atualizarHistoricoTemperaturaCamara(
        grafico2,
        dados.temperatura
      );
    if (grafico3)
      // Histórico de Gases
      ChartService.atualizarHistoricoFluxoGases(grafico3, dados.fluxoGases);
    if (grafico4)
      // Pressão do Vapor
      ChartService.atualizarPressaoVapor(grafico4, dados.pressaoVapor);
    if (grafico5)
      // Histórico do Vapor
      ChartService.atualizarHistoricoPressaoVapor(grafico5, dados.pressaoVapor);

    if (dados.alertaBlower.valor) {
      // Imagem de blower obstruido
      ChartService.toggleAlertaNoSVG("uymA8mR2chiWaQQWN4nk-5");
      ChartService.toggleAlertaNoSVG("uymA8mR2chiWaQQWN4nk-6");
    }
    if (dados.nivelCarga !== undefined) {
      // ligar e desligar blowers
      ChartService.atualizarEstadoBlowers(dados.nivelCarga);
    }
  }

  atualizarButton.addEventListener("click", atualizarGraficos);
  atualizarBotao();
});

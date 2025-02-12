class MockService {
  async getTemperaturaCamara() {
    return { valor: Math.random() * 100 };
  }

  async getPressaoVapor() {
    return { valor: Math.random() * 100 };
  }

  async getVelocidadeBlower() {
    return { valor: Math.random() * 100 };
  }

  async getNivelCarga() {
    return { valor: Math.random() * 100 };
  }

  async getAlertaBlower() {
    return { valor: Math.random() > 0.5 }; // Mock booleano
  }

  async getFluxoGases() {
    return {
      gasA: [10, 20, 30, 40, 50],
      gasB: [15, 25, 35, 45, 55],
      gasC: [5, 15, 25, 35, 45],
    };
  }
}

export default MockService;

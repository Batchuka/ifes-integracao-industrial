// const backendHost = "192.168.25.7:8000";
const backendHost = "localhost:5000";

class ApiService {
  async fetchData(endpoint) {
    try {
      const response = await fetch(`http://${backendHost}${endpoint}`);
      if (!response.ok) throw new Error(`Erro ao buscar ${endpoint}`);
      return await response.json();
    } catch (error) {
      console.error("Erro ao carregar os dados:", error);
      return null;
    }
  }

  async getTemperaturaCamara() {
    return this.fetchData("/historico/temperatura_camara");
  }

  async getPressaoVapor() {
    return this.fetchData("/historico/pressao_vapor");
  }

  async getVelocidadeBlower() {
    return this.fetchData("/historico/velocidade_blower");
  }

  async getNivelCarga() {
    return this.fetchData("/historico/nivel_carga");
  }

  async getAlertaBlower() {
    return this.fetchData("/historico/alerta_blower");
  }

  async getFluxoGases() {
    return this.fetchData("/historico/fluxo_gases");
  }
}

export default ApiService;

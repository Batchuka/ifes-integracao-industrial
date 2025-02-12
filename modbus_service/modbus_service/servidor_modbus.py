import math
import time
import random
from pyModbusTCP.server import ModbusServer, DataBank

class SimuladorPlantaModbus:
    
    def __init__(self, host_ip: str, porta: int):        
        self._server = ModbusServer(host=host_ip, port=porta, no_block=True)
        self._db: DataBank = self._server.data_bank  # Banco de dados interno do Modbus
        self._t = 0  # Tempo da simulação (ciclo)
        
        # Inicializa os registradores
        self.inicializar_registradores()
    
    def inicializar_registradores(self):
        """Inicializa os valores padrão das variáveis Modbus."""
        self._db.set_holding_registers(1000, [1050])  # Temperatura da Câmara (°C)
        self._db.set_holding_registers(1001, [18])    # Pressão do Vapor (bar)
        self._db.set_holding_registers(1002, [1900])  # Fluxo de Gases Inertes (m³/h)
        self._db.set_holding_registers(1003, [1200])  # Velocidade do Blower (RPM)
        self._db.set_holding_registers(1004, [1])     # Nível de Carga (0, 1 ou 2)
        self._db.set_coils(2000, [False])             # Sinal de alerta do Blower (False = ok, True = problema)

    def atualizar_simulacao(self):
        """Atualiza variáveis para simular um comportamento cíclico e suave."""
        while True:
            self._t += 1  # Avança o tempo da simulação
            
            # Temperatura da Câmara (suave variação senoidal entre 1000 e 1100°C)
            temp_camara = 1050 + 50 * math.sin(self._t / 30)
            self._db.set_holding_registers(1000, [int(temp_camara)])

            # Pressão do Vapor (oscila suavemente entre 17 e 21 bar)
            pressao_vapor = 19 + 2 * math.sin(self._t / 40)
            self._db.set_holding_registers(1001, [int(pressao_vapor)])

            # Fluxo de Gases Inertes (muda levemente entre 1750 e 1950 m³/h)
            gases_inertes = 1850 + 100 * math.sin(self._t / 25)
            self._db.set_holding_registers(1002, [int(gases_inertes)])

            # Velocidade do Blower (flutua entre 950 e 1350 RPM)
            velocidade_blower = 1150 + 200 * math.sin(self._t / 35)
            self._db.set_holding_registers(1003, [int(velocidade_blower)])

            # Se velocidade do blower cair abaixo de 1000, aciona sinal de alerta
            sinal_alerta = velocidade_blower < 1000
            self._db.set_coils(2000, [sinal_alerta])

            # Nível de Carga na Câmara
            probabilidade = random.random()
            if probabilidade < 0.05:  # 5% das vezes, nível 0
                nivel_carga = 0
            elif probabilidade < 0.85:  # 80% das vezes, nível 1
                nivel_carga = 1
            else:  # 15% das vezes, nível 2
                nivel_carga = 2
            self._db.set_holding_registers(1004, [nivel_carga])

            # Log da simulação
            print(
                f"Temp: {int(temp_camara)}°C | Pressão: {int(pressao_vapor)} bar | "
                f"Gases: {int(gases_inertes)} m³/h | Blower: {int(velocidade_blower)} RPM | "
                f"Nível de Carga: {nivel_carga} | Alerta Blower: {sinal_alerta}"
            )

            time.sleep(2)  # Atualiza a cada 2 segundos

    def run(self):
        """Inicia o servidor Modbus e mantém a simulação ativa."""
        self._server.start()
        print('\n🔄 Simulador Modbus em Execução...')
        self.atualizar_simulacao()


if __name__ == "__main__":
    servidor = SimuladorPlantaModbus("0.0.0.0", 502)
    servidor.run()

import math
import time
import random
from pyModbusTCP.server import ModbusServer, DataBank

class SimuladorPlantaModbus:
    
    def __init__(self, host_ip: str, porta: int):        
        self._server = ModbusServer(host=host_ip, port=porta, no_block=True)
        self._db: DataBank = self._server.data_bank
        self._t = 0
        self.inicializar_registradores()
    
    def inicializar_registradores(self):
        self._db.set_holding_registers(1000, [1050])  # Temperatura da Câmara (°C)
        self._db.set_holding_registers(1001, [18])    # Pressão do Vapor (bar)
        self._db.set_holding_registers(1002, [650])   # Fluxo de Gás A (m³/h)
        self._db.set_holding_registers(1003, [600])   # Fluxo de Gás B (m³/h)
        self._db.set_holding_registers(1004, [650])   # Fluxo de Gás C (m³/h)
        self._db.set_holding_registers(1005, [1200])  # Velocidade do Blower (RPM)
        self._db.set_holding_registers(1006, [1])     # Nível de Carga (0, 1 ou 2)
        self._db.set_coils(2000, [False])             # Sinal de alerta do Blower (False = ok, True = problema)

    def atualizar_simulacao(self):
        while True:
            self._t += 1  # Avança o tempo da simulação
            
            # Temperatura da Câmara (suave variação senoidal entre 1000 e 1100°C)
            temp_camara = 1050 + 50 * math.sin(self._t / 30)
            self._db.set_holding_registers(1000, [int(temp_camara)])

            # Pressão do Vapor (oscila suavemente entre 17 e 21 bar)
            pressao_vapor = 19 + 2 * math.sin(self._t / 40)
            self._db.set_holding_registers(1001, [int(pressao_vapor)])

            # Fluxo de Gases Inertes (Gás A, B e C)
            gas_a = 600 + 80 * math.sin(self._t / 25)
            gas_b = 600 + 60 * math.sin(self._t / 20)
            gas_c = 600 + 90 * math.sin(self._t / 22)
            self._db.set_holding_registers(1002, [int(gas_a)])
            self._db.set_holding_registers(1003, [int(gas_b)])
            self._db.set_holding_registers(1004, [int(gas_c)])

            # Velocidade do Blower (flutua entre 950 e 1350 RPM)
            velocidade_blower = 1250 + 150 * math.sin(self._t / 35)
            self._db.set_holding_registers(1005, [int(velocidade_blower)])

            # Se velocidade do blower cair abaixo de 1000, aciona sinal de alerta
            alerta_blower = velocidade_blower < 1000
            self._db.set_coils(2000, [alerta_blower])

            # Nível de Carga na Câmara
            probabilidade = random.random()
            if probabilidade < 0.05:  # 5% das vezes, nível 0
                nivel_carga = 0
            elif probabilidade < 0.85:  # 80% das vezes, nível 1
                nivel_carga = 1
            else:  # 15% das vezes, nível 2
                nivel_carga = 2
            self._db.set_holding_registers(1006, [nivel_carga])

            # Log da simulação
            print(
                f"Temp: {int(temp_camara)}°C | Pressão: {int(pressao_vapor)} bar | "
                f"Gás A: {int(gas_a)} | Gás B: {int(gas_b)} | Gás C: {int(gas_c)} | "
                f"Blower: {int(velocidade_blower)} RPM | Nível: {nivel_carga} | "
                f"Alerta Blower: {alerta_blower}"
            )

            time.sleep(5)  # "Tempo de Varredura" de 5 segundos no CLP

    def run(self):
        self._server.start()
        print('\nSimulador Modbus em Execução...')
        self.atualizar_simulacao()


if __name__ == "__main__":
    servidor = SimuladorPlantaModbus("0.0.0.0", 502)
    servidor.run()

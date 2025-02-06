import random
import time
from pyModbusTCP.server import ModbusServer, DataBank

class ServidorModBus:
    
    def __init__(self, host_ip: str, porta: int):        
        self._server = ModbusServer(host=host_ip, port=porta, no_block=True)
        self._db : DataBank = self._server.data_bank  # Banco de dados interno do Modbus
        
        # Inicializa os registradores
        self.inicializar_registradores()
    
    def inicializar_registradores(self):
        """Inicializa os valores padrão das variáveis Modbus."""
        self._db.set_holding_registers(1000, [random.randint(700, 900)])  # Temperatura do forno (°C)
        self._db.set_holding_registers(1001, [random.randint(500, 850)])  # Temperatura da carga (°C)
        self._db.set_holding_registers(1002, [random.randint(0, 100)])    # Nível de gases inertes (%)
        self._db.set_holding_registers(1003, [random.randint(0, 5000)])   # Tonelagem da carga (kg)
        self._db.set_holding_registers(1004, [0])                         # Ventilador (0 = Desligado, 1 = Ligado)

    def atualizar_variaveis(self, tempo_atualizacao):
        
        """Atualiza variáveis e permite controle via Modbus."""
        while True:
            temp_forno = self._db.get_holding_registers(1000)[0] + random.randint(-5, 5)
            temp_forno = max(700, min(900, temp_forno))  
            self._db.set_holding_registers(1000, [temp_forno])

            temp_carga = self._db.get_holding_registers(1001)[0] + random.randint(-3, 3)
            temp_carga = max(500, min(850, temp_carga))
            self._db.set_holding_registers(1001, [temp_carga])

            gases_inertes = self._db.get_holding_registers(1002)[0] + random.randint(-2, 2)
            gases_inertes = max(0, min(100, gases_inertes))
            self._db.set_holding_registers(1002, [gases_inertes])

            ventilador = self._db.get_holding_registers(1004)[0]
            if temp_forno > 900:
                ventilador = 1  
            elif temp_forno < 700:
                ventilador = 0  
            self._db.set_holding_registers(1004, [ventilador])

            print(f'Temperatura: {temp_forno} °C | Carga: {temp_carga} °C | Gases: {gases_inertes}% | Ventilador: {ventilador}')
            
            time.sleep(tempo_atualizacao)

    def run(self, tempo_atualizacao=10):
        """Inicia o servidor Modbus e atualiza as variáveis periodicamente."""
        self._server.start()
        print('\nServidor Modbus em Execução...')
        self.atualizar_variaveis(tempo_atualizacao)

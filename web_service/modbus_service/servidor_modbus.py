import random
import time

from pyModbusTCP.server import ModbusServer

"""
    GitHub: https://github.com/sourceperl/pyModbusTCP
"""

class ServidorModBus:
    
    def __init__(self, host_ip: str, porta: int):        
        self._server = ModbusServer(host=host_ip, port=porta, no_block=True)
        
    
    def run(self, tempo_atualizacao: int):
        
        self._server.start()
        
        print(f'\n\nServidor ModBus em Execução ...')
        
        while True:
            
            temperatura = random.uniform(10, 40)
            umidade = random.uniform(0, 100)
            
            print(f'Temperatura: {temperatura} -- Umidade: {umidade}')
            
            self._server.data_bank.set_holding_registers(1000, [temperatura])
            self._server.data_bank.set_holding_registers(1001, [umidade])
            
            time.sleep(tempo_atualizacao)            
            
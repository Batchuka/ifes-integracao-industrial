import time

from datetime import datetime
from pyModbusTCP.client import ModbusClient
from threading import Thread


class ClienteModbus:
    
    def __init__(self, host_ip: str, porta: int, datapoints: dict, tempo_atualizacao: int):        
        self.cliente = ModbusClient(host=host_ip, port=porta)        
        self.tempo_atualizacao = tempo_atualizacao        
        self.datapoints = datapoints
        self._lista_threads = []
    
    def get_datapoints(self):
        
        print('\n\nCliente em execução ...')
        
        self.cliente.open()
        
        while True:
            
            for endereco, nome in self.datapoints.items():
                
                valor = self.cliente.read_holding_registers(endereco)
                
                data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                
                print(f'{data_hora} -- {nome} -- {valor}')
                
            time.sleep(self.tempo_atualizacao)
                
    def run(self):
        
        self._lista_threads.append(Thread(target=self.get_datapoints))
        
        for thread in self._lista_threads:            
            thread.start()
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
    
    def conectar(self):
        if not self.cliente.is_open():
            self.cliente.open()
    
    def desconectar(self):
        if self.cliente.is_open():
            self.cliente.close()
    
    def obter_variaveis(self):
        self.conectar()
        resultados = {}

        for endereco, nome in self.datapoints.items():
            valor = self.cliente.read_holding_registers(endereco)
            if valor:
                resultados[nome] = valor[0]
        
        self.desconectar()
        return resultados
    
    def obter_datapoints(self):

        print('\n\nCliente Modbus em execução ...')
        
        while True:
            
            data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            valores = self.obter_variaveis()
            
            for nome, valor in valores.items():
                print(f'{data_hora} -- {nome} -- {valor}')
            
            time.sleep(self.tempo_atualizacao)
    
    def inserir_variavel(self, endereco: int, valor: int):
        self.conectar()
        sucesso = self.cliente.write_single_register(endereco, valor)
        self.desconectar()
        return sucesso
                
    def run(self):

        self._lista_threads.append(Thread(target=self.obter_datapoints, daemon=True))
        
        for thread in self._lista_threads:            
            thread.start()

# Teste local
if __name__ == '__main__':
    
    dict_datapoints = {
        1000: 'Temperatura do forno',
        1001: 'Temperatura da carga',
        1002: 'Nível de gases inertes',
        1003: 'Tonelagem da carga',
        1004: 'Ventilador'
    }
    
    cliente = ClienteModbus(host_ip='localhost', porta=502, datapoints=dict_datapoints, tempo_atualizacao=5)
    
    cliente.run()

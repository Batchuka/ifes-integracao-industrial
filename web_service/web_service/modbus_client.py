import time
from threading import Thread
from datetime import datetime
from pyModbusTCP.client import ModbusClient
from web_service.database import BancoDeDados

dict_datapoints = {
    1000: 'Temperatura da Câmara',
    1001: 'Pressão do Vapor',
    1002: 'Fluxo de Gás A',
    1003: 'Fluxo de Gás B',
    1004: 'Fluxo de Gás C',
    1005: 'Velocidade do Blower',
    1006: 'Nível de Carga'
}

class ClienteModbus:
    
    def __init__(self, host_ip: str, porta: int, datapoints: dict = dict_datapoints, tempo_atualizacao: int = 10):        
        self.cliente = ModbusClient(host=host_ip, port=porta)        
        self.tempo_atualizacao = tempo_atualizacao        
        self.datapoints = datapoints
        self._db = BancoDeDados()

    def conectar(self):
        if not self.cliente.is_open:
            self.cliente.open()
    
    def desconectar(self):
        if self.cliente.is_open:
            self.cliente.close()
    
    def obter_variaveis(self):
        self.conectar()
        resultados = {}

        for endereco, nome in self.datapoints.items():
            valor = self.cliente.read_holding_registers(endereco)
            if valor:
                resultados[nome] = valor[0]
            else:
                resultados[nome] = "Erro na leitura"

        alerta_blower = self.cliente.read_coils(2000, 1)
        resultados["Alerta Blower"] = bool(alerta_blower[0]) if alerta_blower else "Erro"

        self.desconectar()
        return resultados
    
    def salvar_dados(self, dados):

        dados_tuple = (
            dados.get("Temperatura da Câmara"),
            dados.get("Pressão do Vapor"),
            dados.get("Fluxo de Gás A"),
            dados.get("Fluxo de Gás B"),
            dados.get("Fluxo de Gás C"),
            dados.get("Velocidade do Blower"),
            dados.get("Nível de Carga"),
            dados.get("Alerta Blower")
        )
        self._db.inserir_dados(dados_tuple)
        self._db.limpar_registros_antigos()

    def obter_datapoints(self):
        print('\nCliente Modbus em execução ...') 
        while True:
            data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            valores = self.obter_variaveis()
            self.salvar_dados(valores) 

            # for nome, valor in valores.items():
            #     print(f'{data_hora} -- {nome} -- {valor}')
            
            time.sleep(self.tempo_atualizacao)
    
    def inserir_variavel(self, endereco: int, valor: int):
        self.conectar()
        sucesso = self.cliente.write_single_register(endereco, valor)
        self.desconectar()
        return sucesso
                
    def run(self):
        thread = Thread(target=self.obter_datapoints, daemon=True)
        thread.start()

# Teste local
if __name__ == '__main__':
    
    dict_datapoints = {
        1000: 'Temperatura da Câmara',
        1001: 'Pressão do Vapor',
        1002: 'Fluxo de Gás A',
        1003: 'Fluxo de Gás B',
        1004: 'Fluxo de Gás C',
        1005: 'Velocidade do Blower',
        1006: 'Nível de Carga'
    }
    cliente = ClienteModbus(host_ip='localhost', porta=502, datapoints=dict_datapoints, tempo_atualizacao=5)
    cliente.run()

from modbus_cliente import ClienteModbus


if __name__ == '__main__':
    
    dict_datapoints = {
        1000: 'Temperatura',
        1001: 'Umidade'
    }
    
    cliente = ClienteModbus(host_ip='localhost', porta=500, datapoints=dict_datapoints, tempo_atualizacao=10)
    
    cliente.run()

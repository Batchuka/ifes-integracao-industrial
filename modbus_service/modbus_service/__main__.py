from modbus_service.servidor_modbus import ServidorModBus

if __name__ == '__main__':
    servidor = ServidorModBus(host_ip='localhost', porta=502)
    servidor.run(tempo_atualizacao=10)

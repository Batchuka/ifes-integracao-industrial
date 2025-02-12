from modbus_service.servidor_modbus import SimuladorPlantaModbus

if __name__ == '__main__':
    servidor = SimuladorPlantaModbus(host_ip='localhost', porta=502)
    servidor.run()

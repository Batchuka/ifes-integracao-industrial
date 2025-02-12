from modbus_service.servidor_modbus import SimuladorPlantaModbus

if __name__ == '__main__':
    servidor = SimuladorPlantaModbus(host_ip='0.0.0.0', porta=502)
    servidor.run()

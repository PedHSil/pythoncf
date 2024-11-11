'''pip install beamngpy
'''
from beamngpy import BeamNGpy, Scenario, Vehicle
import time

# Conectando ao BeamNG.drive
beamng = BeamNGpy('localhost', 64256)  # Porta padrão 64256
beamng.open(launch=True)

# Criando um cenário e um veículo
scenario = Scenario('smallgrid', 'test_scenario')
vehicle = Vehicle('ego_vehicle', model='etk800', licence='PYTHON', colour='Red')

# Adiciona o veículo ao cenário
scenario.add_vehicle(vehicle, pos=(0, 0, 0), rot=(0, 0, 0))
scenario.make(beamng)

# Carrega o cenário
beamng.load_scenario(scenario)
beamng.start_scenario()

# Ligar o veículo
vehicle.control(throttle=0.5, brake=0)

# Coleta dados em tempo real
try:
    for _ in range(100):  # coleta dados por um período de tempo (ajuste conforme necessário)
        sensors = vehicle.sensors.poll()  # Pega os dados do veículo

        # Obtenha dados específicos
        rpm = sensors['electrics']['rpm']
        temperature = sensors['electrics']['engine_temp']
        pressure = sensors['electrics']['oil_pressure']

        # Exibir os dados
        print(f'RPM: {rpm}, Temperatura do Motor: {temperature}, Pressão do Óleo: {pressure}')

        # Pausa entre cada coleta (ajuste conforme necessário)
        time.sleep(0.5)

finally:
    # Encerre a simulação e desconecte
    beamng.close()

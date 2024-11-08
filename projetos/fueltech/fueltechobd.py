'''pip install obd'''

import obd
import time

# Conectar ao dispositivo OBD-II (deixe `None` para detectar automaticamente)
connection = obd.OBD()  # Pode usar "obd.OBD(port)" para especificar uma porta específica

# Verifique se a conexão foi estabelecida
if not connection.is_connected():
    print("Falha ao conectar ao OBD-II")
else:
    print("Conectado ao OBD-II com sucesso!")

# Lista de comandos OBD-II para monitorar
commands = {
    "RPM": obd.commands.RPM,
    "Temperatura do Motor": obd.commands.COOLANT_TEMP,
    "Pressão do Coletor de Admissão": obd.commands.MAP
}

# Loop para leitura e exibição dos dados
try:
    while True:
        print("=== Dados do Motor ===")
        for label, cmd in commands.items():
            response = connection.query(cmd)
            if not response.is_null():
                print(f"{label}: {response.value}")
            else:
                print(f"{label}: Dados não disponíveis")

        time.sleep(1)  # Pausa de 1 segundo entre leituras
except KeyboardInterrupt:
    print("Leitura interrompida pelo usuário")
finally:
    connection.close()
    print("Conexão OBD-II encerrada.")

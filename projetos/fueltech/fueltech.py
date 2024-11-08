'''pip install matplotlib'''
import random
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import csv
from datetime import datetime

# Variáveis globais para os dados
rpm_data = []
temp_data = []
press_data = []
motor_desligado = False  # Flag para desligamento do motor por alta temperatura
target_rpm = 1500  # Valor alvo para o controle PID

# Funções para simulação de dados dos sensores
def simulate_rpm(base_rpm):
    return base_rpm + random.randint(-50, 50)

def simulate_temperature(rpm):
    if len(temp_data) == 0:
        return 70.0
    
    if rpm > 3000:
        return temp_data[-1] + random.uniform(0.5, 1.0)
    elif rpm < 1500:
        return max(temp_data[-1] - random.uniform(0.2, 0.5), 70)
    return temp_data[-1] + random.uniform(-0.2, 0.2)

def simulate_pressure(rpm):
    base_pressure = 0.8 + (rpm / 7000) * 0.5  # Pressão aumenta com o RPM, entre 0.8 e 1.3
    return max(0.5, min(base_pressure + random.uniform(-0.1, 0.1), 1.5))

# Função de controle PID para o RPM
def pid_control(current_rpm, target_rpm):
    error = target_rpm - current_rpm
    control_signal = error * 0.1
    return max(800, min(7000, current_rpm + control_signal))

# Função de atualização dos dados
def update_data():
    global rpm_data, temp_data, press_data, motor_desligado
    
    # Verifica a condição de temperatura e RPM
    if motor_desligado:
        # Se o motor está desligado, zera todos os valores
        rpm = 0
        temperature = 0
        pressure = 0
        rpm_data = [0] * 20
        temp_data = [0] * 20
        press_data = [0] * 20
        if temp_data[-1] < 100:
            motor_desligado = False  # Reativa o motor se a temperatura cair abaixo de 100°C
    else:
        # Obtém o valor do slider para o RPM alvo se o motor estiver ativo
        base_rpm = pid_control(rpm_data[-1], rpm_slider.get())
        if temp_data[-1] > 110:
            motor_desligado = True  # Desliga o motor se a temperatura exceder 110°C
            rpm = 0
            temperature = 0
            pressure = 0
            rpm_data = [0] * 20
            temp_data = [0] * 20
            press_data = [0] * 20
        else:
            # Simula os dados
            rpm = simulate_rpm(base_rpm)
            temperature = simulate_temperature(rpm)
            pressure = simulate_pressure(rpm)
            
            # Atualiza os dados de RPM, temperatura e pressão
            rpm_data.append(rpm)
            temp_data.append(temperature)
            press_data.append(pressure)
    
            # Mantém o histórico dos últimos 20 valores
            if len(rpm_data) > 20:
                rpm_data.pop(0)
            if len(temp_data) > 20:
                temp_data.pop(0)
            if len(press_data) > 20:
                press_data.pop(0)
    
    # Atualiza os gráficos
    rpm_line.set_ydata(rpm_data)
    rpm_line.set_xdata(range(len(rpm_data)))
    
    temp_line.set_ydata(temp_data)
    temp_line.set_xdata(range(len(temp_data)))
    
    press_line.set_ydata(press_data)
    press_line.set_xdata(range(len(press_data)))
    
    # Atualiza os textos dos valores atuais
    rpm_label_var.set(f"RPM Atual: {rpm}")
    temp_label_var.set(f"Temperatura: {temperature:.1f} °C")
    press_label_var.set(f"Pressão: {pressure:.2f} bar")
    
    # Verificação de limites e alertas
    if rpm >= 7000:
        rpm_label.config(fg="red")
        rpm_label_var.set("ALERTA: RPM Muito Alto!")
    else:
        rpm_label.config(fg="black")
        
    if temperature > 110:
        temp_label.config(fg="red")
        temp_label_var.set("ALERTA: Temperatura Alta - Motor Desligado!")
    elif temperature > 100:
        temp_label.config(fg="orange")
    else:
        temp_label.config(fg="black")
    
    if pressure < 0.7 or pressure > 1.3:
        press_label.config(fg="red")
    else:
        press_label.config(fg="black")

    # Salva os dados em CSV
    save_data_to_csv(rpm, temperature, pressure)
    
    # Desenha novamente o canvas
    canvas.draw()
    
    # Agenda a próxima atualização
    root.after(80, update_data)

# Função para salvar os dados em um arquivo CSV
def save_data_to_csv(rpm, temperature, pressure):
    with open("dados_motor.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), rpm, temperature, pressure])

# Configuração da interface principal com tkinter
root = tk.Tk()
root.title("FuelTech - Simulador de Monitoramento")

# Configuração do slider de controle de RPM
rpm_slider = tk.Scale(root, from_=800, to=7000, orient=tk.HORIZONTAL, label="Controle de RPM (Alvo)")
rpm_slider.set(target_rpm)
rpm_slider.pack(fill=tk.X, padx=10, pady=10)

# Criação da figura do gráfico usando matplotlib
fig = Figure(figsize=(6, 4), dpi=100)

# Gráfico de RPM
ax_rpm = fig.add_subplot(311)
ax_rpm.set_ylim(0, 8000)
ax_rpm.set_ylabel("RPM")
rpm_line, = ax_rpm.plot([], [], 'r-')

# Gráfico de Temperatura
ax_temp = fig.add_subplot(312)
ax_temp.set_ylim(60, 120)
ax_temp.set_ylabel("Temperatura (°C)")
temp_line, = ax_temp.plot([], [], 'b-')

# Gráfico de Pressão
ax_press = fig.add_subplot(313)
ax_press.set_ylim(0.5, 1.5)
ax_press.set_ylabel("Pressão (bar)")
press_line, = ax_press.plot([], [], 'g-')

# Integra o gráfico ao tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Labels para exibir os valores atuais
rpm_label_var = tk.StringVar()
temp_label_var = tk.StringVar()
press_label_var = tk.StringVar()

rpm_label = tk.Label(root, textvariable=rpm_label_var, font=("Arial", 12))
temp_label = tk.Label(root, textvariable=temp_label_var, font=("Arial", 12))
press_label = tk.Label(root, textvariable=press_label_var, font=("Arial", 12))

rpm_label.pack()
temp_label.pack()
press_label.pack()

# Inicializa os dados com valores padrão para evitar erro ao acessar o último elemento
initial_rpm = rpm_slider.get()
rpm_data = [initial_rpm] * 20
temp_data = [70.0] * 20  # Temperatura inicial de 70°C
press_data = [simulate_pressure(initial_rpm) for _ in range(20)]

# Inicia a atualização dos dados
update_data()

root.mainloop()

'''pip install matplotlib'''
import random
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import csv
from datetime import datetime
import time

# Variáveis globais para controle
target_rpm = 1500
reativacao_delay = 5000  # Tempo de espera em milissegundos para reativação
ultimo_desligamento = None
motor_desligado = False
historico_limite = 20
intervalo_atualizacao = 80

# Classe para simulação de sensores e controle do motor
class MotorSimulator:
    def __init__(self):
        self.rpm_data = [800] * historico_limite
        self.temp_data = [70.0] * historico_limite
        self.press_data = [1.0] * historico_limite

    def simulate_rpm(self, base_rpm):
        return base_rpm + random.randint(-50, 50)

    def simulate_temperature(self, rpm):
        if rpm > 3000:
            return self.temp_data[-1] + random.uniform(0.5, 1.0)
        elif rpm < 1500:
            return max(self.temp_data[-1] - random.uniform(0.2, 0.5), 70)
        return self.temp_data[-1] + random.uniform(-0.2, 0.2)

    def simulate_pressure(self, rpm):
        base_pressure = 0.8 + (rpm / 7000) * 0.5
        return max(0.5, min(base_pressure + random.uniform(-0.1, 0.1), 1.5))

    def update_data(self, base_rpm):
        rpm = self.simulate_rpm(base_rpm)
        temperature = self.simulate_temperature(rpm)
        pressure = self.simulate_pressure(rpm)
        
        self.rpm_data.append(rpm)
        self.temp_data.append(temperature)
        self.press_data.append(pressure)

        if len(self.rpm_data) > historico_limite:
            self.rpm_data.pop(0)
        if len(self.temp_data) > historico_limite:
            self.temp_data.pop(0)
        if len(self.press_data) > historico_limite:
            self.press_data.pop(0)

        return rpm, temperature, pressure

# Funções de controle do motor e segurança
def pid_control(current_rpm, target_rpm):
    error = target_rpm - current_rpm
    control_signal = error * 0.15
    return max(800, min(7000, current_rpm + control_signal))

def check_safety_conditions(temperature):
    global motor_desligado, ultimo_desligamento
    if temperature > 110:
        motor_desligado = True
        ultimo_desligamento = time.time()
        return True
    elif temperature < 100 and motor_desligado and (time.time() - ultimo_desligamento) * 1000 > reativacao_delay:
        motor_desligado = False
    return False

# Atualização da interface e exibição
def update_data():
    global motor_simulator, motor_desligado

    check_safety_conditions(motor_simulator.temp_data[-1])

    if motor_desligado:
        update_display(0, 0, 0, alert="Motor desligado devido a temperatura alta")
    else:
        base_rpm = pid_control(motor_simulator.rpm_data[-1], rpm_slider.get())
        rpm, temperature, pressure = motor_simulator.update_data(base_rpm)
        update_display(rpm, temperature, pressure)

    # Verifica se os dados estão prontos para serem desenhados no gráfico
    if len(motor_simulator.rpm_data) == historico_limite:
        rpm_line.set_ydata(motor_simulator.rpm_data)
        temp_line.set_ydata(motor_simulator.temp_data)
        press_line.set_ydata(motor_simulator.press_data)
        canvas.draw()

    root.after(intervalo_atualizacao, update_data)

def update_display(rpm, temperature, pressure, alert=""):
    rpm_label_var.set(f"RPM Atual: {rpm}")
    temp_label_var.set(f"Temperatura: {temperature:.1f} °C")
    press_label_var.set(f"Pressão: {pressure:.2f} bar")

    # Alertas e cores
    rpm_label.config(fg="red" if rpm >= 7000 else "black")
    temp_label.config(fg="red" if temperature > 110 else "orange" if temperature > 100 else "black")
    press_label.config(fg="red" if pressure < 0.7 or pressure > 1.3 else "black")

    # Barra de progresso para temperatura
    temp_gauge["value"] = temperature
    temp_gauge["maximum"] = 120

    motor_status_label_var.set("Motor Ligado" if not motor_desligado else "Motor Desligado")
    motor_status_label.config(fg="green" if not motor_desligado else "red")

    if alert:
        log_list.insert(tk.END, f"{datetime.now().strftime('%H:%M:%S')}: {alert}")
        log_list.yview(tk.END)

    save_data_to_csv(rpm, temperature, pressure)

def save_data_to_csv(rpm, temperature, pressure):
    with open("dados_motor.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), rpm, temperature, pressure])

# Configuração da interface principal com tkinter
root = tk.Tk()
root.title("FuelTech - Simulador de Monitoramento")

motor_simulator = MotorSimulator()

rpm_slider = tk.Scale(root, from_=800, to=7000, orient=tk.HORIZONTAL, label="Controle de RPM (Alvo)")
rpm_slider.set(target_rpm)
rpm_slider.pack(fill=tk.X, padx=10, pady=10)

# Gráfico
fig = Figure(figsize=(6, 4), dpi=100)
ax_rpm = fig.add_subplot(311)
ax_temp = fig.add_subplot(312)
ax_press = fig.add_subplot(313)
for ax, label, ylim in zip((ax_rpm, ax_temp, ax_press), ("RPM", "Temperatura (°C)", "Pressão (bar)"), ((0, 8000), (60, 120), (0.5, 1.5))):
    ax.set_ylim(ylim)
    ax.set_ylabel(label)

rpm_line, = ax_rpm.plot(range(historico_limite), motor_simulator.rpm_data, 'r-')
temp_line, = ax_temp.plot(range(historico_limite), motor_simulator.temp_data, 'b-')
press_line, = ax_press.plot(range(historico_limite), motor_simulator.press_data, 'g-')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Labels para exibir os valores atuais
rpm_label_var = tk.StringVar()
temp_label_var = tk.StringVar()
press_label_var = tk.StringVar()
motor_status_label_var = tk.StringVar()

rpm_label = tk.Label(root, textvariable=rpm_label_var, font=("Arial", 12))
temp_label = tk.Label(root, textvariable=temp_label_var, font=("Arial", 12))
press_label = tk.Label(root, textvariable=press_label_var, font=("Arial", 12))
motor_status_label = tk.Label(root, textvariable=motor_status_label_var, font=("Arial", 14, "bold"))

rpm_label.pack()
temp_label.pack()
press_label.pack()
motor_status_label.pack(pady=10)

# Barra de progresso de temperatura
temp_gauge = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
temp_gauge.pack(pady=10)

# Log de eventos
log_list = tk.Listbox(root, height=5, width=50)
log_list.pack(pady=10)
log_list.insert(tk.END, "Log de Eventos:")

# Inicializa dados com valores padrão
initial_rpm = rpm_slider.get()
motor_simulator.rpm_data = [initial_rpm] * historico_limite
motor_simulator.temp_data = [70.0] * historico_limite
motor_simulator.press_data = [1.0] * historico_limite

root.after(intervalo_atualizacao, update_data)
root.mainloop()

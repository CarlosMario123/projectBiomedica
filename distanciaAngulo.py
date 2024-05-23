from mpu6050 import mpu6050
import time
import RPi.GPIO as GPIO

# Inicialización del objeto mpu para el sensor giroscopio
mpu = mpu6050(0x68)

# Configuración inicial del sensor de distancia
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# TRIG = 23
# ECHO = 24
TRIG = 27
ECHO = 22
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def leer_giroscopio():
    accel_data = mpu.get_accel_data()
    x_value = int(accel_data['x'])
    z_value = int(accel_data['z'])

    # Cálculo de ángulos a partir de los datos del giroscopio
    if x_value > 0 and z_value < 0:
        Angulorestado = 90 - (x_value * 10)
        Angulo90a180 = 90 + Angulorestado
        return Angulo90a180
    elif x_value < 0 and z_value < 0:
        Angulosumado = (x_value * 10) * (-1)
        Angulo180a270 = 180 + Angulosumado
        return Angulo180a270
    elif x_value < 0 and z_value > 0:
        Anguloresultante = 90 + (x_value * 10)
        Angulo270a360 = Anguloresultante + 270
        return Angulo270a360
    else:
        return x_value * 10

def leer_distancia():
    GPIO.output(TRIG, False)
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

while True:
    # Leer y calcular los valores
    angulo_giroscopio = leer_giroscopio()
    distancia_cm = leer_distancia()

    # Imprimir los resultados
    print(f"Ángulo del Giroscopio: {angulo_giroscopio}°")
    print(f"Distancia: {distancia_cm} cm")

    # Esperar un minuto antes de la próxima lectura
    time.sleep(30)
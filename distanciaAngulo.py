from mpu6050 import mpu6050
import time
import RPi.GPIO as GPIO

# Inicialización del objeto mpu para el sensor giroscopio
mpu = mpu6050(0x68)

# Configuración inicial del sensor de distancia
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 23
ECHO = 24
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
    time.sleep(60)


# 1. Importa las bibliotecas necesarias: mpu6050 para el sensor MPU6050, time para las funciones de tiempo, y RPi.GPIO para interactuar con los pines GPIO de la Raspberry Pi.

# 2. Inicializa el sensor MPU6050 en la dirección I2C 0x68.

# 3. Configura los pines GPIO para el sensor de distancia. El pin TRIG se configura como salida y el pin ECHO como entrada.

# 4. Define la función leer_giroscopio(), que lee los datos del acelerómetro del MPU6050 y calcula el ángulo basado en los valores de los ejes X y Z. El ángulo calculado depende del cuadrante en el que se encuentren los valores de X y Z.

# 5. Define la función leer_distancia(), que utiliza los pines TRIG y ECHO para medir la distancia. Envía un pulso corto en el pin TRIG y luego mide el tiempo que tarda en recibir el eco en el pin ECHO. Este tiempo se convierte en una distancia en centímetros.

# 6. Entra en un bucle infinito donde lee y calcula los valores del giroscopio y la distancia, los imprime y luego espera un minuto antes de repetir el proceso.
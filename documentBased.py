from mpu6050 import mpu6050
import time
import RPi.GPIO as GPIO
import sqlite3

# Inicialización del objeto mpu para el sensor giroscopio
mpu = mpu6050(0x68)

# Configuración inicial del sensor de distancia
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Configuración inicial del sensor de presión (ejemplo)
SENSOR_PRESION = 25
GPIO.setup(SENSOR_PRESION, GPIO.IN)

# Inicialización de la base de datos SQLite3
conn = sqlite3.connect('postura_conductor.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS postura (
                timestamp TEXT,
                angulo_giroscopio INTEGER,
                distancia_cm REAL,
                presencia BOOLEAN,
                recomendacion TEXT
            )''')
conn.commit()

def leer_giroscopio():
    accel_data = mpu.get_accel_data()
    x_value = int(accel_data['x'])
    z_value = int(accel_data['z'])

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

def leer_presion():
    return GPIO.input(SENSOR_PRESION)

def recomendar_postura(angulo, distancia, presencia):
    if angulo < 90:
        if distancia > 5:
            return "Ajustar asiento con su cuerpo"
        else:
            return "Se recomienda una postura menos erguida, un poco más acostado"
    elif 90 <= angulo <= 110:
        if distancia > 5:
            return "Ajustar asiento con su cuerpo"
        else:
            return "Se recomienda mantener la postura adoptada"
    else:
        return "Se recomienda adoptar una postura menos exigente para la espalda"

while True:
    # Leer y calcular los valores
    angulo_giroscopio = leer_giroscopio()
    distancia_cm = leer_distancia()
    presencia = leer_presion()
    
    # Generar recomendación
    recomendacion = recomendar_postura(angulo_giroscopio, distancia_cm, presencia)

    # Guardar en la base de datos
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO postura (timestamp, angulo_giroscopio, distancia_cm, presencia, recomendacion) VALUES (?, ?, ?, ?, ?)",
              (timestamp, angulo_giroscopio, distancia_cm, presencia, recomendacion))
    conn.commit()

    # Imprimir los resultados
    print(f"Ángulo del Giroscopio: {angulo_giroscopio}°")
    print(f"Distancia: {distancia_cm} cm")
    print(f"Presencia: {'Sí' if presencia else 'No'}")
    print(f"Recomendación: {recomendacion}")

    # Esperar 30 minutos antes de la próxima lectura
    time.sleep(1800)

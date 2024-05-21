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

# Creación de tablas si no existen
c.execute('''CREATE TABLE IF NOT EXISTS postura_temp (
                timestamp TEXT,
                angulo_giroscopio INTEGER,
                distancia_cm REAL,
                presencia BOOLEAN
            )''')
c.execute('''CREATE TABLE IF NOT EXISTS postura_promediada (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_chofer INTEGER,
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
createTables()
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

def promediar_datos():
    c.execute("SELECT AVG(angulo_giroscopio), AVG(distancia_cm), AVG(presencia) FROM postura_temp")
    result = c.fetchone()
    return result

id_chofer = 1

while True:
    for _ in range(60):
        # Leer y calcular los valores
        angulo_giroscopio = leer_giroscopio()
        distancia_cm = leer_distancia()
        presencia = leer_presion()

        # Guardar en la tabla temporal
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO postura_temp (timestamp, angulo_giroscopio, distancia_cm, presencia) VALUES (?, ?, ?, ?)",
                  (timestamp, angulo_giroscopio, distancia_cm, presencia))
        conn.commit()

        # Esperar 30 segundos antes de la próxima lectura
        time.sleep(30)
    
    # Promediar datos cada 30 minutos
    angulo_promedio, distancia_promedio, presencia_promedio = promediar_datos()
    presencia_promedio = bool(round(presencia_promedio))

    # Generar recomendación
    recomendacion = recomendar_postura(angulo_promedio, distancia_promedio, presencia_promedio)

    # Guardar los datos promediados en la tabla final
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO postura_promediada (id_chofer, timestamp, angulo_giroscopio, distancia_cm, presencia, recomendacion) VALUES (?, ?, ?, ?, ?, ?)",
              (id_chofer, timestamp, angulo_promedio, distancia_promedio, presencia_promedio, recomendacion))
    conn.commit()

    # Limpiar la tabla temporal
    c.execute("DELETE FROM postura_temp")
    conn.commit()

    # Imprimir los resultados
    print(f"Ángulo del Giroscopio Promediado: {angulo_promedio}°")
    print(f"Distancia Promediada: {distancia_promedio} cm")
    print(f"Presencia Promediada: {'Sí' if presencia_promedio else 'No'}")
    print(f"Recomendación: {recomendacion}")

    # Esperar 30 minutos antes de la próxima recolección y procesamiento de datos
    time.sleep(1800)

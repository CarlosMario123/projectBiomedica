import time
from mpu6050 import mpu6050
import RPi.GPIO as GPIO
from bd.datos_postura.getAvgPostura import obtener_promedio_postura
from bd.datos_postura.addTempPostura import agregar_postura_temporal
from bd.datos_postura.saveAvgPostura import agregar_postura_promediada
from bd.datos_postura.cleanTemp import limpiar_postura_temp

class ContextPostura:
    _instance = None
    mpu = mpu6050(0x68)
    TRIG = 23
    ECHO = 24
    SENSOR_PRESION = 25

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)
        GPIO.setup(self.SENSOR_PRESION, GPIO.IN)

    @staticmethod
    def get_instance():
        if ContextPostura._instance is None:
            ContextPostura._instance = ContextPostura()
        return ContextPostura._instance

    def leer_giroscopio(self):
        accel_data = self.mpu.get_accel_data()
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

    def leer_distancia(self):
        GPIO.output(self.TRIG, False)
        time.sleep(2)

        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)

        while GPIO.input(self.ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(self.ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        return distance

    def leer_presion(self):
        return GPIO.input(self.SENSOR_PRESION)

    def recomendar_postura(self, angulo, distancia):
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

    def insert_postura_temp(self, timestamp, angulo_giroscopio, distancia_cm, presencia):
        agregar_postura_temporal(timestamp, angulo_giroscopio, distancia_cm, presencia)

    def promediar_datos(self):
        return obtener_promedio_postura()

    def insert_postura_promediada(self, id_chofer, timestamp, angulo_promedio, distancia_promedio, presencia_promedio, recomendacion):
        agregar_postura_promediada(id_chofer, timestamp, angulo_promedio, distancia_promedio, presencia_promedio, recomendacion)

    def limpiar_postura_temp(self):
        limpiar_postura_temp()

    def procesar_datos(self):
        id_chofer = 1
        while True:
            for _ in range(60):
                angulo_giroscopio = self.leer_giroscopio()
                distancia_cm = self.leer_distancia()
                presencia = self.leer_presion()
                
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                self.insert_postura_temp(timestamp, angulo_giroscopio, distancia_cm, presencia)
                
                time.sleep(30)
            
            angulo_promedio, distancia_promedio, presencia_promedio = self.promediar_datos()
            presencia_promedio = bool(round(presencia_promedio))
            
            recomendacion = self.recomendar_postura(angulo_promedio, distancia_promedio)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            self.insert_postura_promediada(id_chofer, timestamp, angulo_promedio, distancia_promedio, presencia_promedio, recomendacion)
            
            self.limpiar_postura_temp()
            
            print(f"Ángulo del Giroscopio Promediado: {angulo_promedio}°")
            print(f"Distancia Promediada: {distancia_promedio} cm")
            print(f"Presencia Promediada: {'Sí' if presencia_promedio else 'No'}")
            print(f"Recomendación: {recomendacion}")
            
            time.sleep(1800)
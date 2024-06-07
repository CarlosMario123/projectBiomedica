import threading
import time
from mpu6050 import mpu6050
import RPi.GPIO as GPIO
from bd.datos_postura.getAvgPostura import obtener_promedio_postura
from bd.datos_postura.addTempPostura import agregar_postura_temporal
from bd.datos_postura.saveAvgPostura import agregar_postura_promediada
from bd.datos_postura.cleanTemp import limpiar_postura_temp
from bd.datos_postura.getLastPosturas import obtener_ultimas_posturas_promediadas
from src.context.contextChofer import ContextChofer
from src.utils.serialReader import SerialReader
class ContextPostura:
    _instance = None
    mpu = mpu6050(0x68)
    TRIG1 = 23
    ECHO1 = 24
    TRIG2 = 27
    ECHO2 = 22
    SENSOR_PRESION = 25
    presenciaSen = SerialReader('/dev/ttyUSB0')
    presenciaValue = 0
   
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.TRIG1, GPIO.OUT)
        GPIO.setup(self.ECHO1, GPIO.IN)
        GPIO.setup(self.TRIG2, GPIO.OUT)
        GPIO.setup(self.ECHO2, GPIO.IN)
        GPIO.setup(self.SENSOR_PRESION, GPIO.IN)
        self.alert_callback = None  # Callback para alertar al controlador
        self.update_callback = None
        self.presenciaSen.start_reading(self.callBackPresencia)
    @staticmethod
    def get_instance():
        if ContextPostura._instance is None:
            ContextPostura._instance = ContextPostura()
        return ContextPostura._instance
    
    def callBackPresencia(self,data):
        if(data =='Golpe detectado!'):
            print('no hay presencia')
            self.presenciaValue = False
        else:
            print('hubo presencia')
            self.presenciaValue = True

    def set_alert_callback(self, callback):
        self.alert_callback = callback

    def set_update_callback(self, callback):
        self.update_callback = callback

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

    def leer_distancia(self, trig, echo):
        GPIO.output(trig, False)
        time.sleep(2)

        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        while GPIO.input(echo) == 0:
            pulse_start = time.time()

        while GPIO.input(echo) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        return distance

    def leer_distancias(self):
        distancia1 = self.leer_distancia(self.TRIG1, self.ECHO1)
        distancia2 = self.leer_distancia(self.TRIG2, self.ECHO2)
        distancia_promedio = (distancia1 + distancia2) / 2
        return distancia_promedio

    def leer_presion(self):
        return self.presenciaValue

    def recomendar_postura(self, angulo, distancia):
        if angulo < 90:
            if distancia > 5:
                return "Ajustar asiento con su cuerpo y mantener una postura menos erguida, un poco más acostado"
            else:
                return "Se recomienda una postura menos erguida, un poco más acostado"
        elif 90 <= angulo <= 110:
            if distancia > 5:
                return "Ajustar asiento con su cuerpo y mantener la postura adoptada"
            else:
                return "Se recomienda mantener la postura adoptada"
        else:
            return "Se recomienda adoptar una postura menos exigente para la espalda"

    def obtener_recomendacion_id(self, recomendacion):
        if recomendacion == "Se recomienda una postura menos erguida, un poco más acostado":
            return 1
        elif recomendacion == "Se recomienda mantener la postura adoptada":
            return 2
        elif recomendacion == "Se recomienda adoptar una postura menos exigente para la espalda":
            return 3
        elif recomendacion == "Ajustar asiento con su cuerpo y mantener una postura menos erguida, un poco más acostado":
            return 4
        elif recomendacion == "Ajustar asiento con su cuerpo y mantener la postura adoptada":
            return 5

    def obtener_promedio_ultimas_posturas(self):
        # ultimas_posturas = obtener_ultimas_posturas_promediadas(10)
        ultimas_posturas = obtener_ultimas_posturas_promediadas(2)
        # en testing se obtienen las ultimas 2 posturas
        if not ultimas_posturas:
            return None, None, None  # Manejar el caso donde no hay suficientes datos
        
        sum_angulo = sum(postura['angulo_giroscopio'] for postura in ultimas_posturas)
        sum_distancia = sum(postura['distancia_cm'] for postura in ultimas_posturas)
        sum_presencia = sum(postura['presencia'] for postura in ultimas_posturas)
        
        count = len(ultimas_posturas)
        angulo_promedio = sum_angulo / count
        distancia_promedio = sum_distancia / count
        presencia_promedio = sum_presencia / count

        return angulo_promedio, distancia_promedio, presencia_promedio

    def insert_postura_temp(self, timestamp, angulo_giroscopio, distancia_cm, presencia):
        agregar_postura_temporal(timestamp, angulo_giroscopio, distancia_cm, presencia)

    def promediar_datos(self):
        return obtener_promedio_postura()

    def insert_postura_promediada(self, id_chofer, timestamp, angulo_promedio, distancia_promedio, presencia_promedio, recomendacion):
        agregar_postura_promediada(id_chofer, timestamp, angulo_promedio, distancia_promedio, presencia_promedio, recomendacion)

    def limpiar_postura_temp(self):
        limpiar_postura_temp()

    def procesar_datos(self):
        inicio_horas = time.time()
        while True:
            id_chofer = ContextChofer.get_instance().get_chofer_id()
            if id_chofer is None:
                print("Esperando la selección del chofer...")
                time.sleep(5)
                continue

            # Recolección y procesamiento de datos
            # for _ in range(60):
            for _ in range(2):
                angulo_giroscopio = self.leer_giroscopio()
                distancia_cm = self.leer_distancias()
                presencia = self.leer_presion()

                distancia1 = self.leer_distancia(self.TRIG1, self.ECHO1)
                distancia2 = self.leer_distancia(self.TRIG2, self.ECHO2)
                
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                self.insert_postura_temp(timestamp, angulo_giroscopio, distancia_cm, presencia)

                if self.update_callback:
                    self.update_callback(angulo_giroscopio, distancia1, distancia2, presencia)
                
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
            
            # Comprobar si han pasado 5 horas (18000 segundos)
            # se agregaron 60 segundos para evitar algun desfase
            # if time.time() - inicio_horas >= 18060:
            if time.time() - inicio_horas >= 90:
                inicio_horas = time.time()  # Reiniciar el contador
                angulo_promedio, distancia_promedio, presencia_promedio = self.obtener_promedio_ultimas_posturas()
                if angulo_promedio is not None:
                    recomendacion = self.recomendar_postura(angulo_promedio, distancia_promedio)
                    recomendacion_id = self.obtener_recomendacion_id(recomendacion)
                    if self.alert_callback:
                        self.alert_callback(recomendacion_id)
            
            # time.sleep(1800)
            time.sleep(60)
# en testing los tiempo son de: guardar promedio cada 60 segundos
# y alertar cada 90 segundos
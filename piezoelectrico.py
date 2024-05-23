import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import digitalio

# Definir los números de pin GPIO para los pines SCL y SDA del bus 4
PIN_GPIO_29 = 29  # GPIO5
PIN_GPIO_31 = 31  # GPIO6

# Crear un objeto GPIO para el pin SCL del bus 4
scl_pin_4 = digitalio.DigitalInOut(PIN_GPIO_29)
# Crear un objeto GPIO para el pin SDA del bus 4
sda_pin_4 = digitalio.DigitalInOut(PIN_GPIO_31)

# Obtener los números de los pines GPIO
scl_pin_num_4 = scl_pin_4._pin
sda_pin_num_4 = sda_pin_4._pin

# Crear bus I2C para el bus 4 usando los números de los pines GPIO
i2c_4 = busio.I2C(scl_pin_num_4, sda_pin_num_4)

# Direcciones I2C para el ADS1115 en cada bus
addresses = [0x48, 0x68]  # Direcciones posibles para el ADS1115

# Intentar inicializar un objeto ADS1115 para cada dirección en el bus 4
ads_4 = None
for address in addresses:
    try:
        ads_4 = ADS.ADS1115(i2c_4, address=address)
        print(f"ADS1115 encontrado en la dirección: {hex(address)} en el bus 4")
        break
    except ValueError:
        print(f"No se encontró el ADS1115 en la dirección: {hex(address)} en el bus 4")

if ads_4 is None:
    raise RuntimeError("No se pudo encontrar un ADS1115 en ninguna dirección I2C en el bus 4")

# Crear objeto para la entrada AIN0 en el bus 4
chan0_4 = AnalogIn(ads_4, ADS.P0)

# Voltaje de tolerancia
tolerancia = 0.1  # Ajusta este valor según tus necesidades

def verificar_presencia(chan0):
    lectura0 = chan0.voltage
    print(f"Lectura0: {lectura0}")

    return lectura0 > tolerancia

while True:
    presencia_4 = verificar_presencia(chan0_4)
    print(f"Presencia en bus 4: {presencia_4}")
    time.sleep(1)

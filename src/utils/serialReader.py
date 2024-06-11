import serial
import time
import threading

class SerialReader:
    def __init__(self, port, baud_rate=9600, timeout=1):
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.ser = None
        self._connect()
        self.running = False
        self.thread = None
        self.callback = None

    def _connect(self):
        """Inicializa la conexi�n serial."""
        self.ser = serial.Serial(self.port, self.baud_rate, timeout=self.timeout)
        time.sleep(2)  # Espera a que la conexi�n serial se establezca
        print("Conexi�n establecida en el puerto:", self.port)

    def read_data(self):
        """Lee datos del puerto serial si est�n disponibles."""
        if self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').rstrip()
            return line
        return None

    def start_reading(self, callback):
        """Inicia la lectura de datos en un hilo separado."""
        self.callback = callback
        self.running = True
        self.thread = threading.Thread(target=self._read_loop)
        self.thread.start()

    def _read_loop(self):
        """Bucle de lectura de datos en el hilo separado."""
        while self.running:
            data = self.read_data()
            if data and self.callback:
                self.callback(data)
            time.sleep(0.1)  # Peque�a espera para no saturar el hilo

    def stop_reading(self):
        """Detiene la lectura de datos."""
        self.running = False
        if self.thread:
            self.thread.join()

    def close(self):
        """Cierra la conexi�n serial."""
        self.stop_reading()
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Puerto serial cerrado.")

    def __del__(self):
        """Asegura que la conexi�n serial se cierre al destruir el objeto."""
        self.close()
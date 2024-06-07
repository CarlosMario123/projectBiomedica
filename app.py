from src.controller.inicioController import InicioController
from src.controller.choiseDriveController import ChoiseDriverController
from src.controller.RecorridoController import RecorridoController
from bd.CreateTables import createTables
from src.context.contextPostura import ContextPostura
import tkinter as tk
import threading

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Viaje seguro")
<<<<<<< HEAD
        self.geometry("1024x768")
=======
        self.geometry("1200x625")
>>>>>>> main
        self.vistas = {}  # las vistas se gestionan por claves y controladores
        self.principal = None
    
    def addFrame(self, controlador, clave):
        controlador_instance = controlador(root=self)
        self.vistas[clave] = controlador_instance
        return controlador_instance  # Devolver la instancia del controlador
        
    def asignarPrincipal(self, clave):
        self.principal = self.vistas[clave]
        self.principal.getView()
    
    def run(self):
        self.mainloop()
        
    def cambiarVista(self, clave):
        for clave1 in self.vistas:
            if clave != clave1:
                self.vistas[clave1].hide()
        self.principal = self.vistas[clave]
        self.principal.getView()

# Datos iniciales de la BD
createTables()

app = Main()
app.addFrame(controlador=InicioController, clave="inicio")
app.addFrame(controlador=ChoiseDriverController, clave="choiseD")
recorrido_controller = app.addFrame(controlador=RecorridoController, clave="recorrido")
app.asignarPrincipal("inicio")

# Iniciar procesamiento de datos de postura en un hilo separado
context_postura = ContextPostura.get_instance()
context_postura.limpiar_postura_temp()  # Limpiar datos temporales al iniciar
context_postura.set_alert_callback(recorrido_controller.recibir_alerta)
thread = threading.Thread(target=context_postura.procesar_datos)
thread.daemon = True
thread.start()

app.run()
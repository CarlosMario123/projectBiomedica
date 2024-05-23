#definiremos una clase principal
import os
from src.controller.inicioController import InicioController
from src.controller.choiseDriveController import ChoiseDriverController
from src.controller.RecorridoController import RecorridoController

#todo relacionado con sqlite
from bd.chofer.addChofer import llenarChoferes
from bd.CreateTables import createTables
import tkinter as tk

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Viaje seguro")
        self.geometry("900x600")
        self.vistas = {} #las vistas se gestionan por claves y controladores
        self.principal = None
    
    
    def addFrame(self,controlador,clave):
        self.vistas[clave] = controlador(root=self)
        
    def asignarPrincipal(self,clave):
        self.principal = self.vistas[clave]
        self.principal.getView()
        
    
    def run(self):
        self.mainloop()
        
    def cambiarVista(self,clave):
        
        for clave1 in self.vistas:
            if clave != clave1:
                self.vistas[clave1].hide()
                
        self.principal = self.vistas[clave]
        self.principal.getView()

# Establecer la variable de entorno DISPLAY
os.environ["DISPLAY"] = ":0"

# Datos iniciales de la bd
createTables()
# llenarChoferes()

app = Main()
app.addFrame(controlador=InicioController,clave="inicio")
app.addFrame(controlador=ChoiseDriverController,clave="choiseD")
app.addFrame(controlador=RecorridoController,clave="recorrido")
app.asignarPrincipal("inicio")

app.run()
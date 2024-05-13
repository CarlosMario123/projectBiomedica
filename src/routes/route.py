from src.view.ControllerView import ControllerView
from src.controller.inicioController import InicioController
from src.controller.choiseDriveController import ChoiseDriverController

class Route():
    def __init__(self):
        self.routes = {#routes se definen todas la vistas de la app pero se les asigna un clave para micers
        "inicio":InicioController,
        "driver":ChoiseDriverController
        }
        self.controllerView = ControllerView()        
        
    def moveTo(self,ruta:str,msg = None):
        self.controllerView.change_view(self.routes[ruta](route=self).getView(msg=msg))
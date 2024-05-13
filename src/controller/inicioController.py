from src.view.frames.inicio import InicioView

class InicioController():
    def __init__(self,route = None):
        self.view =  None
        self.router = route
        
    def getView(self,msg = None):
        self.view = InicioView(controller=self)
        return self.view
        
    
    def redirectDrivers(self):
       
        self.router.moveTo("driver")
        
from src.view.frames.inicio import InicioView

class InicioController():
    def __init__(self,root):
        self.root = root
        self.view = InicioView(master=root,controller=self)
        
    def getView(self):#muestra el frame
        self.view.show()
    
    def hide(self):#cierra el frame
        self.view.hide() 
        
    def redirectDrivers(self):
        print("entro")
        self.root.cambiarVista("choiseD")  

        
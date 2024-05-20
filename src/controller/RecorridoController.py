from src.view.frames.recorridoFrame import RecorridoFrame
class RecorridoController():
    def __init__(self,root):
        self.root = root
        self.view = RecorridoFrame(controller=self,master=root)
        
    def getView(self):#muestra el frame
        self.view.show()
    
    def hide(self):#cierra el frame
        self.view.hide() 
    
    def regresarInicio(self):
        self.root.cambiarVista("choiseD")
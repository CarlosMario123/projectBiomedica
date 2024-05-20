from src.view.frames.ChoiseDriver import ChoiseDriverView
from bd.chofer.getChofer import obtener_choferes
class ChoiseDriverController():
    def __init__(self,root):
        self.view = ChoiseDriverView(master=root,controller=self)
        self.root = root
    
    def obtener_choferes(self):
        return obtener_choferes()
    
    def getView(self):
        self.view.show()
        
    def hide(self):
        self.view.hide()
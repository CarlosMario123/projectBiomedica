from src.view.frames.ChoiseDriver import ChoiseDriverView
from src.context.contextChofer import ContextChofer
from bd.getChofer import obtener_choferes
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
        
    def selectionOptions(self,text):
        context = ContextChofer()
        #el nombre del chofer lo guardamos en nuestro contexto guardado para que sea accessible desde otra vista
        context.name_chofer = text
        self.root.cambiarVista("recorrido")
        
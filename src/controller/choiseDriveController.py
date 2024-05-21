from src.view.frames.ChoiseDriver import ChoiseDriverView
from bd.chofer.getChofer import obtener_choferes
from src.context.contextChofer import ContextChofer
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
        ContextChofer().get_instance().set_name_chofer(text)
        print(ContextChofer().get_instance().get_name_chofer())
        self.root.cambiarVista("recorrido")
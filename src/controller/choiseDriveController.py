from src.view.frames.ChoiseDriver import ChoiseDriverView
class ChoiseDriverController():
    def __init__(self,root):
        self.view = ChoiseDriverView(master=root,controller=self)
        self.root = root
    
    def getView(self):
        self.view.show()
        
    def hide(self):#cierra el frame
        self.view.hide()
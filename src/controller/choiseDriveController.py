from src.view.frames.ChoiseDriver import ChoiseDriverView
class ChoiseDriverController():
    def __init__(self,route = None):
        self.view =  None
        self.router = route
    
    def getView(self,msg = None):
        self.view = ChoiseDriverView(controller=self)
        return self.view
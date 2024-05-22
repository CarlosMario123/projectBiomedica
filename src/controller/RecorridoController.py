from src.view.frames.recorridoFrame import RecorridoFrame
class RecorridoController():
    def __init__(self,root):
        self.root = root
        self.view = RecorridoFrame(controller=self,master=root)
        self.execute2()
        self.mostrando = False
        
    def getView(self):#muestra el frame
        self.mostrando = True
        self.view.show()
    
    def hide(self):#cierra el frame
        self.mostrando = False
        self.view.hide() 
    
    def regresarInicio(self):
<<<<<<< HEAD
        self.root.cambiarVista("choiseD")
=======
        self.root.cambiarVista("choiseD")
    
    def execute2(self):
        self.view.after(5000,self.comando)
        
    
    def comando(self):
        if self.mostrando:
            self.view.abrir_ventana()
            print("ventana abierta")
        self.execute2() 
             
>>>>>>> carlos

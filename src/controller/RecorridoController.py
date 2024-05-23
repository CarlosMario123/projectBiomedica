from src.view.frames.recorridoFrame import RecorridoFrame
class RecorridoController():
    def __init__(self,root):
        self.root = root
        self.view = RecorridoFrame(controller=self, master=root)
        self.execute2()
        self.mostrando = False

    def getView(self):
        self.mostrando = True
        self.view.show()
    
    def hide(self):
        self.mostrando = False
        self.view.hide() 
    
    def regresarInicio(self):
        self.root.cambiarVista("choiseD")

    def execute2(self):
        self.view.after(5000, self.comando)
    
    # def comando(self):
    #     if self.mostrando:
    #         self.view.abrir_ventana(random.randint(1, 3))  # Para testeo
    #         print("ventana abierta")
    #     self.execute2()

    def recibir_alerta(self, id_recomendacion):
        if self.mostrando:
            self.view.abrir_ventana(id_recomendacion)
            print(f"Alerta enviada con recomendación ID: {id_recomendacion}")
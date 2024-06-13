from src.view.frames.recorridoFrame import RecorridoFrame
class RecorridoController:
    def __init__(self, root, base_dir):
        self.root = root
        self.view = RecorridoFrame(controller=self, master=root, base_dir=base_dir)
        self.mostrando = False

    def getView(self):
        self.mostrando = True
        self.view.show()

    def hide(self):
        self.mostrando = False
        self.view.hide()

    def regresarInicio(self):
        self.root.cambiarVista("choiseD")

    def recibir_alerta(self, id_recomendacion):
        if self.mostrando:
            self.view.abrir_ventana(id_recomendacion)
            print(f"Alerta enviada con recomendación ID: {id_recomendacion}")

    def actualizar_datos_sensores(self, angulo, distancia1, distancia2, presencia):
        if self.mostrando:
            self.view.actualizar_datos_sensores(angulo, distancia1, distancia2, presencia)
from src.view.frames.ChoiseDriver import ChoiseDriverView
from bd.chofer.getChofer import obtener_choferes
from src.context.contextChofer import ContextChofer

class ChoiseDriverController:
    def __init__(self, root):
        self.view = ChoiseDriverView(master=root, controller=self)
        self.root = root

    def obtener_choferes(self):
        return obtener_choferes()

    def getView(self):
        self.view.show()

    def hide(self):
        self.view.hide()

    def selectionOptions(self, chofer_name):
        # Obtener el ID del chofer seleccionado
        choferes = self.obtener_choferes()
        chofer_id = next((id for id, name in choferes if name == chofer_name), None)

        # Almacenar el ID del chofer en ContextChofer
        ContextChofer.get_instance().set_chofer_id(chofer_id)
        print(f"Chofer seleccionado: {ContextChofer.get_instance().get_chofer_id()}")

        # Cambiar a la vista de recorrido
        self.root.cambiarVista("recorrido")

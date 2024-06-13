from src.view.frames.ChoiseDriver import ChoiseDriverView
from bd.chofer.getChofer import obtener_choferes
from src.context.contextChofer import ContextChofer

class ChoiseDriverController:
    def __init__(self, root, base_dir):
        self.view = ChoiseDriverView(master=root, controller=self, base_dir=base_dir)
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
        chofer_id = next((id_chofer for id_chofer, name in choferes if name == chofer_name), None)

        # Almacenar el ID y el nombre del chofer en ContextChofer
        context_chofer = ContextChofer.get_instance()
        context_chofer.set_chofer_id(chofer_id)
        context_chofer.set_name_chofer(chofer_name)
        print(f"Chofer seleccionado: {context_chofer.get_chofer_id()}")

        # Cambiar a la vista de recorrido
        self.root.cambiarVista("recorrido")

class ContextChofer:
    _instance = None
    _name_chofer = ""
    _chofer_id = None

    @staticmethod
    def get_instance():
        if ContextChofer._instance is None:
            ContextChofer._instance = ContextChofer()
        return ContextChofer._instance

    def get_name_chofer(self):
        return self._name_chofer

    def set_name_chofer(self, value):
        self._name_chofer = value

    def get_chofer_id(self):
        return self._chofer_id

    def set_chofer_id(self, value):
        self._chofer_id = value
class ContextChofer:
    _instance = None
    _name_chofer = ""

    @staticmethod
    def get_instance():
        if ContextChofer._instance is None:
            ContextChofer._instance = ContextChofer()
        return ContextChofer._instance

    @staticmethod
    def get_name_chofer():
        return ContextChofer._name_chofer

    @staticmethod
    def set_name_chofer(value):
        ContextChofer._name_chofer = value


class ContextChofer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._name_chofer = None
        return cls._instance

    @property
    def name_chofer(self):
        return self._name_chofer

    @name_chofer.setter
    def name_chofer(self, value):
        self._name_chofer = value

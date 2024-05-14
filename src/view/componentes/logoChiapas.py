import tkinter as tk

class LogoChiapas(tk.Label):
    # Atributo de clase para mantener la instancia única
    _instance = None
    # Atributo de clase para mantener la referencia a la imagen
    image = None

    def __new__(cls, master=None, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.init_singleton(master, **kwargs)
        return cls._instance

    def init_singleton(self, master=None, **kwargs):
        tk.Label.__init__(self, master, **kwargs)
        self.place(x=670, y=400)
        self.doConfig()

    def doConfig(self):
        file = "img/chiapas.png"
        
        # Asignar la imagen al atributo de clase
        if not LogoChiapas.image:
            LogoChiapas.image = tk.PhotoImage(file=file)
        
        self.config(image=LogoChiapas.image)
    
    def editPosition(self, x1, y1):
        self.place(x=x1, y=y1)
    
    @staticmethod
    def get_instance(master=None):
        if not LogoChiapas._instance:
            LogoChiapas._instance = LogoChiapas(master)
        return LogoChiapas._instance

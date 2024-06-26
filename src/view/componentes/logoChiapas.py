import tkinter as tk

class LogoChiapas(tk.Label):
    _instance = None
    image = None

    def __new__(cls, master=None, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.init_singleton(master, **kwargs)
        return cls._instance

    def init_singleton(self, master=None, **kwargs):
        tk.Label.__init__(self, master, **kwargs)
        self.master.bind("<Configure>", self.on_resize)
        self.doConfig()

    def doConfig(self):
        file = "img/chiapas.png"
        
        if not LogoChiapas.image:
            LogoChiapas.image = tk.PhotoImage(file=file)
        
        self.config(image=LogoChiapas.image, bg="#F6F5FB")
        self.update_position()

    def update_position(self):
        if self.master:
            window_width = 1200
            window_height = 630
            image_width = LogoChiapas.image.width()
            image_height = LogoChiapas.image.height()
            x = window_width - image_width - 10  # margen de 10 píxeles desde el borde derecho
            y = window_height - image_height - 10  # margen de 10 píxeles desde el borde inferior
            self.place(x=x, y=y)

    def on_resize(self, event):
        self.update_position()

    @staticmethod
    def get_instance(master=None):
        if not LogoChiapas._instance:
            LogoChiapas._instance = LogoChiapas(master)
        return LogoChiapas._instance

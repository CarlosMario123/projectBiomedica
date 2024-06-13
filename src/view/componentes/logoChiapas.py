import tkinter as tk
import os

class LogoChiapas(tk.Label):
    _instance = None
    image = None

    def __new__(cls, master=None, base_dir=None, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.init_singleton(master, base_dir, **kwargs)
        return cls._instance

    def init_singleton(self, master=None, base_dir=None, **kwargs):
        tk.Label.__init__(self, master, **kwargs)
        self.master.bind("<Configure>", self.on_resize)
        self.base_dir = base_dir
        self.doConfig()

    def doConfig(self):
        file = os.path.join(self.base_dir, "img/chiapas.png")
        
        if not LogoChiapas.image:
            LogoChiapas.image = tk.PhotoImage(file=file)
        
        self.config(image=LogoChiapas.image, bg="#F6F5FB")
        self.update_position()

    def update_position(self):
        if self.master:
            window_width = self.master.winfo_width()
            window_height = self.master.winfo_height()
            image_width = LogoChiapas.image.width()
            image_height = LogoChiapas.image.height()
            x = window_width - image_width - 10  # margen de 10 píxeles desde el borde derecho
            y = window_height - image_height - 10  # margen de 10 píxeles desde el borde inferior
            self.place(x=x, y=y)

    def on_resize(self, event):
        self.update_position()

    @staticmethod
    def get_instance(master=None, base_dir=None, **kwargs):
        if not LogoChiapas._instance:
            LogoChiapas._instance = LogoChiapas(master, base_dir=base_dir, **kwargs)
        return LogoChiapas._instance
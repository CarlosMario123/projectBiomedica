import tkinter as tk
from src.context.contextChofer import ContextChofer
import time

class RecorridoFrame(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.cronometro = 0
        self.nameChofer = ""
        self.running = True
        self.init_ui()

    def init_ui(self):
        self.nameChofer = ContextChofer().name_chofer
        self.label1 = tk.Label(self, text=f"Bienvenido: {self.nameChofer}", font=("", 18, "bold"), height=3)
        self.label1.pack()
    
        self.label2 = tk.Label(self, text=f"Tiempo de viaje trancurrido {self.cronometro}", font=("", 14, "bold"), height=4, width=300)
        self.label2.pack()
        
        self.label3 = tk.Label(self, text="¿ No es usted cancelar recorrido ?", font=("", 16, "bold"))
        self.label3.pack()
        self.label2.after(1000, self.changeCronometro)
        
    def show(self):
        self.pack(fill=tk.BOTH, expand=True) 
    
    def hide(self):
        self.pack_forget()
        
    def changeCronometro(self):
        if self.running:
            self.cronometro += 1
            self.label2.config(text=f"Tiempo de viaje trancurrido {self.cronometro}")
            self.label2.after(2000, self.changeCronometro)

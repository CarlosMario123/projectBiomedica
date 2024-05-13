import tkinter as tk
class ChoiseDriverView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("")
        self.geometry("900x600")
        self.controller = controller
        self.init_ui()
        
    def init_ui(self):
        self.label1 = tk.Label(self, text="Elige el operador", font=("", 18, "bold"))
        self.label1.place(x=350, y=1)

        
    
        
        
    
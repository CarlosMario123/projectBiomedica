import tkinter as tk
from src.view.componentes.logoChiapas import LogoChiapas

class ChoiseDriverView(tk.Frame):
    def __init__(self,master, controller):
        super().__init__(master)
        self.controller = controller
        self.image2 = None
        self.init_ui()
        
    def init_ui(self):
        self.logoChiapa = LogoChiapas().get_instance(master=self)
        self.label1 = tk.Label(self, text="Elige el operador", font=("", 18, "bold"))
        self.label1.place(x=350, y=1)
        self.sectionBtn1()
        self.sectionBtn2()
       
        
        
    def sectionBtn1(self):
        self.btns1 = []
        incremento = 20
        for i in range(4):
            btn = tk.Button(self, text=f"Conductor {i+1}", height=4, width=15, font=("", 12, "bold"))
            btn.configure(command=lambda text=f"Conductor {i+1}": self.actionBtn(text))
            btn.place(x=incremento, y=160)
            incremento += 220
            self.btns1.append(btn)
            
    def sectionBtn2(self):
        self.btns2 = []
        incremento = 20
        for i in range(4):
            btn = tk.Button(self, text=f"Conductor {i+5}", height=4, width=15, font=("", 12, "bold"))
            btn.configure(command=lambda text=f"Conductor {i+5}": self.actionBtn(text))
            btn.place(x=incremento, y=300)
            incremento += 220
            self.btns2.append(btn)
    
    def show(self):
        self.pack(fill=tk.BOTH, expand=True) 
        
    def hide(self):
        self.pack_forget()
        
    def actionBtn(self,text):
        self.controller.selectionOptions(text)    
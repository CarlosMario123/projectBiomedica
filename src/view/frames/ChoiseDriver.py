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
        choferes = self.controller.obtener_choferes()  # Obtén los nombres de los choferes
        for i in range(4):
            self.btns1.append(tk.Button(self, text=choferes[i], height=4, width=15, font=("", 12, "bold"))) 
            self.btns1[i].place(x=incremento, y=160)
            incremento += 220

    def sectionBtn2(self):
        self.btns2 = []
        incremento = 20
        choferes = self.controller.obtener_choferes()  # Obtén los nombres de los choferes
        for i in range(4, 8):
            self.btns2.append(tk.Button(self, text=choferes[i], height=4, width=15, font=("", 12, "bold"))) 
            self.btns2[len(self.btns2) - 1].place(x=incremento, y=300)
            incremento += 220
    
    def show(self):
        self.pack(fill=tk.BOTH, expand=True) 
        
    def hide(self):
        self.pack_forget()    
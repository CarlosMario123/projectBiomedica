import tkinter as tk
class InicioView(tk.Frame):
    def __init__(self,master, controller):
        super().__init__(master)
        self.controller = controller
        self.init_ui()
        self.after(1000,self.btnAnimate)#evento para prolongar eventos a un tiempo especifico


    def init_ui(self):
        #self.logo = LogoChiapas()
        self.label1 = tk.Label(self, text="Maneje con preocupación y sin distracciones", font=("", 18, "bold"), width=40, height=5)
        self.label1.place(x=300, y=1)

        self.label2 = tk.Label(self, text="¡Feliz viaje!", font=("", 16, "bold"))
        self.label2.place(x=550,y=100)
        
        
    def btnAnimate(self):
        self.btn = tk.Button(text="iniciar recorrido", font=("", 18, "bold"),bg="#3DDE19",fg="white")
        self.btn.place(x=350,y=500,width=200,height=50)
        self.btn.config(command=self.controller.redirectDrivers)
    
    def show(self):
        self.pack(fill=tk.BOTH, expand=True) 
        
    def hide(self):
        self.pack_forget()
  

        
        
        
        
        
        
 
        
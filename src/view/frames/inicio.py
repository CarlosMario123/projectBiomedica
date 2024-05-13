import tkinter as tk

class InicioView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("")
        self.geometry("900x600")
        self.controller = controller
        self.init_ui()
        self.after(1000,self.btnAnimate)#evento para prolongar eventos a un tiempo especifico

    def init_ui(self):
        self.label1 = tk.Label(self, text="Maneje con preocupación y sin distracciones", font=("", 18, "bold"), width=40, height=5)
        self.label1.place(x=300, y=1)

        self.label2 = tk.Label(self, text="¡Feliz viaje!", font=("", 16, "bold"))
        self.label2.place(x=550,y=100)
        self.insertImg()
        
        
    def btnAnimate(self):
        self.btn = tk.Button(text="iniciar recorrido", font=("", 18, "bold"),bg="#3DDE19",fg="white")
        self.btn.place(x=350,y=500,width=200,height=50)
        self.btn.config(command=self.controller.redirectDrivers)
        
    def insertImg(self):
        file = "img/chiapas.png"
        self.image = tk.PhotoImage(file=file)
        label_image = tk.Label(self, image=self.image)
        label_image.place(x=670, y=400)
        
        
        
        
        
        
 
        
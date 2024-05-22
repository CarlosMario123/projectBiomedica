import tkinter as tk
from PIL import Image, ImageTk

class InicioView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.init_ui()
        self.after(1000, self.btnAnimate)  # evento para prolongar eventos a un tiempo especifico

    def init_ui(self):
      
        self.addBackgroudImage()
        self.addLogos()
        self.label1 = tk.Label(self, text="Maneje con preocupación y sin distracciones", font=("", 18, "bold"), width=40, height=5)
        self.label1.place(x=300, y=1)

        self.label2 = tk.Label(self, text="¡Feliz viaje!", font=("", 16, "bold"))
        self.label2.place(x=550, y=100)
     

    def btnAnimate(self):
        self.btn = tk.Button(self, text="Iniciar recorrido", font=("", 18, "bold"), bg="#3DDE19", fg="white")
        self.btn.place(x=350, y=500, width=200, height=50)
        self.btn.config(command=self.controller.redirectDrivers)

    def show(self):
        self.init_ui()
        self.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.btn.destroy()
        self.pack_forget()

    def addBackgroudImage(self):
        self.img = Image.open("img/fondo.png")
        self.img = self.img.resize((400, 300), Image.LANCZOS)
        self.imgtk = ImageTk.PhotoImage(self.img)

        # Crear un Label con la imagen y centrarla
        label_img = tk.Label(self, image=self.imgtk)
        label_img.place(x=-250, y=-220, relwidth=1, relheight=1)
        
    def addLogos(self):
        self.img1 = Image.open("img/rs.jpeg")
        self.img1 = self.img1.resize((70, 70), Image.LANCZOS)
        self.imgtk1 = ImageTk.PhotoImage(self.img1)

        self.img2 = Image.open("img/ado.jpeg")
        self.img2 = self.img2.resize((70, 70), Image.LANCZOS)
        self.imgtk2 = ImageTk.PhotoImage(self.img2)

        # Crear Labels para los logos
        label_logo1 = tk.Label(self, image=self.imgtk1)
        label_logo2 = tk.Label(self, image=self.imgtk2)

        # Obtener el tamaño de la ventana y las imágenes
        window_height = 600  # Altura de la ventana
        logo_height = 80   # Altura de los logotipos

        # Calcular la posición y colocar los logos en la parte inferior izquierda
        label_logo1.place(x=10, y=window_height - logo_height - 10)  # Ajusta las coordenadas según sea necesario
        label_logo2.place(x=120, y=window_height - logo_height - 10)  # Ajusta las coordenadas según sea necesario
        
        
    
        

  

        
        
        
        
        
        
 
        
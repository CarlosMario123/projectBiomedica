import tkinter as tk
from PIL import Image, ImageTk

class InicioView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#F6F5FB")
        self.controller = controller
        self.init_ui()
        self.after(1000, self.btnAnimate)  # evento para prolongar eventos a un tiempo especifico

    def init_ui(self):
      
        self.addBackgroudImage()
        self.addLogos()
        self.label1 = tk.Label(self, text="Monitoreo de Postura para Conducción de Vehículos de Transporte Público de Ruta Prolongada", font=("", 10, "bold"), bg="#F6F5FB", fg="black")
        self.label1.place(x=400, y=10)

    def btnAnimate(self):
        self.btn = tk.Button(self, text="INICIAR RECORRIDO", font=("", 15, "bold"), bg="#90EE90", fg="black")
        self.btn.place(x=450, y=300, width=380, height=180)
        self.btn.config(command=self.controller.redirectDrivers)

    def show(self):
        self.init_ui()
        self.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.btn.destroy()
        self.pack_forget()

    def addBackgroudImage(self):
        self.img = Image.open("img/fondo.png")
        self.img = self.img.resize((490, 380), Image.LANCZOS)
        self.imgtk = ImageTk.PhotoImage(self.img)

        # Crear un Label con la imagen y centrarla
        label_img = tk.Label(self, image=self.imgtk, bg="#F6F5FB")
        label_img.place(x=-1, y=-1)

        self.img2 = Image.open("img/project91.png")
        self.img2 = self.img2.resize((750, 210), Image.LANCZOS)
        self.imgtk2 = ImageTk.PhotoImage(self.img2)

        # Crear un Label con la imagen y centrarla
        label_img2 = tk.Label(self, image=self.imgtk2)
        label_img2.place(x=400, y=50)
        
    def addLogos(self):
        self.logo1 = Image.open("img/rs.jpeg")
        self.logo1 = self.logo1.resize((70, 70), Image.LANCZOS)
        self.logotk1 = ImageTk.PhotoImage(self.logo1)

        self.logo2 = Image.open("img/ado.jpeg")
        self.logo2 = self.logo2.resize((70, 70), Image.LANCZOS)
        self.logotk2 = ImageTk.PhotoImage(self.logo2)

        # Crear Labels para los logos
        label_logo1 = tk.Label(self, image=self.logotk1)
        label_logo2 = tk.Label(self, image=self.logotk2)

        # Obtener el tamaño de la ventana y las imágenes
        window_height = 625  # Altura de la ventana
        logo_height = 80   # Altura de los logotipos

        # Calcular la posición y colocar los logos en la parte inferior izquierda
        label_logo1.place(x=30, y=window_height - logo_height - 10)  # Ajusta las coordenadas según sea necesario
        label_logo2.place(x=140, y=window_height - logo_height - 10)  # Ajusta las coordenadas según sea necesario
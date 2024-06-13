import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class InicioView(tk.Frame):
    def __init__(self, master, controller, base_dir):
        super().__init__(master, bg="#F6F5FB")
        self.controller = controller
        self.base_dir = base_dir
        self.init_ui()
        self.after(1000, self.btnAnimate)  # evento para prolongar eventos a un tiempo especifico

    def init_ui(self):
        self.addBackgroudImage()
        self.addLogos()
        self.create_logo_chiapas()
        self.label1 = tk.Label(self, text="Monitoreo de Postura para Conducción de Vehículos de Transporte Público de Ruta Prolongada", font=("", 10, "bold"), bg="#F6F5FB", fg="black")
        self.label1.place(x=400, y=10)

        # Botón para exportar datos
        self.export_button = tk.Button(self, text="Exportar Datos", font=("", 10), command=self.controller.exportar_datos, bg="#1B6FBF", fg="white")
        self.export_button.place(x=10, y=10)

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
        image_path = os.path.join(self.base_dir, "img/fondo.png")
        self.img = Image.open(image_path)
        self.img = self.img.resize((490, 380), Image.LANCZOS)
        self.imgtk = ImageTk.PhotoImage(self.img)

        # Crear un Label con la imagen y centrarla
        label_img = tk.Label(self, image=self.imgtk, bg="#F6F5FB")
        label_img.place(x=-1, y=-1)

        image_path2 = os.path.join(self.base_dir, "img/project91.png")
        self.img2 = Image.open(image_path2)
        self.img2 = self.img2.resize((750, 210), Image.LANCZOS)
        self.imgtk2 = ImageTk.PhotoImage(self.img2)

        # Crear un Label con la imagen y centrarla
        label_img2 = tk.Label(self, image=self.imgtk2)
        label_img2.place(x=400, y=50)
        
    def addLogos(self):
        logo_path1 = os.path.join(self.base_dir, "img/rs.jpeg")
        self.logo1 = Image.open(logo_path1)
        self.logo1 = self.logo1.resize((70, 70), Image.LANCZOS)
        self.logotk1 = ImageTk.PhotoImage(self.logo1)

        logo_path2 = os.path.join(self.base_dir, "img/ado.jpeg")
        self.logo2 = Image.open(logo_path2)
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

    def create_logo_chiapas(self):
        image_path = os.path.join(self.base_dir, "img/chiapas.png")
        self.logo_chiapas = Image.open(image_path)
        self.logo_chiapas = self.logo_chiapas.resize((206, 189), Image.LANCZOS)
        self.logo_chiapas_tk = ImageTk.PhotoImage(self.logo_chiapas)

        # Crear Label para el logo de Chiapas
        self.label_logoChiapas = tk.Label(self, image=self.logo_chiapas_tk)
        self.label_logoChiapas.image = self.logo_chiapas_tk  # Guardar una referencia para evitar la recolección de basura
        self.label_logoChiapas.place(x=960, y=420)  # Ajusta las coordenadas según sea necesario
        self.label_logoChiapas.config(bg="#F6F5FB")

    def update_position(self):
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        image_width = self.logo_chiapas.width()
        image_height = self.logo_chiapas.height()
        x = window_width - image_width - 10  # margen de 10 píxeles desde el borde derecho
        y = window_height - image_height - 10  # margen de 10 píxeles desde el borde inferior
        self.label_logoChiapas.place(x=x, y=y)

    def on_resize(self, event):
        self.update_position()
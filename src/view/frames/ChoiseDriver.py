import tkinter as tk
from PIL import Image, ImageTk
import os

class ChoiseDriverView(tk.Frame):
    def __init__(self, master, controller, base_dir):
        super().__init__(master, bg="#F6F5FB")
        self.controller = controller
        self.base_dir = base_dir
        self.image2 = None

        self.init_ui()

    def init_ui(self):
        self.addBackgroudImage()
        self.addLogos()
        self.create_logo_chiapas()  # Add this line to create the LogoChiapas instance

        self.label_static = tk.Label(self, text="Monitoreo de Postura para Conducción de Vehículos de Transporte Público de Ruta Prolongada", font=("", 10, "bold"), bg="#F6F5FB", fg="black")
        self.label_static.place(x=400, y=10)

        self.label1 = tk.Label(self, text="Elige perfil de Operador", font=("Montserrat", 26, "bold"), bg="#F6F5FB", fg="black")
        self.label1.place(x=480, y=50)

        self.label2 = tk.Label(self, text="Maneje con precaución y sin distracciones", font=("Montserrat", 12, "bold"), bg="#F6F5FB", fg="black")
        self.label2.place(x=510, y=100)

        self.label3 = tk.Label(self, text="¡FELIZ VIAJE!", font=("Montserrat", 14, "bold"), bg="#F6F5FB", fg="black")
        self.label3.place(x=625, y=130)

        self.sectionBtn1()
        self.sectionBtn2()

    def sectionBtn1(self):
        self.btns1 = []
        incremento = 200
        choferes = self.controller.obtener_choferes()  # Obtén los choferes (id, nombre)
        for i in range(4):
            if i < len(choferes):  # Asegurarse de no superar el índice
                id_chofer, nombre = choferes[i]
                btn = tk.Button(self, text=nombre, height=4, width=15, font=("", 12, "bold"), bg="#F0F0F0")
                btn.place(x=incremento, y=200)
                btn.configure(command=lambda text=nombre: self.actionBtn(text))
                btn.lift()  # Asegurarse de que el botón esté al frente
                self.btns1.append(btn)
                incremento += 220

    def sectionBtn2(self):
        self.btns2 = []
        incremento = 200
        choferes = self.controller.obtener_choferes()  # Obtén los choferes (id, nombre)
        for i in range(4, 8):
            if i < len(choferes):  # Asegurarse de no superar el índice
                id_chofer, nombre = choferes[i]
                btn = tk.Button(self, text=nombre, height=4, width=15, font=("", 12, "bold"), bg="#F0F0F0")
                btn.place(x=incremento, y=340)
                btn.configure(command=lambda text=nombre: self.actionBtn(text))  # Corregido el comando
                btn.lift()  # Asegurarse de que el botón esté al frente
                self.btns2.append(btn)
                incremento += 220

    def show(self):
        self.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.pack_forget()

    def actionBtn(self, text):
        self.controller.selectionOptions(text)

    def addBackgroudImage(self):
        image_path = os.path.join(self.base_dir, "img/fondo.png")
        self.img = Image.open(image_path)
        self.img = self.img.resize((490, 380), Image.LANCZOS)
        self.imgtk = ImageTk.PhotoImage(self.img)

        # Crear un Label con la imagen y centrarla
        label_img = tk.Label(self, image=self.imgtk, bg="#F6F5FB")
        label_img.place(x=-1, y=-1)

    def addLogos(self):
        img_path1 = os.path.join(self.base_dir, "img/rs.jpeg")
        img_path2 = os.path.join(self.base_dir, "img/ado.jpeg")

        self.img1 = Image.open(img_path1)
        self.img1 = self.img1.resize((70, 70), Image.LANCZOS)
        self.imgtk1 = ImageTk.PhotoImage(self.img1)

        self.img2 = Image.open(img_path2)
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
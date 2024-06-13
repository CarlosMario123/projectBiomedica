import tkinter as tk
from PIL import Image, ImageTk
from src.context.contextChofer import ContextChofer
from datetime import datetime
import os

class RecorridoFrame(tk.Frame):
    def __init__(self, master, controller, base_dir):
        super().__init__(master, bg="#F6F5FB")
        self.controller = controller
        self.base_dir = base_dir
        self.init_ui()
        self.start_time = None
        self.running = False
        
        # Crear instancia de LogoChiapas
        self.create_logo_chiapas()

    def init_ui(self):
        self.addBackgroundImage()
        self.addLogos()

        self.label1 = tk.Label(self, text="", font=("", 18, "bold"), height=2)
        self.label1.pack()

        self.label2 = tk.Label(self, text="Tiempo de viaje transcurrido 00:00:00", font=("", 14, ""), height=1, bg="#F6F5FB", fg="black")
        self.label2.place(x=480, y=70)
        self.label2.pack()

        self.label3 = tk.Label(self, text="¿No es usted o desea cancelar recorrido?", font=("", 16, "bold"), height=12, bg="#F6F5FB", fg="black")
        self.label3.place(x=480, y=200)
        self.label3.pack()

        self.label4 = tk.Label(self, text="Maneje con precaución y sin distracciones", font=("Montserrat", 12, "bold"), bg="#F6F5FB", fg="black")
        self.label4.place(x=510, y=100)
        self.label5 = tk.Label(self, text="¡FELIZ VIAJE!", font=("Montserrat", 14, "bold"), bg="#F6F5FB", fg="black")
        self.label5.place(x=625, y=130)

        self.btn2 = tk.Button(self, text="Cancelar recorrido", bg="blue", fg="white", font=("Arial", 18), height=1)
        self.btn2.config(command=self.controller.regresarInicio)
        self.btn2.pack()

        # Llamar a la función para actualizar el nombre del chofer cada vez que se muestra la ventana
        self.bind("<Visibility>", self.update_name)

        self.sensor_labels = {
            "angulo": tk.Label(self, text="Ángulo: 0°", font=("Arial", 12), bg="#F6F5FB", fg="black"),
            "distancia1": tk.Label(self, text="Distancia 1: 0 cm", font=("Arial", 12), bg="#F6F5FB", fg="black"),
            "distancia2": tk.Label(self, text="Distancia 2: 0 cm", font=("Arial", 12), bg="#F6F5FB", fg="black"),
            "presencia": tk.Label(self, text="Presencia: No", font=("Arial", 12), bg="#F6F5FB", fg="black")
        }

        for label in self.sensor_labels.values():
            label.pack()

    def update_name(self, event):
        # Actualizar el nombre del chofer cada vez que se muestra la ventana
        self.label1.config(text=f"Bienvenido: {ContextChofer().get_instance().get_name_chofer()}", bg="#F6F5FB", fg="black")

    def show(self):
        # Actualizar el nombre del chofer al mostrar la ventana
        self.update_name(None)
        self.pack(fill=tk.BOTH, expand=True)
        self.running = True
        self.start_time = datetime.now()
        self.changeCronometro()

    def hide(self):
        self.running = False
        self.pack_forget()

    def changeCronometro(self):
        if self.running:
            current_time = datetime.now()
            elapsed_time = current_time - self.start_time
            formatted_time = str(elapsed_time).split(".")[0]
            self.label2.config(text=f"Tiempo de viaje transcurrido {formatted_time}")
            self.after(1000, self.changeCronometro)

    def abrir_ventana(self, id):
        ruta = os.path.join(self.base_dir, f"img/postura{id}.png")
        self.nueva_ventana = tk.Toplevel(self)
        self.nueva_ventana.title("Sugerencia de Postura")
        self.nueva_ventana.geometry("800x600")
    
        # Cargar la imagen
        self.img = Image.open(ruta)
        self.img = self.img.resize((800, 500), Image.LANCZOS)
        self.imgtk = ImageTk.PhotoImage(self.img)
        
        # Crear un Label con la imagen y centrarla
        label_img = tk.Label(self.nueva_ventana, image=self.imgtk)
        label_img.pack(expand=True)
        
        # Etiqueta en la nueva ventana
        label_texto = tk.Label(self.nueva_ventana, text="¡Esta es una sugerencia de postura!")
        label_texto.pack(pady=10)

        # Cerrar la ventana después de 2 minutos (120000 ms)
        self.nueva_ventana.after(120000, self.cerrar_ventana)
    
    def cerrar_ventana(self):
        self.nueva_ventana.destroy()

    def actualizar_datos_sensores(self, angulo, distancia1, distancia2, presencia):
        self.sensor_labels["angulo"].config(text=f"Ángulo: {angulo}°")
        self.sensor_labels["distancia1"].config(text=f"Distancia 1: {distancia1} cm")
        self.sensor_labels["distancia2"].config(text=f"Distancia 2: {distancia2} cm")
        self.sensor_labels["presencia"].config(text=f"Presencia: {'Sí' if presencia else 'No'}")

    def addBackgroundImage(self):
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
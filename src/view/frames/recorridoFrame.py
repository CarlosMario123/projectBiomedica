import tkinter as tk
from PIL import Image, ImageTk
from src.context.contextChofer import ContextChofer
import random

class RecorridoFrame(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.cronometro = 0
        self.running = True
        self.init_ui()

    def init_ui(self):
        self.addBackgroudImage()
        self.addLogos()
        self.label1 = tk.Label(self, text="", font=("", 18, "bold"), height=2)
        self.label1.pack()

        self.label2 = tk.Label(self, text=f"Tiempo de viaje transcurrido {self.cronometro}", font=("", 14, ""), height=1, width=300)
        self.label2.pack()

        self.label3 = tk.Label(self, text="¿No es usted cancelar recorrido?", font=("", 16, "bold"), height=12)
        self.label3.pack()
        
        self.btn2 = tk.Button(self, text="Cancelar recorrido", bg="blue", fg="white", font=("Arial", 18), height=1)
        self.btn2.config(command=self.controller.regresarInicio)
        self.btn2.pack()

        # Llamar a la función para actualizar el nombre del chofer cada vez que se muestra la ventana
        self.bind("<Visibility>", self.update_name)

        self.label2.after(1000, self.changeCronometro)

    def update_name(self, event):
        # Actualizar el nombre del chofer cada vez que se muestra la ventana
        self.label1.config(text=f"Bienvenido: {ContextChofer().get_instance().get_name_chofer()}")

    def show(self):
        # Actualizar el nombre del chofer al mostrar la ventana
        self.update_name(None)
        self.pack(fill=tk.BOTH, expand=True)
        self.running = True
        self.changeCronometro()

    def hide(self):
        self.running = False
        self.cronometro = 0
        self.pack_forget()

    def changeCronometro(self):
        if self.running:
            self.cronometro += 1
            self.label2.config(text=f"Tiempo de viaje transcurrido {self.cronometro}")
            self.label2.after(2000, self.changeCronometro)

    def abrir_ventana(self,id):#funcion que notificara atravez de id
        ruta = "img/postura.png"
        if id == 1:
            ruta = "img/postura2.png"
        elif id == 2:
            ruta = "img/postura3.png"
        

        self.nueva_ventana = tk.Toplevel(self)
        self.nueva_ventana.title("Otra Ventana")
        self.nueva_ventana.geometry("800x600")
        
        # Cargar la imagen
        self.img = Image.open(random.choice(ruta))
  # Reemplaza con la ruta de tu imagen
        self.img = self.img.resize((800, 500), Image.ANTIALIAS)  # Redimensionar si es necesario
        self.imgtk = ImageTk.PhotoImage(self.img)
        
        # Crear un Label con la imagen y centrarla
        label_img = tk.Label(self.nueva_ventana, image=self.imgtk)
        label_img.pack(expand=True)
        
        # Etiqueta en la nueva ventana
        label_texto = tk.Label(self.nueva_ventana, text="¡Esta es otra ventana!")
        label_texto.pack(pady=10)

        # Cerrar la ventana después de 2 segundos
        self.nueva_ventana.after(2000, self.cerrar_ventana)
    
    def cerrar_ventana(self):
        self.nueva_ventana.destroy()
        
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
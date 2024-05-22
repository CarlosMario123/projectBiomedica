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
        self.label1 = tk.Label(self, text="", font=("", 18, "bold"), height=2)
        self.label1.pack()

        self.label2 = tk.Label(self, text=f"Tiempo de viaje transcurrido {self.cronometro}", font=("", 14, ""), height=1, width=300)
        self.label2.pack()

        self.label3 = tk.Label(self, text="¿No es usted o desea cancelar recorrido?", font=("", 16, "bold"), height=12)
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

    def abrir_ventana(self):
        ruta = ["img/postura.png","img/postura2.png","img/postura3.png"]
        # Crear y configurar la nueva ventana
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
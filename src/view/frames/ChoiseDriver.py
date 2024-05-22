import tkinter as tk
from src.view.componentes.logoChiapas import LogoChiapas
from PIL import Image, ImageTk
class ChoiseDriverView(tk.Frame):
    def __init__(self,master, controller):
        super().__init__(master)
        self.controller = controller
        self.image2 = None
     
        self.init_ui()
        print("dentro")
        
    def init_ui(self):
        self.logoChiapa = LogoChiapas().get_instance(master=self)
        self.addBackgroudImage()
        self.addLogos()
        self.label1 = tk.Label(self, text="Elige el operador", font=("", 18, "bold"))
        self.label1.place(x=350, y=1)
        self.sectionBtn1()
        self.sectionBtn2()
        
       
        
        
    def sectionBtn1(self):
        self.btns1 = []
        incremento = 20
        choferes = self.controller.obtener_choferes()  # Obtén los nombres de los choferes
        for i in range(4):
            btn = tk.Button(self, text=choferes[i], height=4, width=15, font=("", 12, "bold"))
            btn.place(x=incremento, y=160)
            btn.configure(command=lambda text=choferes[i]: self.actionBtn(text))
            self.btns1.append(btn)
            incremento += 220


    def sectionBtn2(self):
        self.btns2 = []
        incremento = 20
        choferes = self.controller.obtener_choferes()  # Obtén los nombres de los choferes
        for i in range(4, 8):
            btn = tk.Button(self, text=choferes[i], height=4, width=15, font=("", 12, "bold"))
            btn.place(x=incremento, y=300)
            btn.configure(command=lambda text=choferes[i]: self.actionBtn(text))  # Corregido el comando
            self.btns2.append(btn)
            incremento += 220
    
    def show(self):
        self.pack(fill=tk.BOTH, expand=True) 

    def hide(self):
        self.pack_forget()

    def actionBtn(self, text):
        self.controller.selectionOptions(text)
    
    
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
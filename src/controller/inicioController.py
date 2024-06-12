from src.view.frames.inicio import InicioView
from bd.datos_postura.getAllData import obtener_todos_registros
import csv
from tkinter import filedialog
from datetime import datetime

class InicioController():
    def __init__(self, root):
        self.root = root
        self.view = InicioView(master=root, controller=self)
        
    def getView(self):
        self.view.show()
    
    def hide(self):
        self.view.hide()
        
    def redirectDrivers(self):
        print("entro")
        self.root.cambiarVista("choiseD")

    def exportar_datos(self):
        registros = obtener_todos_registros()

        if not registros:
            print("No hay datos para exportar.")
            return

        # Generar el nombre del archivo basado en la fecha actual
        fecha_actual = datetime.now().strftime("%d-%m-%Y")
        nombre_predeterminado = f"Posturas-{fecha_actual}.csv"
        
        # Abrir el explorador de archivos nativo del sistema con el nombre predeterminado del archivo
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile=nombre_predeterminado, filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        
        if file_path:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'ID Chofer', 'Timestamp', 'Ángulo Giroscopio', 'Distancia CM', 'Presencia', 'Recomendación'])
                for registro in registros:
                    writer.writerow([
                        registro['id'], registro['id_chofer'], registro['timestamp'], 
                        registro['angulo_giroscopio'], registro['distancia_cm'], 
                        registro['presencia'], registro['recomendacion']
                    ])
            print(f"Datos exportados correctamente a {file_path}")

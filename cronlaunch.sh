#!/bin/bash
echo "La aplicación no está en ejecución. Iniciando..."
# Activar el entorno virtual de Python
source /home/pi/Desktop/projectBiomedica/venv/bin/activate
# Esperar unos segundos antes de iniciar la aplicación
#sleep 5
# Iniciar la aplicación en segundo plano y registrar la salida
python /home/pi/Desktop/projectBiomedica/app.py
#fi

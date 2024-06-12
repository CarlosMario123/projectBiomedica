#!/bin/bash
echo "La aplicación no está en ejecución. Iniciando..."
# Activar el entorno virtual de Python
source /home/raspberry/Documentos/projectBiomedica/venv/bin/activate
# Esperar unos segundos antes de iniciar la aplicación
#sleep 5
# Iniciar la aplicación en segundo plano y registrar la salida
python3 /home/raspberry/Documentos/projectBiomedica/app.py
#fi

import sqlite3

def agregar_postura_temporal(timestap, angulo_giroscopio, distancia_cm, presencia):    
    conn = sqlite3.connect('bio.db')

    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO postura_temp (timestamp, angulo_giroscopio, distancia_cm, presencia)
        VALUES (?, ?, ?, ?)
        ''', 
        (timestap, angulo_giroscopio, distancia_cm, presencia))

    conn.commit()
    conn.close()
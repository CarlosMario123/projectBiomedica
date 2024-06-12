import sqlite3

def agregar_postura_promediada(id_chofer, timestamp, angulo_promedio, distancia_promedio, presencia_promedio, recomendacion):
    conn = sqlite3.connect('bio.db')

    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO postura_promediada (id_chofer, timestamp, angulo_giroscopio, distancia_cm, presencia, recomendacion)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', 
        (id_chofer, timestamp, angulo_promedio, distancia_promedio, presencia_promedio, recomendacion))
    
    conn.commit()

    conn.close()
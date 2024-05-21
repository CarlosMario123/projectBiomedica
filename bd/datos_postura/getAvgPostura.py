import sqlite3
def obtener_promedio_postura():
    conn = sqlite3.connect('bio.db')
    cursor = conn.cursor()
    
    cursor.execute('''
            SELECT AVG(angulo_giroscopio), AVG(distancia_cm), AVG(presencia)
            FROM postura_temp
        ''')
    
    result = cursor.fetchone()

    conn.close()

    return result
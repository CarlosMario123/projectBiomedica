import sqlite3

def obtener_todos_registros():
    try:
        conn = sqlite3.connect('bio.db') 
        cursor = conn.cursor()

        query = "SELECT * FROM postura_promediada"
        cursor.execute(query)
        rows = cursor.fetchall()

        posturas = [{'id': row[0], 'id_chofer': row[1], 'timestamp': row[2], 'angulo_giroscopio': row[3], 'distancia_cm': row[4], 'presencia': row[5], 'recomendacion': row[6]} for row in rows]

        conn.close()
        return posturas

    except sqlite3.Error as e:
        print(f"Error al acceder a la base de datos: {e}")
        return None

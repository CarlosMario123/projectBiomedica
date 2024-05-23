import sqlite3

def obtener_ultimas_posturas_promediadas(limit):
    try:
        conn = sqlite3.connect('bio.db') 
        cursor = conn.cursor()

        query = """
        SELECT angulo, distancia, presencia
        FROM postura_promediada
        ORDER BY timestamp DESC
        LIMIT ?
        """
        cursor.execute(query, (limit,))
        
        rows = cursor.fetchall()

        posturas = [{'angulo': row[0], 'distancia': row[1], 'presencia': row[2]} for row in rows]

        conn.close()
        
        return posturas
    
    except sqlite3.Error as e:
        print(f"Error al acceder a la base de datos: {e}")
        return None
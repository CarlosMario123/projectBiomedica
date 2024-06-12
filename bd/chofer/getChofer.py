import sqlite3

def obtener_choferes():
    conn = sqlite3.connect('bio.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id_chofer, nombre FROM chofer')
    choferes = cursor.fetchall()

    conn.close()

    return choferes  # Devuelve una lista de tuplas (id_chofer, nombre)
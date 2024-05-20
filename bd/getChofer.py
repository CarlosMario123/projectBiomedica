import sqlite3

def obtener_choferes():
    conn = sqlite3.connect('bio.db')
    cursor = conn.cursor()

    cursor.execute('SELECT nombre FROM chofer')
    choferes = cursor.fetchall()

    conn.close()

    return [chofer[0] for chofer in choferes]
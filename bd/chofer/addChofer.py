import sqlite3

def agregar_chofer(nombre):
    conn = sqlite3.connect('bio.db')
    cursor = conn.cursor()

    # verificar si el chofer existe
    cursor.execute('SELECT id_chofer FROM chofer WHERE nombre = ?', (nombre,))
    existente = cursor.fetchone()
    
 
    if not existente:
        cursor.execute('INSERT INTO chofer (nombre) VALUES (?)', (nombre,))
        conn.commit()

    conn.close()

def llenarChoferes():
    for i in range(8):
        nombre = f"Conductor {i+1}"
        agregar_chofer(nombre)
        
llenarChoferes()

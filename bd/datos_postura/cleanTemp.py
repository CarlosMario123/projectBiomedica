import sqlite3

def limpiar_postura_temp():
    conn = sqlite3.connect('bio.db')

    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM postura_temp
        ''')
    
    conn.commit()

    conn.close()
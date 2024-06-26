import sqlite3

def createTables():

    conn = sqlite3.connect('bio.db')
    cursor = conn.cursor()
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS chofer (
                       id_chofer INTEGER PRIMARY KEY,
                       nombre TEXT
                   )
                   ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS sensores (
                       id_sensores INTEGER PRIMARY KEY,
                       datos_giroscopio REAL,
                       distancia REAL,
                       presion REAL
                   )
                   ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS recorrido (
                       id_recorrido INTEGER PRIMARY KEY,
                       id_chofer INTEGER,
                       id_sensores INTEGER,
                       FOREIGN KEY(id_chofer) REFERENCES chofer(id_chofer),
                       FOREIGN KEY(id_sensores) REFERENCES sensores(id_sensores)
                   )
                   ''')
    
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS postura_temp (
                    timestamp TEXT,
                    angulo_giroscopio INTEGER,
                    distancia_cm REAL,
                    presencia BOOLEAN
                )
                ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS postura_promediada (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_chofer INTEGER,
                timestamp TEXT,
                angulo_giroscopio INTEGER,
                distancia_cm REAL,
                presencia BOOLEAN,
                recomendacion TEXT
            )''')

    conn.commit()
    conn.close()



import sqlite3

# Conectar a la base de datos (se creará si no existe)
conexion = sqlite3.connect('prision_twd.db')
cursor = conexion.cursor()

#Tabla supervivientes

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Supervivientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER,
        genero TEXT,
        rol TEXT,
        estado TEXT
    )
''')

#Tabla suministros

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Suministros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        cantidad INTEGER,
        tipo TEXT,
        id_superviviente INTEGER,
        FOREIGN KEY (id_superviviente) REFERENCES Supervivientes(id)
    )
''')

#Tabla vehiculos

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vehiculos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca TEXT,
        modelo TEXT,
        año INTEGER,
        id_superviviente INTEGER,
        FOREIGN KEY (id_superviviente) REFERENCES Supervivientes(id)
    )
''')

#Tabla Armas

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Armas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT,
        modelo TEXT,
        municion INTEGER,
        id_superviviente INTEGER,
        FOREIGN KEY (id_superviviente) REFERENCES Supervivientes(id)
    )
''')

conexion.commit()
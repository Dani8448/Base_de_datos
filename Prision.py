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

# Función genérica para ejecutar consultas con control de transacciones
def ejecutar_consulta(query, parametros=()):
    conexion = conectar_bd()
    try:
        with conexion:  # Maneja automáticamente el commit y el rollback en caso de error
            cursor = conexion.cursor()
            cursor.execute(query, parametros)
            if query.strip().upper().startswith("SELECT"):
                return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error en la consulta: {e}")
        return None
# CRUD Supervivientes
def insertar_superviviente(nombre, edad, genero, rol, estado):
    ejecutar_consulta("INSERT INTO Supervivientes (nombre, edad, genero, rol, estado) VALUES (?, ?, ?, ?, ?)", 
                      (nombre, edad, genero, rol, estado))

def leer_supervivientes():
    return ejecutar_consulta("SELECT * FROM Supervivientes")

def actualizar_superviviente(id, nombre, edad, genero, rol, estado):
    ejecutar_consulta("UPDATE Supervivientes SET nombre=?, edad=?, genero=?, rol=?, estado=? WHERE id=?", 
                      (nombre, edad, genero, rol, estado, id))

def eliminar_superviviente(id):
    ejecutar_consulta("DELETE FROM Supervivientes WHERE id=?", (id,))
# CRUD Suministros
def insertar_suministro(nombre, cantidad, tipo, id_superviviente):
    ejecutar_consulta("INSERT INTO Suministros (nombre, cantidad, tipo, id_superviviente) VALUES (?, ?, ?, ?)", 
                      (nombre, cantidad, tipo, id_superviviente))

def leer_suministros():
    return ejecutar_consulta("SELECT * FROM Suministros")

def actualizar_suministro(id, nombre, cantidad, tipo, id_superviviente):
    ejecutar_consulta("UPDATE Suministros SET nombre=?, cantidad=?, tipo=?, id_superviviente=? WHERE id=?", 
                      (nombre, cantidad, tipo, id_superviviente, id))

def eliminar_suministro(id):
    ejecutar_consulta("DELETE FROM Suministros WHERE id=?", (id,))

# CRUD Vehículos
def insertar_vehiculo(marca, modelo, ano, id_superviviente):
    ejecutar_consulta("INSERT INTO Vehiculos (marca, modelo, ano, id_superviviente) VALUES (?, ?, ?, ?)", 
                      (marca, modelo, ano, id_superviviente))

def leer_vehiculos():
    return ejecutar_consulta("SELECT * FROM Vehiculos")

def actualizar_vehiculo(id, marca, modelo, ano, id_superviviente):
    ejecutar_consulta("UPDATE Vehiculos SET marca=?, modelo=?, ano=?, id_superviviente=? WHERE id=?", 
                      (marca, modelo, ano, id_superviviente, id))

def eliminar_vehiculo(id):
    ejecutar_consulta("DELETE FROM Vehiculos WHERE id=?", (id,))

# CRUD Armas
def insertar_arma(tipo, modelo, municion, id_superviviente):
    ejecutar_consulta("INSERT INTO Armas (tipo, modelo, municion, id_superviviente) VALUES (?, ?, ?, ?)", 
                      (tipo, modelo, municion, id_superviviente))

def leer_armas():
    return ejecutar_consulta("SELECT * FROM Armas")

def actualizar_arma(id, tipo, modelo, municion, id_superviviente):
    ejecutar_consulta("UPDATE Armas SET tipo=?, modelo=?, municion=?, id_superviviente=? WHERE id=?", 
                      (tipo, modelo, municion, id_superviviente, id))

def eliminar_arma(id):
    ejecutar_consulta("DELETE FROM Armas WHERE id=?", (id,))

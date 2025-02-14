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

import sqlite3

# Conectar a la base de datos (se creará si no existe)
conexion = sqlite3.connect('prision_twd.db')
cursor = conexion.cursor()

# Función genérica para ejecutar consultas con control de transacciones
def ejecutar_consulta(query, parametros=()):
    try:
        with conexion:  # Maneja automáticamente el commit y el rollback en caso de error
            cursor = conexion.cursor()
            cursor.execute(query, parametros)
            if query.strip().upper().startswith("SELECT"):
                return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error en la consulta: {e}")
        return None

# Menú interactivo
def menu():
    while True:
        print("\nMenú principal:")
        print("1. Insertar superviviente")
        print("2. Ver supervivientes")
        print("3. Actualizar superviviente")
        print("4. Eliminar superviviente")
        print("5. Insertar suministro")
        print("6. Ver suministros")
        print("7. Actualizar suministro")
        print("8. Eliminar suministro")
        print("9. Insertar vehículo")
        print("10. Ver vehículos")
        print("11. Actualizar vehículo")
        print("12. Eliminar vehículo")
        print("13. Insertar arma")
        print("14. Ver armas")
        print("15. Actualizar arma")
        print("16. Eliminar arma")
        print("17. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            genero = input("Género: ")
            rol = input("Rol: ")
            estado = input("Estado: ")
            ejecutar_consulta("INSERT INTO Supervivientes (nombre, edad, genero, rol, estado) VALUES (?, ?, ?, ?, ?)", 
                              (nombre, edad, genero, rol, estado))
            print("Superviviente agregado.")
        
        elif opcion == "2":
            for s in ejecutar_consulta("SELECT * FROM Supervivientes"):
                print(s)
        
        elif opcion == "3":
            id = int(input("ID del superviviente: "))
            nombre = input("Nuevo nombre: ")
            edad = int(input("Nueva edad: "))
            genero = input("Nuevo género: ")
            rol = input("Nuevo rol: ")
            estado = input("Nuevo estado: ")
            ejecutar_consulta("UPDATE Supervivientes SET nombre=?, edad=?, genero=?, rol=?, estado=? WHERE id=?", 
                              (nombre, edad, genero, rol, estado, id))
            print("Superviviente actualizado.")
        
        elif opcion == "4":
            id = int(input("ID del superviviente a eliminar: "))
            ejecutar_consulta("DELETE FROM Supervivientes WHERE id=?", (id,))
            print("Superviviente eliminado.")
        
        elif opcion == "5":
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            tipo = input("Tipo: ")
            id_superviviente = int(input("ID del superviviente: "))
            ejecutar_consulta("INSERT INTO Suministros (nombre, cantidad, tipo, id_superviviente) VALUES (?, ?, ?, ?)", 
                              (nombre, cantidad, tipo, id_superviviente))
            print("Suministro agregado.")
        
        elif opcion == "6":
            for s in ejecutar_consulta("SELECT * FROM Suministros"):
                print(s)
        
        elif opcion == "7":
            id = int(input("ID del suministro: "))
            nombre = input("Nuevo nombre: ")
            cantidad = int(input("Nueva cantidad: "))
            tipo = input("Nuevo tipo: ")
            id_superviviente = int(input("Nuevo ID del superviviente: "))
            ejecutar_consulta("UPDATE Suministros SET nombre=?, cantidad=?, tipo=?, id_superviviente=? WHERE id=?", 
                              (nombre, cantidad, tipo, id_superviviente, id))
            print("Suministro actualizado.")
        
        elif opcion == "8":
            id = int(input("ID del suministro a eliminar: "))
            ejecutar_consulta("DELETE FROM Suministros WHERE id=?", (id,))
            print("Suministro eliminado.")
        
        elif opcion == "9":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            ano = int(input("Año: "))
            id_superviviente = int(input("ID del superviviente: "))
            ejecutar_consulta("INSERT INTO Vehiculos (marca, modelo, año, id_superviviente) VALUES (?, ?, ?, ?)", 
                              (marca, modelo, ano, id_superviviente))
            print("Vehículo agregado.")
        
        elif opcion == "10":
            for v in ejecutar_consulta("SELECT * FROM Vehiculos"):
                print(v)
        
        elif opcion == "11":
            id = int(input("ID del vehículo: "))
            marca = input("Nueva marca: ")
            modelo = input("Nuevo modelo: ")
            ano = int(input("Nuevo año: "))
            id_superviviente = int(input("Nuevo ID del superviviente: "))
            ejecutar_consulta("UPDATE Vehiculos SET marca=?, modelo=?, año=?, id_superviviente=? WHERE id=?", 
                              (marca, modelo, ano, id_superviviente, id))
            print("Vehículo actualizado.")
        
        elif opcion == "12":
            id = int(input("ID del vehículo a eliminar: "))
            ejecutar_consulta("DELETE FROM Vehiculos WHERE id=?", (id,))
            print("Vehículo eliminado.")
        
        elif opcion == "13":
            tipo = input("Tipo: ")
            modelo = input("Modelo: ")
            municion = int(input("Munición: "))
            id_superviviente = int(input("ID del superviviente: "))
            ejecutar_consulta("INSERT INTO Armas (tipo, modelo, municion, id_superviviente) VALUES (?, ?, ?, ?)", 
                              (tipo, modelo, municion, id_superviviente))
            print("Arma agregada.")
        
        elif opcion == "14":
            for a in ejecutar_consulta("SELECT * FROM Armas"):
                print(a)
        
        elif opcion == "15":
            id = int(input("ID del arma: "))
            tipo = input("Nuevo tipo: ")
            modelo = input("Nuevo modelo: ")
            municion = int(input("Nueva munición: "))
            id_superviviente = int(input("Nuevo ID del superviviente: "))
            ejecutar_consulta("UPDATE Armas SET tipo=?, modelo=?, municion=?, id_superviviente=? WHERE id=?", 
                              (tipo, modelo, municion, id_superviviente, id))
            print("Arma actualizada.")
        
        elif opcion == "16":
            id = int(input("ID del arma a eliminar: "))
            ejecutar_consulta("DELETE FROM Armas WHERE id=?", (id,))
            print("Arma eliminada.")
        
        elif opcion == "17":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


# Ejecutar la creación de las tablas y mostrar el menú si se ejecuta directamente
if __name__ == "__main__":
    menu()

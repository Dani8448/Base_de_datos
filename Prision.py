import sqlite3

# Conectar a la base de datos (se creará si no existe)
conexion = sqlite3.connect('prision_twd.db')
cursor = conexion.cursor()


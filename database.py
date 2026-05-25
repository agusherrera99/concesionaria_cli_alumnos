import sqlite3

class Database:
    def __init__(self):
        self.conexion = sqlite3.connect('database.sqlite3')

        self.inicializar_base_de_datos()

    def inicializar_base_de_datos(self):
        self.inicializar_autos()

    def ejecutar_query(self, query, params=()):
        try:
            with self.conexion as conexion:
                cursor = conexion.cursor()
                return cursor.execute(query, params)
        except Exception as error:
            print(error)

    def inicializar_autos(self):
        query = """
        CREATE TABLE IF NOT EXISTS autos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patente TEXT UNIQUE NOT NULL,
            marca TEXT NOT NULL,
            modelo TEXT NOT NULL,
            anio INTEGER NOT NULL,
            kilometros INTEGER NOT NULL,
            precio INTEGER NOT NULL,
            estado TEXT NOT NULL,
            fecha_ingreso TEXT NOT NULL
        )
        """
        self.ejecutar_query(query)

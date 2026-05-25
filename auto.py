from database import Database


class Auto:
    def __init__(self):
        self.database = Database()

    def guardar_auto(self, datos):
        query = """
        INSERT INTO autos (patente, marca, modelo, anio, kilometros, precio, estado, fecha_ingreso)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.database.ejecutar_query(query, datos)
        print("Auto guardado correctamente")

    def seleccionar_todos(self):
        query = """
        SELECT * FROM autos
        """

        respuesta = self.database.ejecutar_query(query)
        resultado = respuesta.fetchall()
        return resultado

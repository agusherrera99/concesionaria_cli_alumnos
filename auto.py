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
        query = "SELECT * FROM autos"

        respuesta = self.database.ejecutar_query(query)
        resultado = respuesta.fetchall()
        return resultado

    def seleccionar_por(self, columna, valor):
        query = f"""
        SELECT * FROM autos
        WHERE {columna} = ?
        ORDER BY id
        """
        respuesta = self.database.ejecutar_query(query, (valor,))
        resultado = respuesta.fetchall()
        return resultado

    def seleccionar_por_rango(self, minimo, maximo):
        query = """
        SELECT * FROM autos
        WHERE precio BETWEEN ? AND ?
        ORDER BY precio
        """
        respuesta = self.database.ejecutar_query(query, (minimo, maximo,))
        resultado = respuesta.fetchall()
        return resultado

    def seleccionar_auto_por_patente(self, patente: str):
        query = """
        SELECT * FROM autos
        WHERE patente = ?
        """
        respuesta = self.database.ejecutar_query(query, (patente,))
        resultado = respuesta.fetchone()
        return resultado

    def seleccionar_auto_por_numero_interno(self, numero_interno: int):
        query = """
        SELECT * FROM autos
        WHERE id = ?
        """
        respuesta = self.database.ejecutar_query(query, (numero_interno,))
        resultado = respuesta.fetchone()
        return resultado

    def cambiar_estado(self, _id, estado):
        query = """
        UPDATE autos
        SET estado = ?
        WHERE id = ?
        """
        self.database.ejecutar_query(query, (estado, _id,))
        print("Estado del auto actualizado correctamente")

    def dar_de_baja(self, _id):
        query = """
        DELETE FROM autos
        WHERE id = ?
        """
        self.database.ejecutar_query(query, (_id,))
        print("Auto eliminado correctamente")

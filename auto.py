from database import Database

# La clase Auto representa el "Modelo" de datos.
# Se encarga de las consultas SQL para que el menú no tenga que saber cómo funciona la base de datos.
class Auto:
    def __init__(self):
        # Usamos una instancia de Database para realizar las operaciones.
        self.database = Database()

    def guardar_auto(self, datos):
        """Inserta un nuevo auto en la tabla 'autos'."""
        query = """
        INSERT INTO autos (patente, marca, modelo, anio, kilometros, precio, estado, fecha_ingreso)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.database.ejecutar_query(query, datos)

    def seleccionar_todos(self):
        """Trae todos los registros de la tabla."""
        query = "SELECT * FROM autos"
        respuesta = self.database.ejecutar_query(query)
        return respuesta.fetchall()

    def seleccionar_por(self, columna, valor):
        """Busca autos filtrando por una columna específica (ej: marca o estado)."""
        query = f"SELECT * FROM autos WHERE {columna} = ? ORDER BY id"
        respuesta = self.database.ejecutar_query(query, (valor,))
        return respuesta.fetchall()

    def seleccionar_por_rango(self, minimo, maximo):
        """Busca autos cuyo precio esté entre el mínimo y el máximo."""
        query = "SELECT * FROM autos WHERE precio BETWEEN ? AND ? ORDER BY precio"
        respuesta = self.database.ejecutar_query(query, (minimo, maximo,))
        return respuesta.fetchall()

    def seleccionar_auto_por_patente(self, patente: str):
        """Busca un único auto por su patente."""
        query = "SELECT * FROM autos WHERE patente = ?"
        respuesta = self.database.ejecutar_query(query, (patente,))
        return respuesta.fetchone()

    def seleccionar_auto_por_numero_interno(self, numero_interno: int):
        """Busca un único auto por su ID (número interno)."""
        query = "SELECT * FROM autos WHERE id = ?"
        respuesta = self.database.ejecutar_query(query, (numero_interno,))
        return respuesta.fetchone()

    def cambiar_estado(self, _id, estado):
        """Actualiza el campo 'estado' de un auto específico."""
        query = "UPDATE autos SET estado = ? WHERE id = ?"
        self.database.ejecutar_query(query, (estado, _id,))

    def dar_de_baja(self, _id):
        """Elimina físicamente un registro de la base de datos."""
        query = "DELETE FROM autos WHERE id = ?"
        self.database.ejecutar_query(query, (_id,))

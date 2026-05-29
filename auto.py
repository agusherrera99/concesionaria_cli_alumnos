import database


def guardar_auto(datos):
    """Inserta un nuevo auto."""
    database.guardar_auto(datos)


def seleccionar_todos():
    """Trae todos los registros."""
    return database.obtener_todos()


def seleccionar_por(columna, valor):
    """Busca autos filtrando por una columna específica."""
    return database.buscar_por_campo(columna, valor)


def seleccionar_por_rango(minimo, maximo):
    """Busca autos cuyo precio esté entre el mínimo y el máximo."""
    return database.buscar_por_rango_precio(minimo, maximo)


def seleccionar_auto_por_patente(patente: str):
    """Busca un único auto por su patente."""
    return database.buscar_por_patente(patente)


def seleccionar_auto_por_numero_interno(numero_interno: int):
    """Busca un único auto por su ID."""
    return database.buscar_por_id(numero_interno)


def cambiar_estado(_id, estado):
    """Actualiza el campo 'estado' de un auto específico."""
    database.cambiar_estado(_id, estado)


def dar_de_baja(_id):
    """Elimina físicamente un registro."""
    database.dar_de_baja(_id)

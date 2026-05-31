import database


def registrar_cliente(datos):
    """Registra un nuevo cliente."""
    return database.guardar_cliente(datos)


def listar_todos():
    """Retorna todos los clientes."""
    return database.obtener_todos_clientes()


def buscar_por_dni(dni):
    """Busca un cliente por DNI."""
    return database.buscar_cliente_por_dni(dni)


def buscar_por_nombre(nombre):
    """Busca clientes por nombre."""
    return database.buscar_clientes_por_nombre(nombre)


def actualizar_datos(id_cliente, nuevos_datos):
    """Actualiza datos de contacto de un cliente."""
    return database.actualizar_cliente(id_cliente, nuevos_datos)


def eliminar_cliente(id_cliente):
    """Elimina a un cliente de la base."""
    database.eliminar_cliente(id_cliente)

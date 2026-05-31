"""
Este módulo maneja la 'lógica' de los clientes.
Al igual que con los autos, separa lo que ve el usuario (el menú) 
de cómo se guardan los datos (la base de datos).
"""

import database


def registrar_cliente(datos):
    """Le pide a la base de datos que registre a un nuevo cliente."""
    return database.guardar_cliente(datos)


def listar_todos():
    """Trae la lista de todos los clientes de la base de datos."""
    return database.obtener_todos_clientes()


def buscar_por_dni(dni):
    """Busca un cliente específico por su número de DNI."""
    return database.buscar_cliente_por_dni(dni)


def buscar_por_nombre(nombre):
    """Busca clientes que tengan un nombre similar al que escribimos."""
    return database.buscar_clientes_por_nombre(nombre)


def actualizar_datos(id_cliente, nuevos_datos):
    """Actualiza los datos de contacto de un cliente existente."""
    return database.actualizar_cliente(id_cliente, nuevos_datos)


def eliminar_cliente(id_cliente):
    """Borra a un cliente de la base de datos."""
    database.eliminar_cliente(id_cliente)

"""
Este módulo maneja la 'lógica' de los autos. 
Sirve como un puente: el menú le pide cosas a este archivo, 
y este archivo se comunica con la base de datos (database.py).
"""

import database


def guardar_auto(datos):
    """Le pide a la base de datos que guarde un auto nuevo."""
    database.guardar_auto(datos)


def seleccionar_todos():
    """Trae la lista completa de autos desde la base de datos."""
    return database.obtener_todos()


def seleccionar_por(columna, valor):
    """Busca autos filtrando por una columna (ej: 'marca') y un valor (ej: 'Fiat')."""
    return database.buscar_por_campo(columna, valor)


def seleccionar_por_rango(minimo, maximo):
    """Trae los autos que estén entre un precio mínimo y uno máximo."""
    return database.buscar_por_rango_precio(minimo, maximo)


def seleccionar_auto_por_patente(patente):
    """Busca un solo auto usando su patente."""
    return database.buscar_por_patente(patente)


def seleccionar_auto_por_numero_interno(numero_interno):
    """Busca un solo auto usando su ID o número interno."""
    return database.buscar_por_id(numero_interno)


def cambiar_estado(id_auto, estado):
    """Actualiza el estado de un auto (ej: ponerlo como 'Vendido')."""
    database.cambiar_estado(id_auto, estado)


def dar_de_baja(id_auto):
    """Elimina físicamente un auto de la base de datos."""
    database.dar_de_baja(id_auto)

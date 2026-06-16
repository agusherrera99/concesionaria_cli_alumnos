"""
Este archivo funciona como nuestra base de datos.
Ahora usamos archivos JSON para que los datos NO se borren al cerrar el programa.

alumna: Maria Laura Castro
programacion I UNER
"""

import json
import os
from pathlib import Path

from stock_autos import auto_cliente

# Nombres de nuestros "archivos-base de datos"
BASE_DIR = Path(__file__).resolve().parent  #busca la ruta donde está el archivo que llama a la constante
CARPETA_RAIZ = BASE_DIR.parent # bajamos un nivel en la ruta
CARPETA_DATOS = CARPETA_RAIZ /'base_datos' #indicamos que ruta usar desde el nivel donde nos dejó la constante anterior
ARCHIVO_CLIENTES = "clientes.json"
RUTA_CLIENTES = CARPETA_DATOS / ARCHIVO_CLIENTES #ruta completa donde se guardará el archivo

CARPETA_DATOS.mkdir(parents=True, exist_ok=True) #crea la carpeta si no existe
# --- ALMACENAMIENTO TEMPORAL EN MEMORIA ---

lista_de_clientes = []
contador_id_clientes = 0
compra = []
reserva = []

# ============================================================
# FUNCIONES PARA MANEJAR ARCHIVOS (JSON)
# ============================================================

def guardar_datos_en_json():
    """
    Toma las listas que tenemos en memoria y las guarda en archivos .json.
    Así, la próxima vez que abramos el programa, los datos seguirán ahí.
    """

    # Guardamos los clientes
    data_clientes = {
        "contador": contador_id_clientes,
        "lista": lista_de_clientes
    }
    with open(RUTA_CLIENTES, "w") as f:
        json.dump(data_clientes, f, indent=4)


def cargar_datos_desde_json():
    """
    Lee los archivos .json al inicio del programa para llenar nuestras listas.
    """
    global lista_de_clientes, contador_id_clientes
    
    # Cargamos Clientes
    if os.path.exists(RUTA_CLIENTES):
        with open(RUTA_CLIENTES, "r") as f:
            data = json.load(f)
            lista_de_clientes = data["lista"]
            contador_id_clientes = data["contador"]
    return lista_de_clientes, contador_id_clientes


# Llamamos a esta función apenas se importa este archivo para cargar todo
cargar_datos_desde_json()


# ============================================================
# FUNCIONES PARA GESTIONAR CLIENTES
# ============================================================

def obtener_todos_clientes():
    """Devuelve la lista de todos nuestros clientes."""
    return lista_de_clientes


def guardar_cliente(datos_cliente):
    """Registra un cliente nuevo y guarda en el archivo JSON."""
    global contador_id_clientes, compra, reserva
    
    contador_id_clientes += 1
    
    cliente_dict = {
        "id": contador_id_clientes,
        "dni": datos_cliente["dni"],
        "nombre": datos_cliente["nombre"],
        "telefono": datos_cliente["telefono"],
        "email": datos_cliente.get("email", ""),
        "localidad": datos_cliente["localidad"],
        "busqueda": datos_cliente["busqueda"],
        "compras": compra,
        "reservas": reserva,
    }
    
    lista_de_clientes.append(cliente_dict)
    
    
    guardar_datos_en_json()
    return cliente_dict["id"]


def buscar_cliente_por_dni(dni):
    """Busca un cliente exacto por su número de documento."""
    for cliente in lista_de_clientes:
        if cliente["dni"] == dni:
            return cliente
    return None


def buscar_clientes_por_nombre(nombre):
    """Busca clientes que tengan ese nombre (o parte de él)."""
    nombre_buscado = nombre.capitalize()
    resultados = []
    for c in lista_de_clientes:
        if nombre_buscado in c["nombre"].capitalize():
            resultados.append(c)
    return resultados


def actualizar_cliente(id_cliente, nuevos_datos):
    """Actualiza datos de un cliente y guarda en el JSON."""
    for cliente in lista_de_clientes:
        if cliente["id"] == id_cliente:
            cliente.update(nuevos_datos)
            guardar_datos_en_json()
            return True
    return False


def eliminar_cliente(id_cliente):
    """Borra a un cliente y actualiza el archivo JSON."""
    global lista_de_clientes
    nueva_lista = []
    for c in lista_de_clientes:
        if c["id"] != id_cliente:
            nueva_lista.append(c)
    lista_de_clientes = nueva_lista
    guardar_datos_en_json()

def compra_auto (stock_autos, patente):
    auto = auto_cliente (stock_autos, patente)
    
    if auto:
        compra.append (auto)
    

def reserva_auto ():
    
    pass
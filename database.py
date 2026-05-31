"""
Este archivo funciona como nuestra base de datos.
Ahora usamos archivos JSON para que los datos NO se borren al cerrar el programa.
"""

import json
import os

# Nombres de nuestros "archivos-base de datos"
ARCHIVO_AUTOS = "autos.json"
ARCHIVO_CLIENTES = "clientes.json"

# --- ALMACENAMIENTO TEMPORAL EN MEMORIA ---
lista_de_autos = []
contador_id_autos = 1

lista_de_clientes = []
contador_id_clientes = 1


# ============================================================
# FUNCIONES PARA MANEJAR ARCHIVOS (JSON)
# ============================================================

def guardar_datos_en_json():
    """
    Toma las listas que tenemos en memoria y las guarda en archivos .json.
    Así, la próxima vez que abramos el programa, los datos seguirán ahí.
    """
    # Guardamos los autos
    data_autos = {
        "contador": contador_id_autos,
        "lista": lista_de_autos
    }
    # Usamos 'w' (write) para escribir el archivo
    with open(ARCHIVO_AUTOS, "w") as f:
        # json.dump convierte diccionarios/listas de Python a formato JSON
        # default=str es para que sepa cómo guardar las fechas (date)
        json.dump(data_autos, f, indent=4, default=str)

    # Guardamos los clientes
    data_clientes = {
        "contador": contador_id_clientes,
        "lista": lista_de_clientes
    }
    with open(ARCHIVO_CLIENTES, "w") as f:
        json.dump(data_clientes, f, indent=4)


def cargar_datos_desde_json():
    """
    Lee los archivos .json al inicio del programa para llenar nuestras listas.
    """
    global lista_de_autos, contador_id_autos, lista_de_clientes, contador_id_clientes

    # Cargamos Autos
    if os.path.exists(ARCHIVO_AUTOS):
        with open(ARCHIVO_AUTOS, "r") as f:
            data = json.load(f)
            lista_de_autos = data["lista"]
            contador_id_autos = data["contador"]
    
    # Cargamos Clientes
    if os.path.exists(ARCHIVO_CLIENTES):
        with open(ARCHIVO_CLIENTES, "r") as f:
            data = json.load(f)
            lista_de_clientes = data["lista"]
            contador_id_clientes = data["contador"]

# Llamamos a esta función apenas se importa este archivo para cargar todo
cargar_datos_desde_json()


# ============================================================
# FUNCIONES PARA GESTIONAR AUTOS
# ============================================================

def obtener_todos():
    """Simplemente devuelve la lista completa de autos."""
    return lista_de_autos


def guardar_auto(datos_auto):
    """Recibe un auto nuevo, lo guarda en la lista y actualiza el archivo JSON."""
    global contador_id_autos
    
    auto_dict = {
        "id": contador_id_autos,
        "patente": datos_auto[0],
        "marca": datos_auto[1],
        "modelo": datos_auto[2],
        "anio": datos_auto[3],
        "kilometros": datos_auto[4],
        "precio": datos_auto[5],
        "estado": datos_auto[6],
        "fecha_ingreso": str(datos_auto[7]), # Lo pasamos a texto para JSON
    }
    
    lista_de_autos.append(auto_dict)
    contador_id_autos += 1
    
    # ¡Importante! Después de cambiar la lista, guardamos en el archivo
    guardar_datos_en_json()


def buscar_por_campo(campo, valor):
    """Busca autos que coincidan con un valor en un campo específico."""
    resultados = []
    for auto in lista_de_autos:
        if str(auto[campo]).lower() == str(valor).lower():
            resultados.append(auto)
    return resultados


def buscar_por_rango_precio(minimo, maximo):
    """Busca autos que estén dentro de un rango de precios."""
    resultados = []
    for auto in lista_de_autos:
        if minimo <= auto["precio"] <= maximo:
            resultados.append(auto)
    return resultados


def buscar_por_patente(patente):
    """Busca un auto específico usando su patente."""
    for auto in lista_de_autos:
        if auto["patente"].lower() == patente.lower():
            return auto
    return None


def buscar_por_id(id_auto):
    """Busca un auto específico usando su número interno (ID)."""
    for auto in lista_de_autos:
        if auto["id"] == id_auto:
            return auto
    return None


def cambiar_estado(id_auto, nuevo_estado):
    """Busca el auto por su ID, cambia su estado y guarda en el JSON."""
    for auto in lista_de_autos:
        if auto["id"] == id_auto:
            auto["estado"] = nuevo_estado
            break
    guardar_datos_en_json()


def dar_de_baja(id_auto):
    """Elimina un auto y actualiza el archivo JSON."""
    global lista_de_autos
    nueva_lista = []
    for auto in lista_de_autos:
        if auto["id"] != id_auto:
            nueva_lista.append(auto)
    lista_de_autos = nueva_lista
    guardar_datos_en_json()


# ============================================================
# FUNCIONES PARA GESTIONAR CLIENTES
# ============================================================

def obtener_todos_clientes():
    """Devuelve la lista de todos nuestros clientes."""
    return lista_de_clientes


def guardar_cliente(datos_cliente):
    """Registra un cliente nuevo y guarda en el archivo JSON."""
    global contador_id_clientes
    
    cliente_dict = {
        "id": contador_id_clientes,
        "dni": datos_cliente["dni"],
        "nombre": datos_cliente["nombre"],
        "telefono": datos_cliente["telefono"],
        "email": datos_cliente.get("email", ""),
        "localidad": datos_cliente["localidad"],
        "busqueda": datos_cliente["busqueda"],
        "compras": [],
        "reservas": [],
    }
    
    lista_de_clientes.append(cliente_dict)
    contador_id_clientes += 1
    
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
    nombre_buscado = nombre.lower()
    resultados = []
    for c in lista_de_clientes:
        if nombre_buscado in c["nombre"].lower():
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

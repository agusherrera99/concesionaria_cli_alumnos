"""
Este archivo funciona como nuestra base de datos.
Como todavía no usamos archivos o bases de datos reales,
guardamos todo en listas de Python mientras el programa esté prendido.
"""

# --- ALMACENAMIENTO DE AUTOS ---
# Usamos una lista para guardar cada auto (que será un diccionario)
lista_de_autos = []
# Este contador nos sirve para que cada auto tenga un número único (ID)
contador_id_autos = 1

# --- ALMACENAMIENTO DE CLIENTES ---
lista_de_clientes = []
contador_id_clientes = 1


# ============================================================
# FUNCIONES PARA GESTIONAR AUTOS
# ============================================================


def obtener_todos():
    """Simplemente devuelve la lista completa de autos que tenemos."""
    return lista_de_autos


def guardar_auto(datos_auto):
    """
    Recibe los datos de un auto nuevo, le asigna un ID único
    y lo guarda en nuestra lista de stock.
    """
    global contador_id_autos

    # Creamos un diccionario para que los datos estén organizados y sean fáciles de leer
    auto_dict = {
        "id": contador_id_autos,
        "patente": datos_auto[0],
        "marca": datos_auto[1],
        "modelo": datos_auto[2],
        "anio": datos_auto[3],
        "kilometros": datos_auto[4],
        "precio": datos_auto[5],
        "estado": datos_auto[6],
        "fecha_ingreso": datos_auto[7],
    }

    lista_de_autos.append(auto_dict)
    # Sumamos 1 para que el próximo auto tenga el número siguiente
    contador_id_autos += 1


def buscar_por_campo(campo, valor):
    """
    Busca autos que coincidan con un valor en un campo específico.
    Por ejemplo: buscar todos los que tengan la marca 'Ford'.
    """
    # Creamos una lista vacía para ir guardando los que coincidan
    resultados = []
    for auto in lista_de_autos:
        # Si el valor del auto coincide con lo que buscamos...
        if str(auto[campo]).lower() == str(valor).lower():
            # ... lo agregamos a nuestra lista de resultados
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
    return None # Si no lo encuentra, devuelve 'nada'


def buscar_por_id(id_auto):
    """Busca un auto específico usando su número interno (ID)."""
    for auto in lista_de_autos:
        if auto["id"] == id_auto:
            return auto
    return None


def cambiar_estado(id_auto, nuevo_estado):
    """Busca el auto por su ID y le cambia el estado (ej: de 'Disponible' a 'Vendido')."""
    for auto in lista_de_autos:
        if auto["id"] == id_auto:
            auto["estado"] = nuevo_estado
            break


def dar_de_baja(id_auto):
    """Elimina definitivamente un auto de nuestra lista de stock."""
    global lista_de_autos
    # Creamos una lista nueva donde pondremos todos los que NO queremos borrar
    nueva_lista = []
    for auto in lista_de_autos:
        if auto["id"] != id_auto:
            nueva_lista.append(auto)
    # Reemplazamos la lista vieja por la nueva
    lista_de_autos = nueva_lista


# ============================================================
# FUNCIONES PARA GESTIONAR CLIENTES
# ============================================================

def obtener_todos_clientes():
    """Devuelve la lista de todos nuestros clientes registrados."""
    return lista_de_clientes


def guardar_cliente(datos_cliente):
    """
    Registra un cliente nuevo asignándole un ID autoincremental.
    """
    global contador_id_clientes

    cliente_dict = {
        "id": contador_id_clientes,
        "dni": datos_cliente["dni"],
        "nombre": datos_cliente["nombre"],
        "telefono": datos_cliente["telefono"],
        "email": datos_cliente.get("email", ""),
        "localidad": datos_cliente["localidad"],
        "busqueda": datos_cliente["busqueda"],
        "compras": [],  # Acá guardaremos los IDs de los autos que compre
        "reservas": [], # Acá guardaremos los IDs de los autos que reserve
    }

    lista_de_clientes.append(cliente_dict)
    contador_id_clientes += 1
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
    """Busca al cliente y actualiza sus datos de contacto."""
    for cliente in lista_de_clientes:
        if cliente["id"] == id_cliente:
            # .update() pisa los datos viejos con los nuevos que le pasemos
            cliente.update(nuevos_datos)
            return True
    return False


def eliminar_cliente(id_cliente):
    """Borra a un cliente de nuestra base (si pidió no figurar más)."""
    global lista_de_clientes
    nueva_lista = []
    for c in lista_de_clientes:
        if c["id"] != id_cliente:
            nueva_lista.append(c)
    lista_de_clientes = nueva_lista


from datetime import date

lista_de_autos = []
contador_id_autos = 1

lista_de_clientes = []
contador_id_clientes = 1


def obtener_todos():
    """Retorna la lista completa de autos."""
    return lista_de_autos


def guardar_auto(datos_auto):
    """Agrega un nuevo auto a la lista."""
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
        "fecha_ingreso": datos_auto[7],
    }
    lista_de_autos.append(auto_dict)
    contador_id_autos += 1


def buscar_por_campo(campo, valor):
    """Busca autos filtrando por una columna específica."""
    return [auto for auto in lista_de_autos if auto[campo] == valor]


def buscar_por_rango_precio(minimo, maximo):
    """Busca autos cuyo precio esté entre el mínimo y el máximo."""
    return [auto for auto in lista_de_autos if minimo <= auto["precio"] <= maximo]


def buscar_por_patente(patente):
    """Busca un único auto por su patente."""
    for auto in lista_de_autos:
        if auto["patente"] == patente:
            return auto
    return None


def buscar_por_id(id_auto):
    """Busca un único auto por su ID."""
    for auto in lista_de_autos:
        if auto["id"] == id_auto:
            return auto
    return None


def cambiar_estado(id_auto, nuevo_estado):
    """Actualiza el campo 'estado' de un auto específico."""
    for auto in lista_de_autos:
        if auto["id"] == id_auto:
            auto["estado"] = nuevo_estado
            break


def dar_de_baja(id_auto):
    """Elimina un registro de la lista."""
    global lista_de_autos
    lista_de_autos = [auto for auto in lista_de_autos if auto["id"] != id_auto]


# --- Funciones de Clientes ---

def obtener_todos_clientes():
    """Retorna la lista completa de clientes."""
    return lista_de_clientes


def guardar_cliente(datos_cliente):
    """Agrega un nuevo cliente a la lista."""
    global contador_id_clientes
    cliente_dict = {
        "id": contador_id_clientes,
        "dni": datos_cliente["dni"],
        "nombre": datos_cliente["nombre"],
        "telefono": datos_cliente["telefono"],
        "email": datos_cliente.get("email", ""),
        "localidad": datos_cliente["localidad"],
        "busqueda": datos_cliente["busqueda"],
        "compras": [],  # Lista de IDs de autos comprados
        "reservas": [],  # Lista de IDs de autos reservados
    }
    lista_de_clientes.append(cliente_dict)
    contador_id_clientes += 1
    return cliente_dict["id"]


def buscar_cliente_por_dni(dni):
    """Busca un cliente por su DNI."""
    for cliente in lista_de_clientes:
        if cliente["dni"] == dni:
            return cliente
    return None


def buscar_clientes_por_nombre(nombre):
    """Busca clientes que coincidan con el nombre (parcial)."""
    return [c for c in lista_de_clientes if nombre.lower() in c["nombre"].lower()]


def actualizar_cliente(id_cliente, nuevos_datos):
    """Actualiza datos de contacto de un cliente."""
    for cliente in lista_de_clientes:
        if cliente["id"] == id_cliente:
            cliente.update(nuevos_datos)
            return True
    return False


def eliminar_cliente(id_cliente):
    """Elimina un cliente de la lista."""
    global lista_de_clientes
    lista_de_clientes = [c for c in lista_de_clientes if c["id"] != id_cliente]

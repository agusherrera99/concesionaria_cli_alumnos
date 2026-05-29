from datetime import date

lista_de_autos = []
contador_id = 1


def obtener_todos():
    """Retorna la lista completa de autos."""
    return lista_de_autos


def guardar_auto(datos_auto):
    """Agrega un nuevo auto a la lista."""
    global contador_id
    auto_dict = {
        "id": contador_id,
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
    contador_id += 1


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

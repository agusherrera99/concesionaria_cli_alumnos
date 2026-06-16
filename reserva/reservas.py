import json
from pathlib import Path
from validaciones2 import ingresar_entero, ingresar_float, ingresar_fecha, confirmacion, mensaje
from datetime import date
import sys
_dir_stock_autos = Path(__file__).resolve().parent.parent / "autos" / "stock_autos"
if str(_dir_stock_autos) not in sys.path:
    sys.path.append(str(_dir_stock_autos))
from archivo2 import cargar_stock, guardar_stock


# Ruta del archivo reserva.json en la raíz del módulo (carpeta reservas)
RUTA_RESERVA = Path(__file__).resolve().parent / "reserva.json"

# Tupla con los estados posibles de la reserva
ESTADOS_RESERVA = ('activa', 'concretada', 'cancelada')


def cargar_reservas():
    """
    Carga las reservas desde el archivo reserva.json.
    Si el archivo no existe o está vacío, retorna una lista vacía.
    """
    if not RUTA_RESERVA.exists():
        return []
    try:
        with open(RUTA_RESERVA, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def guardar_reservas(reservas_lista):
    """
    Guarda la lista de reservas en el archivo reserva.json.
    """
    try:
        with open(RUTA_RESERVA, "w", encoding="utf-8") as archivo:
            json.dump(reservas_lista, archivo, indent=4, ensure_ascii=False)
            archivo.write('\n')
    except Exception as e:
        mensaje(f"Error al guardar los datos: {e}")


def seleccionar_estado() -> str:
    """
    Muestra un menú para seleccionar el estado de la reserva a partir de la tupla.
    """
    while True:
        print("\n================ ESTADO DE LA RESERVA ================")
        for i, est in enumerate(ESTADOS_RESERVA, 1):
            print(f"{i}.- {est.capitalize()}")
        print("======================================================")
        
        opc = ingresar_entero("Seleccione el estado: ")
        if 1 <= opc <= len(ESTADOS_RESERVA):
            return ESTADOS_RESERVA[opc - 1]
        else:
            mensaje("Opción no válida. Intente nuevamente.")


def registrar_reserva():
    print("\n================ REGISTRAR RESERVA ================")
    id_auto = ingresar_entero("Ingrese el id del auto: ")
    id_cliente = ingresar_entero("Ingrese el id del cliente: ")
    id_vendedor = ingresar_entero("Ingrese el id del vendedor: ")
    fecha_res = date.today()
    monto_s = ingresar_float("Ingrese el monto de la seña: ")
    fecha_lim = ingresar_fecha("Ingrese la fecha limite (YYYY-MM-DD): ")
    estado = "Activa"
    
    if confirmacion("\n¿Desea registrar esta reserva? (S/N): ") == 'N':
        mensaje("\nOperación cancelada.")
        return

    # Cargar reservas existentes (maneja si no existe el archivo)
    reservas_lista = cargar_reservas()

    # Calcular ID autoincremental para la nueva reserva
    id_reserva = max([r.get("id", 0) for r in reservas_lista], default=0) + 1

    nueva_reserva = {
        "id": id_reserva,
        "id_auto": id_auto,
        "id_cliente": id_cliente,
        "id_vendedor": id_vendedor,
        "fecha_reserva": fecha_res.isoformat(),
        "monto_sena": monto_s,
        "fecha_limite": fecha_lim.isoformat(),
        "estado": estado
    }

    # Agregar la nueva reserva a la lista
    reservas_lista.append(nueva_reserva)
    
    # Guardar en archivo reserva.json
    guardar_reservas(reservas_lista)
    
    mensaje(f"\nReserva registrada correctamente. ID de Reserva: {id_reserva}")


def listar_reservas():
    """
    Lista todas las reservas registradas en reserva.json para revisión.
    """
    reservas_lista = cargar_reservas()
    if not reservas_lista:
        mensaje("\nNo hay reservas registradas.")
        return

    print("\n================ LISTADO DE RESERVAS ================")
    for r in reservas_lista:
        print(f"ID Reserva:     {r.get('id')}")
        print(f"ID Auto:        {r.get('id_auto')}")
        print(f"ID Cliente:     {r.get('id_cliente')}")
        print(f"ID Vendedor:    {r.get('id_vendedor')}")
        print(f"Fecha Reserva:  {r.get('fecha_reserva')}")
        print(f"Monto Seña:     ${r.get('monto_sena'):.2f}")
        print(f"Fecha Límite:   {r.get('fecha_limite')}")
        print(f"Estado:         {str(r.get('estado')).upper()}")
        print("-" * 50)


def buscar_reservas(criterio: str, valor) -> list:
    """
    Filtra las reservas existentes en el archivo JSON mediante uno de estos tres criterios:
    id_auto, id_cliente o id_vendedor (o también de forma abreviada 'auto', 'cliente', 'vendedor').
    Recibe el criterio de búsqueda y el valor a buscar.
    Retorna la lista de reservas que coinciden con el valor proporcionado o una lista vacía si no hay coincidencias.
    """
    reservas_lista = cargar_reservas()
    
    # Mapear el criterio al nombre de la clave en la estructura de datos
    criterio_normalizado = criterio.lower().strip()
    if criterio_normalizado in ('id_auto', 'auto'):
        clave = 'id_auto'
    elif criterio_normalizado in ('id_cliente', 'cliente'):
        clave = 'id_cliente'
    elif criterio_normalizado in ('id_vendedor', 'vendedor'):
        clave = 'id_vendedor'
    else:
        return []

    coincidencias = []
    for reserva in reservas_lista:
        val_reserva = reserva.get(clave)
        
        # Como los ids suelen ser enteros, intentamos comparar como enteros para evitar fallas por tipo
        try:
            if int(val_reserva) == int(valor):
                coincidencias.append(reserva)
                continue
        except (ValueError, TypeError):
            pass
            
        if str(val_reserva) == str(valor):
            coincidencias.append(reserva)
            
    return coincidencias


def buscar_reservas_interactivo():
    """
    Pide al usuario el criterio y valor de búsqueda,
    llama a la función buscar_reservas e imprime los resultados en consola de forma legible.
    Si no hay coincidencias, informa al usuario.
    """
    print("\n================ BUSCAR RESERVA ================")
    print("1.- Buscar por ID de Auto")
    print("2.- Buscar por ID de Cliente")
    print("3.- Buscar por ID de Vendedor")
    print("0.- Volver")
    print("=================================================")
    
    opc = ingresar_entero("Seleccione el criterio de búsqueda: ")
    if opc == 0:
        return
        
    criterios = {1: "id_auto", 2: "id_cliente", 3: "id_vendedor"}
    criterio = criterios.get(opc)
    if not criterio:
        mensaje("Opción no válida.")
        return
        
    valor = ingresar_entero(f"Ingrese el ID del {criterio.split('_')[1]} a buscar: ")
    
    resultados = buscar_reservas(criterio, valor)
    
    if resultados:
        print(f"\n================ RESULTADOS DE BÚSQUEDA ================")
        print(f"Criterio: {criterio} = {valor}")
        print("=" * 55)
        for r in resultados:
            print(f"ID Reserva:     {r.get('id')}")
            print(f"ID Auto:        {r.get('id_auto')}")
            print(f"ID Cliente:     {r.get('id_cliente')}")
            print(f"ID Vendedor:    {r.get('id_vendedor')}")
            print(f"Fecha Reserva:  {r.get('fecha_reserva')}")
            monto = r.get('monto_sena')
            monto_str = f"${monto:.2f}" if isinstance(monto, (int, float)) else f"${monto}"
            print(f"Monto Seña:     {monto_str}")
            print(f"Fecha Límite:   {r.get('fecha_limite')}")
            print(f"Estado:         {str(r.get('estado')).upper()}")
            print("-" * 50)
    else:
        mensaje(f"No se encontraron reservas con {criterio} = {valor}.")

def cancelar_reserva():
    print("\n================ CANCELAR RESERVA ================")
    id_res = ingresar_entero("Ingrese el ID de la reserva a cancelar: ")
    reservas = cargar_reservas()
    res = next((r for r in reservas if r.get("id") == id_res), None)
    
    if not res:
        return mensaje(f"Error: No se encontró la reserva con ID {id_res}.")
    if str(res.get("estado", "")).lower() != "activa":
        return mensaje(f"Error: La reserva no está activa (Estado actual: '{res.get('estado')}').")
        
    if confirmacion("\n¿Desea cancelar esta reserva? (S/N): ") == 'N':
        return mensaje("\nOperación cancelada.")
        
    stock = cargar_stock()
    auto = next((a for a in stock if a.get("Id", a.get("id")) == res.get("id_auto")), None)
    if auto:
        auto["Estado" if "Estado" in auto else "estado"] = "Disponible"
        guardar_stock(stock)
    else:
        print(f"Advertencia: Auto ID {res.get('id_auto')} no encontrado en stock.")
        
    res["estado"] = "Cancelada"
    guardar_reservas(reservas)
    mensaje(f"\nReserva ID {id_res} cancelada con éxito. El vehículo asociado vuelve a estar 'Disponible'.")


def menu_reservas(reservas_lista=None, stock_autos=None):
    """
    Bucle principal del módulo con un menú estético usando match-case.
    """
    while True:
        print("\n================ MENÚ RESERVAS ================")
        print("1.- Registrar una reserva")
        print("2.- Listar las reservas registradas")
        print("3.- Buscar reservas (por auto, cliente o vendedor)")
        print("4.- Concretar una reserva (convertir en venta)")
        print("5.- Cancelar una reserva")
        print("0.- Volver al menú principal")
        print("===============================================")

        opcion = ingresar_entero("Elija una opción: ")

        match opcion:
            case 1:
                registrar_reserva()
            case 2:
                listar_reservas()
            case 3:
                buscar_reservas_interactivo()
            case 5:
                cancelar_reserva()
            case 0:
                break
            case _:
                mensaje("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu_reservas()

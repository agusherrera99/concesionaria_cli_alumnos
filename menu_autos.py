import os
from inspect import cleandoc
from datetime import date
import auto

def iniciar():
    """Punto de entrada para este menú."""
    mostrar_menu_principal_autos()

# --- Funciones de Ayuda (Helper Functions) ---
def limpiar_menu():
    """Limpia la terminal dependiendo del sistema operativo."""
    os.system("cls" if os.name == "nt" else "clear")

def leer_entero(mensaje):
    """Pide un dato y verifica que sea un número entero."""
    while True:
        valor = input(cleandoc(mensaje))
        if valor.isdigit():
            return int(valor)
        print("\nEso no parece un número. Por favor, intenta de nuevo con números solamente.")

def seleccionar_estado():
    """Sub-menú para elegir un estado válido."""
    mensaje = """
    1. Disponible
    2. Reservado
    3. Vendido
    4. En taller

    Seleccionar un estado: """

    while True:
        opcion_seleccionada = input(cleandoc(mensaje))
        match opcion_seleccionada:
            case "1": return "disponible"
            case "2": return "reservado"
            case "3": return "vendido"
            case "4": return "en taller"
            case _:
                print("\nEsa opción no es válida. ¡Probá con una del 1 al 4!")
                input("Presioná Enter para intentar de nuevo...")

def pedir_confirmacion():
    """Pide confirmación antes de acciones críticas."""
    while True:
        confirmar = input("\n¿Confirmar acción? (1: Sí / 0: No): ")
        if confirmar == "1": return True
        if confirmar == "0": return False
        print("Por favor, ingresa 1 o 0.")

# --- Operaciones CRUD ---
def cargar_auto_nuevo():
    """CARGAR (Alta): Pide los datos y los guarda."""
    print("\n--- COMPLETAR DATOS DEL NUEVO AUTO ---")

    try:
        patente = input("Patente: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        anio = leer_entero("Año: ")
        kilometros = leer_entero("Kilometros: ")
        precio = leer_entero("Precio: ")
        estado = seleccionar_estado()
        fecha_ingreso_str = input("Fecha de Ingreso (DD/MM/AAAA): ")
        dia, mes, anio_fecha = map(int, fecha_ingreso_str.split('/'))
        fecha_ingreso = date(anio_fecha, mes, dia)

        print("\n¿Confirmas la carga de este auto?")
        if pedir_confirmacion():
            datos = (patente, marca, modelo, anio, kilometros, precio, estado, fecha_ingreso)
            auto.guardar_auto(datos)
            print("\n¡Excelente! El auto se guardó correctamente.")
        else:
            print("\nCarga cancelada. Volviendo al menú...")

        input("\nPresioná Enter para continuar...")
    except Exception as error:
        print(f"\nOcurrió un error inesperado: {error}")
        input("Presiona Enter para volver...")

def mostrar_resultados(listado, criterio):
    """Muestra los resultados de una búsqueda de forma prolija."""
    if listado:
        print(f"\nResultados encontrados para {criterio}:")
        for a in listado:
            print(f"ID: {a['id']} | Patente: {a['patente']} | Marca: {a['marca']} | Modelo: {a['modelo']} | Año: {a['anio']} | KM: {a['kilometros']} | Precio: {a['precio']} | Estado: {a['estado']} | Ingreso: {a['fecha_ingreso']}")
    else:
        print(f"\nNo encontré resultados para {criterio}.")
    input("\nPresiona Enter para volver")

def filtrar_listado():
    """Permite buscar grupos de autos por criterios."""
    mensaje = """
    ===============
    FILTRAR LISTADO
    ===============

    1. Por marca
    2. Por rango de precio
    3. Por estado
    0. Volver

    ¿Qué quieres hacer? """

    while True:
        limpiar_menu()
        opcion_seleccionada = input(cleandoc(mensaje))
        match opcion_seleccionada:
            case "1":
                marca = input("\nIngresa la marca a buscar: ")
                listado = auto.seleccionar_por("marca", marca)
                mostrar_resultados(listado, f"marca '{marca}'")
            case "2":
                minimo = leer_entero("\nPrecio mínimo: ")
                maximo = leer_entero("Precio máximo: ")
                listado = auto.seleccionar_por_rango(minimo, maximo)
                mostrar_resultados(listado, f"rango ${minimo} - ${maximo}")
            case "3":
                estado_buscado = seleccionar_estado()
                listado = auto.seleccionar_por("estado", estado_buscado)
                mostrar_resultados(listado, f"estado '{estado_buscado}'")
            case "0":
                break
            case _:
                print("\n¡Oops! Esa opción no existe.")
                input("Presiona Enter para volver a intentarlo...")

def ver_listado():
    """Muestra todos los autos o deriva al menú de filtros."""
    mensaje = """
    ================
    LISTADO DE AUTOS
    ================

    1. Ver listado completo
    2. Filtrar listado
    0. Volver

    ¿Qué quieres hacer? """

    while True:
        limpiar_menu()
        opcion_seleccionada = input(cleandoc(mensaje))
        match opcion_seleccionada:
            case "1":
                listado = auto.seleccionar_todos()
                if listado:
                    print("\n--- Listado Completo de Autos ---")
                    for a in listado:
                        print(f"ID: {a['id']} | Patente: {a['patente']} | Marca: {a['marca']} | Modelo: {a['modelo']} | Año: {a['anio']} | KM: {a['kilometros']} | Precio: {a['precio']} | Estado: {a['estado']} | Ingreso: {a['fecha_ingreso']}")
                else:
                    print("\nTodavía no hay autos cargados.")
                input("\nPresiona Enter para volver")
            case "2":
                filtrar_listado()
            case "0":
                break
            case _:
                print("\nEsa opción no es válida.")
                input("Presiona Enter para intentar de nuevo...")

def buscar_auto_por(tipo):
    """Busca un solo auto."""
    try:
        if tipo == "patente":
            patente = input("\nIngrese la patente: ")
            encontrado = auto.seleccionar_auto_por_patente(patente)
        else:
            numero_interno = leer_entero("\nIngrese el número interno: ")
            encontrado = auto.seleccionar_auto_por_numero_interno(numero_interno)

        if encontrado:
            print(f"\n¡AUTO ENCONTRADO!\nID: {encontrado['id']} | Patente: {encontrado['patente']} | Marca: {encontrado['marca']} | Modelo: {encontrado['modelo']} | Año: {encontrado['anio']} | KM: {encontrado['kilometros']} | Precio: {encontrado['precio']} | Estado: {encontrado['estado']} | Ingreso: {encontrado['fecha_ingreso']}")
        else:
            print("\nLo siento, no pude encontrar ningún auto con ese dato.")
        return encontrado
    except Exception as error:
        print(f"Hubo un problemita al buscar: {error}")
        return None

def buscar_auto(con_pausa=True):
    """Menú de búsqueda individual."""
    mensaje = """
    =============
    BUSCAR AUTO
    =============

    1. Por patente
    2. Por número interno
    0. Volver

    ¿Qué quieres hacer? """

    while True:
        limpiar_menu()
        opcion_seleccionada = input(cleandoc(mensaje))
        match opcion_seleccionada:
            case "1" | "2":
                tipo = "patente" if opcion_seleccionada == "1" else "numero_interno"
                encontrado = buscar_auto_por(tipo)
                if not encontrado:
                    input("\nPresiona Enter para intentar de nuevo...")
                    continue
                if con_pausa: 
                    input("\nPresionar Enter para volver")
                return encontrado
            case "0":
                break
            case _:
                print("\nEsa opción no es válida.")
                input("Presiona Enter para intentar de nuevo...")

def cambiar_estado():
    """MODIFICAR (Actualizar): Permite cambiar el estado de un auto."""
    mensaje = """
    =========================
    CAMBIAR ESTADO DE UN AUTO
    =========================

    1. Seleccionar auto
    0. Volver

    ¿Qué quieres hacer? """

    while True:
        limpiar_menu()
        opcion_seleccionada = input(cleandoc(mensaje))
        match opcion_seleccionada:
            case "1":
                encontrado = buscar_auto(con_pausa=False)
                if encontrado:
                    numero_interno = encontrado["id"]
                    print("\nSelecciona el nuevo estado:")
                    nuevo_estado = seleccionar_estado()
                    auto.cambiar_estado(numero_interno, nuevo_estado)
                    print(f"\n¡Listo! Estado actualizado a '{nuevo_estado}'.")
                input("\nPresionar Enter para volver")
            case "0":
                break
            case _:
                print("\n¡Oops! Opción no válida.")
                input("Presiona Enter para intentar de nuevo...")

def dar_de_baja_un_auto():
    """ELIMINAR (Baja): Borra un registro."""
    mensaje = """
    ===================
    DAR DE BAJA UN AUTO
    ===================

    1. Seleccionar auto para eliminar
    0. Volver

    ¿Qué quieres hacer? """

    while True:
        limpiar_menu()
        opcion_seleccionada = input(cleandoc(mensaje))
        match opcion_seleccionada:
            case "1":
                encontrado = buscar_auto(con_pausa=False)
                if encontrado:
                    print("\n¡ATENCIÓN! Esta acción no se puede deshacer.")
                    if pedir_confirmacion():
                        auto.dar_de_baja(encontrado["id"])
                        print("\nEl auto ha sido eliminado.")
                    else:
                        print("\nOperación cancelada. El auto sigue en el sistema.")
                input("\nPresionar Enter para volver")
            case "0":
                break
            case _:
                print("\nOpción no válida.")
                input("Presiona Enter para intentar de nuevo...")

def mostrar_menu_principal_autos():
    """Corazón del área de autos."""
    mensaje = """
    ==============
    AUTOS EN STOCK
    ==============

    1. Cargar un auto nuevo
    2. Ver listado de autos
    3. Buscar un auto
    4. Cambiar estado de un auto
    5. Dar de baja un auto
    0. Volver a la pantalla principal

    ¿Qué quieres hacer? """

    while True:
        limpiar_menu()
        opcion_seleccionada = input(cleandoc(mensaje))
        match opcion_seleccionada:
            case "1": cargar_auto_nuevo()
            case "2": ver_listado()
            case "3": buscar_auto()
            case "4": cambiar_estado()
            case "5": dar_de_baja_un_auto()
            case "0": break
            case _:
                print("\n¡Oops! Esa opción no existe.")
                input("Presiona Enter para volver a intentarlo...")

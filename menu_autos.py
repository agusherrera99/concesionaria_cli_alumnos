"""
En este archivo manejamos toda la interacción con el usuario 
referida a los autos en stock.
"""

import os
from inspect import cleandoc
from datetime import date
import auto


def iniciar():
    """Arranca el menú de gestión de stock."""
    mostrar_menu_principal_autos()


# --- FUNCIONES DE AYUDA (Para no repetir código) ---

def limpiar_menu():
    """Limpia la pantalla según el sistema operativo."""
    os.system("cls" if os.name == "nt" else "clear")


def leer_entero(mensaje):
    """
    Esta función es muy útil: pide un dato y se asegura 
    de que el usuario escriba un número y no letras.
    """
    while True:
        valor = input(cleandoc(mensaje))
        if valor.isdigit():
            return int(valor)
        print("\n¡Error! Por favor, ingresá un número (sin puntos ni letras).")


def seleccionar_estado():
    """Pone opciones fijas para el estado del auto y evita errores de escritura."""
    mensaje = """
    1. Disponible
    2. Reservado
    3. Vendido
    4. En taller

    Elegí el número del estado: """

    while True:
        opcion = input(cleandoc(mensaje))
        match opcion:
            case "1": return "disponible"
            case "2": return "reservado"
            case "3": return "vendido"
            case "4": return "en taller"
            case _:
                print("\nOpción inválida. Elegí del 1 al 4.")


def pedir_confirmacion():
    """Pide un Sí o un No para acciones importantes."""
    while True:
        confirmar = input("\n¿Estás seguro? (1: Sí / 0: No): ")
        if confirmar == "1": return True
        if confirmar == "0": return False
        print("Escribí 1 para Sí o 0 para No.")


# --- FUNCIONES PRINCIPALES DEL MENÚ ---

def cargar_auto_nuevo():
    """Pide los datos de un auto y le pide a la lógica que lo guarde."""
    print("\n--- COMPLETAR DATOS DEL NUEVO AUTO ---")

    try:
        patente = input("Patente: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        anio = leer_entero("Año de fabricación: ")
        kilometros = leer_entero("Kilómetros actuales: ")
        precio = leer_entero("Precio de venta: ")
        estado = seleccionar_estado()
        
        # Para la fecha, pedimos los datos por separado para no complicar al alumno
        fecha_str = input("Fecha de hoy (DD/MM/AAAA): ")
        dia, mes, anio_f = map(int, fecha_str.split('/'))
        fecha_ingreso = date(anio_f, mes, dia)

        if pedir_confirmacion():
            # Juntamos todo en una 'tupla' para mandarlo más fácil
            datos = (patente, marca, modelo, anio, kilometros, precio, estado, fecha_ingreso)
            auto.guardar_auto(datos)
            print("\n¡Genial! El auto se cargó al stock.")
        else:
            print("\nCarga cancelateda.")

        input("\nPresiona Enter para continuar...")
    except Exception as e:
        print(f"\nOops, algo salió mal: {e}")
        input("Presiona Enter para volver...")


def mostrar_resultados(listado, criterio):
    """Muestra una lista de autos de forma prolija en pantalla."""
    if listado:
        print(f"\n--- Resultados para: {criterio} ---")
        for a in listado:
            print(f"ID: {a['id']} | {a['marca']} {a['modelo']} ({a['patente']}) | ${a['precio']} | {a['estado']}")
    else:
        print(f"\nNo encontré nada para {criterio}.")
    input("\nPresiona Enter para volver...")


def filtrar_listado():
    """Permite buscar autos por marca, precio o estado."""
    mensaje = """
    =================
    FILTRAR STOCK
    =================

    1. Por Marca
    2. Por Rango de Precio
    3. Por Estado
    0. Volver

    ¿Cómo quieres filtrar? """

    while True:
        limpiar_menu()
        opcion = input(cleandoc(mensaje))
        match opcion:
            case "1":
                marca = input("\n¿Qué marca buscás?: ")
                resultados = auto.seleccionar_por("marca", marca)
                mostrar_resultados(resultados, marca)
            case "2":
                min_p = leer_entero("\nPrecio mínimo: ")
                max_p = leer_entero("Precio máximo: ")
                resultados = auto.seleccionar_por_rango(min_p, max_p)
                mostrar_resultados(resultados, f"Precio entre ${min_p} y ${max_p}")
            case "3":
                est = seleccionar_estado()
                resultados = auto.seleccionar_por("estado", est)
                mostrar_resultados(resultados, est)
            case "0": break


def ver_listado_completo():
    """Muestra absolutamente todos los autos que tenemos."""
    listado = auto.seleccionar_todos()
    if listado:
        print("\n--- STOCK COMPLETO ---")
        for a in listado:
            print(f"ID: {a['id']} | {a['marca']} {a['modelo']} | Patente: {a['patente']} | ${a['precio']} | {a['estado']}")
    else:
        print("\nTodavía no hay autos en el sistema.")
    input("\nPresiona Enter para volver...")


def buscar_auto_individual():
    """Busca un auto específico para ver sus detalles."""
    print("\n1. Buscar por Patente")
    print("2. Buscar por ID Interno")
    op = input("Elegí una opción: ")
    
    if op == "1":
        pat = input("Escribí la patente: ")
        encontrado = auto.seleccionar_auto_por_patente(pat)
    else:
        idx = leer_entero("Escribí el ID: ")
        encontrado = auto.seleccionar_auto_por_numero_interno(idx)

    if encontrado:
        print("\n--- AUTO ENCONTRADO ---")
        for clave, valor in encontrado.items():
            print(f"{clave.capitalize()}: {valor}")
    else:
        print("\nNo encontré ningún auto con ese dato.")
    input("\nPresiona Enter para volver...")


def cambiar_estado_auto():
    """Busca un auto y le cambia el estado (ej: si se vendió)."""
    idx = leer_entero("\nIngresá el ID del auto a modificar: ")
    encontrado = auto.seleccionar_auto_por_numero_interno(idx)
    
    if encontrado:
        print(f"\nModificando {encontrado['marca']} {encontrado['modelo']}")
        print(f"Estado actual: {encontrado['estado']}")
        nuevo = seleccionar_estado()
        auto.cambiar_estado(idx, nuevo)
        print("¡Estado actualizado!")
    else:
        print("No encontré un auto con ese ID.")
    input("\nPresiona Enter para continuar...")


def borrar_auto():
    """Elimina un auto del sistema."""
    idx = leer_entero("\nIngresá el ID del auto a eliminar: ")
    encontrado = auto.seleccionar_auto_por_numero_interno(idx)
    
    if encontrado:
        print(f"\nVas a borrar el auto: {encontrado['marca']} {encontrado['modelo']}")
        if pedir_confirmacion():
            auto.dar_de_baja(idx)
            print("Auto eliminado del stock.")
        else:
            print("Acción cancelada.")
    else:
        print("No encontré ese auto.")
    input("\nPresiona Enter para continuar...")


def mostrar_menu_principal_autos():
    """El menú central de la sección de autos."""
    mensaje = """
    ====================
    GESTIÓN DE STOCK
    ====================

    1. Cargar un auto nuevo
    2. Ver stock completo
    3. Filtrar stock (Búsquedas)
    4. Ver detalle de un auto
    5. Cambiar estado (Vendido, Reservado, etc.)
    6. Eliminar un auto
    0. Volver al inicio

    ¿Qué quieres hacer? """

    while True:
        limpiar_menu()
        opcion = input(cleandoc(mensaje))
        match opcion:
            case "1": cargar_auto_nuevo()
            case "2": ver_listado_completo()
            case "3": filtrar_listado()
            case "4": buscar_auto_individual()
            case "5": cambiar_estado_auto()
            case "6": borrar_auto()
            case "0": break
            case _:
                print("\nOpción inválida.")
                input("Presiona Enter para continuar...")

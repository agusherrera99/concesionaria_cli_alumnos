"""
En este archivo manejamos toda la interacción con el usuario
referida a la gestión de clientes.

alumna: Maria Laura Castro
programacion I UNER
"""

import os
from rich.table import Table
from rich.console import Console

from .cliente import (
    buscar_por_dni,
    buscar_por_nombre,
    registrar_cliente,
    listar_todos,
    actualizar_datos,
    eliminar_cliente,
)
from .mensaje_menu import mensaje
from .validaciones import ingresar_entero


console = Console()


def limpiar_pantalla():
    """Limpia la terminal para mantener el orden."""
    os.system("cls" if os.name == "nt" else "clear")


def iniciar():
    """Arranca el menú de clientes."""
    while True:
        limpiar_pantalla()

        mensaje("GESTIÓN DE CLIENTES")

        print("1. Registrar nuevo cliente")
        print("2. Listar todos los clientes")
        print("3. Buscar cliente por DNI")
        print("4. Buscar cliente por Nombre")
        print("5. Actualizar datos de contacto")
        print("6. Eliminar cliente de la base")
        print("0. Volver al menú principal")

        opcion = ingresar_entero("¿Qué queres hacer?: ")

        match opcion:
            case 1:
                registrar_nuevo_cliente()
            case 2:
                mostrar_todos_los_clientes()
            case 3:
                buscar_cliente_dni()
            case 4:
                buscar_cliente_nombre()
            case 5:
                actualizar_datos_cliente()
            case 6:
                dar_de_baja_cliente()
            case 0:
                break
            case _:
                mensaje("\nOpción no válida.")
                input("Presiona Enter para continuar...")


def registrar_nuevo_cliente():
    """Pide los datos para dar de alta a un cliente nuevo."""
    print("\n--- REGISTRO DE NUEVO CLIENTE ---")
    dni = ingresar_entero("DNI: ")

    # Primero chequeamos que no esté ya registrado
    if buscar_por_dni(dni):
        print("¡Ojo! Ya tenemos un cliente con ese DNI.")
        input("Presiona Enter para volver...")
        return

    nombre = input("Nombre completo: ").capitalize()
    telefono = input("Teléfono: ")
    email = input("Email (si no tiene, dejar vacío): ").lower()
    localidad = input("Localidad: ").capitalize()
    busqueda = input("¿Qué tipo de auto está buscando?: ").upper()

    # Organizamos los datos en un diccionario
    datos = {
        "dni": dni,
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "localidad": localidad,
        "busqueda": busqueda,
    }

    # Se lo mandamos a la lógica para que lo guarde
    id_cliente = registrar_cliente(datos)
    print(f"\n¡Listo! Cliente guardado. Su número de cliente es: {id_cliente}")
    input("Presiona Enter para continuar...")


def mostrar_todos_los_clientes():
    """Muestra una lista de todos los clientes en una tabla."""
    lista = listar_todos()
    if not lista:
        print("\nNo hay clientes cargados todavía.")
    else:
        table = Table(title="Listado de Clientes")
        table.add_column("ID", style="cyan")
        table.add_column("DNI", style="magenta")
        table.add_column("Nombre", style="green")

        for c in lista:
            table.add_row(str(c["id"]), str(c["dni"]), c["nombre"])

        console.print(table)
    input("\nPresiona Enter para volver...")


def buscar_cliente_dni():
    """Busca y muestra el detalle de un cliente por su DNI."""
    dni = input("\nIngresa el DNI que querés buscar: ")
    c = buscar_por_dni(dni)
    if c:
        mostrar_detalle_cliente(c)
    else:
        print("No encontré ningún cliente con ese DNI.")
    input("Presiona Enter para continuar...")


def buscar_cliente_nombre():
    """Busca clientes por nombre y permite elegir uno para ver su detalle."""
    nombre = input("\nIngresa el nombre (o parte del nombre) a buscar: ")
    resultados = buscar_por_nombre(nombre)

    if not resultados:
        print("No encontré coincidencias.")
    elif len(resultados) == 1:
        mostrar_detalle_cliente(resultados[0])
    else:
        table = Table(title="Seleccioná un Cliente")
        table.add_column("ID", style="cyan")
        table.add_column("DNI", style="magenta")
        table.add_column("Nombre", style="green")

        for c in resultados:
            table.add_row(str(c["id"]), str(c["dni"]), c["nombre"])

        console.print(table)

        id_sel = input(
            "\nEscribí el ID para ver el detalle completo (o Enter para salir): "
        )
        if id_sel:
            # Buscamos en los resultados el que coincida con el ID ingresado
            c_sel = next((c for c in resultados if str(c["id"]) == id_sel), None)

            if c_sel:
                mostrar_detalle_cliente(c_sel)
            else:
                print("ID no válido.")
    input("Presiona Enter para continuar...")


def mostrar_detalle_cliente(c):
    """
    Esta función es clave: muestra TODA la info del cliente,
    incluyendo qué autos compró o reservó usando una tabla.
    """
    table = Table(title=f"FICHA DEL CLIENTE - ID: {c['id']}", show_header=False)
    table.add_column("Campo", style="cyan")
    table.add_column("Valor", style="white")

    table.add_row("DNI", str(c["dni"]))
    table.add_row("Nombre", c["nombre"])
    table.add_row("Teléfono", c["telefono"])
    table.add_row("Email", c["email"])
    table.add_row("Localidad", c["localidad"])
    table.add_row("Búsqueda", c["busqueda"])

    console.print(table)


def actualizar_datos_cliente():
    """Permite cambiar el teléfono, email, etc. de un cliente."""
    dni = input("\nIngresa el DNI del cliente a actualizar: ")
    c = buscar_por_dni(dni)

    if not c:
        print("Cliente no encontrado.")
    else:
        print(f"\nModificando datos de: {c['nombre']}")
        print("(Si no querés cambiar un dato, simplemente presiona Enter)")

        nuevo_tel = input(f"Nuevo Teléfono (actual: {c['telefono']}): ")
        nuevo_email = input(f"Nuevo Email (actual: {c['email']}): ")
        nueva_loc = input(f"Nueva Localidad (actual: {c['localidad']}): ")
        nueva_busq = input(f"Nueva Búsqueda (actual: {c['busqueda']}): ")

        # Armamos un diccionario solo con lo que el usuario escribió
        nuevos_datos = {}
        if nuevo_tel:
            nuevos_datos["telefono"] = nuevo_tel
        if nuevo_email:
            nuevos_datos["email"] = nuevo_email
        if nueva_loc:
            nuevos_datos["localidad"] = nueva_loc
        if nueva_busq:
            nuevos_datos["busqueda"] = nueva_busq

        if nuevos_datos:
            actualizar_datos(c["id"], nuevos_datos)
            print("¡Datos actualizados con éxito!")
        else:
            print("No se hicieron cambios.")
    input("Presiona Enter para continuar...")


def dar_de_baja_cliente():
    """Elimina a un cliente si pide no figurar más."""
    dni = input("\nIngresa el DNI del cliente a eliminar: ")
    c = buscar_por_dni(dni)

    if not c:
        print("No encontré a ese cliente.")
    else:
        confirmar = input(f"¿Estás seguro de borrar a {c['nombre']}? (S/N): ")
        if confirmar.lower() == "s":
            eliminar_cliente(c["id"])
            print("Cliente eliminado correctamente.")
        else:
            print("Operación cancelada.")
    input("Presiona Enter para continuar...")

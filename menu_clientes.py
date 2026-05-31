"""
En este archivo manejamos toda la interacción con el usuario 
referida a la gestión de clientes.
"""

import os
from inspect import cleandoc
import cliente
import auto


def limpiar_pantalla():
    """Limpia la terminal para mantener el orden."""
    os.system("cls" if os.name == "nt" else "clear")


def iniciar():
    """Arranca el menú de clientes."""
    while True:
        limpiar_pantalla()
        mensaje = """
        ====================
        GESTIÓN DE CLIENTES
        ====================

        1. Registrar nuevo cliente (Primera consulta)
        2. Listar todos los clientes
        3. Buscar cliente por DNI
        4. Buscar cliente por Nombre
        5. Actualizar datos de contacto
        6. Eliminar cliente de la base
        0. Volver al menú principal

        ¿Qué quieres hacer? """
        
        opcion = input(cleandoc(mensaje))

        match opcion:
            case "1": registrar_nuevo_cliente()
            case "2": mostrar_todos_los_clientes()
            case "3": buscar_cliente_dni()
            case "4": buscar_cliente_nombre()
            case "5": actualizar_datos_cliente()
            case "6": dar_de_baja_cliente()
            case "0": break
            case _:
                print("\nOpción no válida.")
                input("Presiona Enter para continuar...")


def registrar_nuevo_cliente():
    """Pide los datos para dar de alta a un cliente nuevo."""
    print("\n--- REGISTRO DE NUEVO CLIENTE ---")
    dni = input("DNI: ")
    
    # Primero chequeamos que no esté ya registrado
    if cliente.buscar_por_dni(dni):
        print("¡Ojo! Ya tenemos un cliente con ese DNI.")
        input("Presiona Enter para volver...")
        return

    nombre = input("Nombre completo: ")
    telefono = input("Teléfono: ")
    email = input("Email (si no tiene, dejar vacío): ")
    localidad = input("Localidad: ")
    busqueda = input("¿Qué tipo de auto está buscando?: ")

    # Organizamos los datos en un diccionario
    datos = {
        "dni": dni,
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "localidad": localidad,
        "busqueda": busqueda
    }
    
    # Se lo mandamos a la lógica para que lo guarde
    id_cliente = cliente.registrar_cliente(datos)
    print(f"\n¡Listo! Cliente guardado. Su número de cliente es: {id_cliente}")
    input("Presiona Enter para continuar...")


def mostrar_todos_los_clientes():
    """Muestra una lista simple de todos los clientes."""
    lista = cliente.listar_todos()
    if not lista:
        print("\nNo hay clientes cargados todavía.")
    else:
        print("\n--- LISTADO DE CLIENTES ---")
        for c in lista:
            print(f"ID: {c['id']} | DNI: {c['dni']} | Nombre: {c['nombre']}")
    input("\nPresiona Enter para volver...")


def buscar_cliente_dni():
    """Busca y muestra el detalle de un cliente por su DNI."""
    dni = input("\nIngresa el DNI que querés buscar: ")
    c = cliente.buscar_por_dni(dni)
    if c:
        mostrar_detalle_cliente(c)
    else:
        print("No encontré ningún cliente con ese DNI.")
    input("Presiona Enter para continuar...")


def buscar_cliente_nombre():
    """Busca clientes por nombre y permite elegir uno para ver su detalle."""
    nombre = input("\nIngresa el nombre (o parte del nombre) a buscar: ")
    resultados = cliente.buscar_por_nombre(nombre)
    
    if not resultados:
        print("No encontré coincidencias.")
    elif len(resultados) == 1:
        mostrar_detalle_cliente(resultados[0])
    else:
        print("\n--- SELECCIONÁ UN CLIENTE ---")
        for c in resultados:
            print(f"ID: {c['id']} | DNI: {c['dni']} | Nombre: {c['nombre']}")
        
        id_sel = input("\nEscribí el ID para ver el detalle completo (o Enter para salir): ")
        if id_sel:
            # Buscamos en los resultados el que coincida con el ID ingresado
            c_sel = next((c for c in resultados if str(c['id']) == id_sel), None)
            if c_sel:
                mostrar_detalle_cliente(c_sel)
            else:
                print("ID no válido.")
    input("Presiona Enter para continuar...")


def mostrar_detalle_cliente(c):
    """
    Esta función es clave: muestra TODA la info del cliente, 
    incluyendo qué autos compró o reservó.
    """
    print("\n" + "="*40)
    print(f"FICHA DEL CLIENTE - ID: {c['id']}")
    print("="*40)
    print(f"DNI:       {c['dni']}")
    print(f"Nombre:    {c['nombre']}")
    print(f"Teléfono:  {c['telefono']}")
    print(f"Email:     {c['email']}")
    print(f"Localidad: {c['localidad']}")
    print(f"Búsqueda:  {c['busqueda']}")
    
    # Mostramos los autos vinculados (compras)
    print("\n--- AUTOS COMPRADOS ---")
    if not c["compras"]:
        print("No tiene compras registradas.")
    else:
        for auto_id in c["compras"]:
            # Le pedimos al módulo de autos la info de ese ID
            a = auto.seleccionar_auto_por_numero_interno(auto_id)
            if a:
                print(f"-> {a['marca']} {a['modelo']} (Patente: {a['patente']})")

    # Mostramos las reservas
    print("\n--- RESERVAS ACTIVAS ---")
    if not c["reservas"]:
        print("No tiene reservas activas.")
    else:
        for auto_id in c["reservas"]:
            a = auto.seleccionar_auto_por_numero_interno(auto_id)
            if a:
                print(f"-> {a['marca']} {a['modelo']} (Patente: {a['patente']})")
    print("="*40)


def actualizar_datos_cliente():
    """Permite cambiar el teléfono, email, etc. de un cliente."""
    dni = input("\nIngresa el DNI del cliente a actualizar: ")
    c = cliente.buscar_por_dni(dni)
    
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
        if nuevo_tel: nuevos_datos["telefono"] = nuevo_tel
        if nuevo_email: nuevos_datos["email"] = nuevo_email
        if nueva_loc: nuevos_datos["localidad"] = nueva_loc
        if nueva_busq: nuevos_datos["busqueda"] = nueva_busq
        
        if nuevos_datos:
            cliente.actualizar_datos(c["id"], nuevos_datos)
            print("¡Datos actualizados con éxito!")
        else:
            print("No se hicieron cambios.")
    input("Presiona Enter para continuar...")


def dar_de_baja_cliente():
    """Elimina a un cliente si pide no figurar más."""
    dni = input("\nIngresa el DNI del cliente a eliminar: ")
    c = cliente.buscar_por_dni(dni)
    
    if not c:
        print("No encontré a ese cliente.")
    else:
        confirmar = input(f"¿Estás seguro de borrar a {c['nombre']}? (S/N): ")
        if confirmar.lower() == 's':
            cliente.eliminar_cliente(c["id"])
            print("Cliente eliminado correctamente.")
        else:
            print("Operación cancelada.")
    input("Presiona Enter para continuar...")

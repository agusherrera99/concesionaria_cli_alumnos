import os
from inspect import cleandoc
import cliente
import auto


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def iniciar():
    """Menú principal de clientes."""
    while True:
        limpiar_pantalla()
        mensaje = """
        =============
        MENU CLIENTES
        =============

        1. Registrar nuevo cliente
        2. Listar todos los clientes
        3. Buscar cliente por DNI
        4. Buscar cliente por Nombre
        5. Actualizar datos de contacto
        6. Eliminar cliente
        0. Volver al menú principal

        ¿Qué quieres hacer? """
        
        opcion = input(cleandoc(mensaje))

        match opcion:
            case "1":
                registrar_nuevo_cliente()
            case "2":
                mostrar_todos_los_clientes()
            case "3":
                buscar_cliente_dni()
            case "4":
                buscar_cliente_nombre()
            case "5":
                actualizar_datos_cliente()
            case "6":
                dar_de_baja_cliente()
            case "0":
                break
            case _:
                print("\nOpción no válida.")
                input("Presiona Enter para continuar...")


def registrar_nuevo_cliente():
    print("\n--- REGISTRO DE NUEVO CLIENTE ---")
    dni = input("DNI: ")
    if cliente.buscar_por_dni(dni):
        print("Error: Ya existe un cliente con ese DNI.")
        input("Presiona Enter para volver...")
        return

    nombre = input("Nombre completo: ")
    telefono = input("Teléfono: ")
    email = input("Email (opcional): ")
    localidad = input("Localidad: ")
    busqueda = input("¿Qué está buscando?: ")

    datos = {
        "dni": dni,
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "localidad": localidad,
        "busqueda": busqueda
    }
    
    id_cliente = cliente.registrar_cliente(datos)
    print(f"\nCliente registrado con éxito. ID Interno: {id_cliente}")
    input("Presiona Enter para continuar...")


def mostrar_todos_los_clientes():
    lista = cliente.listar_todos()
    if not lista:
        print("\nNo hay clientes registrados.")
    else:
        print("\n--- LISTADO DE CLIENTES ---")
        for c in lista:
            print(f"ID: {c['id']} | DNI: {c['dni']} | Nombre: {c['nombre']} | Localidad: {c['localidad']}")
    input("\nPresiona Enter para continuar...")


def buscar_cliente_dni():
    dni = input("\nIngrese DNI a buscar: ")
    c = cliente.buscar_por_dni(dni)
    if c:
        mostrar_detalle_cliente(c)
    else:
        print("Cliente no encontrado.")
    input("Presiona Enter para continuar...")


def buscar_cliente_nombre():
    nombre = input("\nIngrese nombre a buscar: ")
    resultados = cliente.buscar_por_nombre(nombre)
    if not resultados:
        print("No se encontraron coincidencias.")
    elif len(resultados) == 1:
        mostrar_detalle_cliente(resultados[0])
    else:
        print("\n--- RESULTADOS ---")
        for c in resultados:
            print(f"ID: {c['id']} | DNI: {c['dni']} | Nombre: {c['nombre']}")
        
        id_sel = input("\nIngrese el ID para ver detalle (o Enter para salir): ")
        if id_sel:
            c_sel = next((c for c in resultados if str(c['id']) == id_sel), None)
            if c_sel:
                mostrar_detalle_cliente(c_sel)
            else:
                print("ID no válido.")
    input("Presiona Enter para continuar...")


def mostrar_detalle_cliente(c):
    print("\n" + "="*30)
    print(f"DETALLE DEL CLIENTE (ID: {c['id']})")
    print("="*30)
    print(f"DNI:       {c['dni']}")
    print(f"Nombre:    {c['nombre']}")
    print(f"Teléfono:  {c['telefono']}")
    print(f"Email:     {c['email']}")
    print(f"Localidad: {c['localidad']}")
    print(f"Búsqueda:  {c['busqueda']}")
    
    print("\n--- COMPRAS REALIZADAS ---")
    if not c["compras"]:
        print("Sin compras registradas.")
    else:
        for auto_id in c["compras"]:
            a = auto.seleccionar_auto_por_numero_interno(auto_id)
            if a:
                print(f"- {a['marca']} {a['modelo']} ({a['patente']})")

    print("\n--- RESERVAS ACTIVAS ---")
    if not c["reservas"]:
        print("Sin reservas activas.")
    else:
        for auto_id in c["reservas"]:
            a = auto.seleccionar_auto_por_numero_interno(auto_id)
            if a:
                print(f"- {a['marca']} {a['modelo']} ({a['patente']})")
    print("="*30)


def actualizar_datos_cliente():
    dni = input("\nIngrese DNI del cliente a actualizar: ")
    c = cliente.buscar_por_dni(dni)
    if not c:
        print("Cliente no encontrado.")
    else:
        print(f"\nActualizando datos de {c['nombre']}")
        nuevo_tel = input(f"Nuevo Teléfono (actual: {c['telefono']}): ")
        nuevo_email = input(f"Nuevo Email (actual: {c['email']}): ")
        nueva_loc = input(f"Nueva Localidad (actual: {c['localidad']}): ")
        nueva_busq = input(f"Nueva Búsqueda (actual: {c['busqueda']}): ")
        
        nuevos_datos = {}
        if nuevo_tel: nuevos_datos["telefono"] = nuevo_tel
        if nuevo_email: nuevos_datos["email"] = nuevo_email
        if nueva_loc: nuevos_datos["localidad"] = nueva_loc
        if nueva_busq: nuevos_datos["busqueda"] = nueva_busq
        
        if nuevos_datos:
            cliente.actualizar_datos(c["id"], nuevos_datos)
            print("Datos actualizados correctamente.")
        else:
            print("No se realizaron cambios.")
    input("Presiona Enter para continuar...")


def dar_de_baja_cliente():
    dni = input("\nIngrese DNI del cliente a eliminar: ")
    c = cliente.buscar_por_dni(dni)
    if not c:
        print("Cliente no encontrado.")
    else:
        confirmar = input(f"¿Está seguro que desea eliminar a {c['nombre']}? (s/n): ")
        if confirmar.lower() == 's':
            cliente.eliminar_cliente(c["id"])
            print("Cliente eliminado de la base de datos.")
        else:
            print("Operación cancelada.")
    input("Presiona Enter para continuar...")

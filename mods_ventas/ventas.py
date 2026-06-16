
from ventas_registros import f_cargar_ventas, f_guardar_ventas
from ventas_utilidades import f_pedir_entero, f_pedir_confirmacion, f_forma_pago, f_estado_pago, f_imprimir_detalle, f_imprimir_resumen_venta
from datetime import date

def f_menu_ventas():
    while True:
        print("\n-----")
        print("Ventas")
        print("-----")
        print("1. Registrar una venta")
        print("2. Ver todas las ventas")
        print("3. Buscar ventas por patente, DNI o vendedor")
        print("4. Buscar una venta / cambiar estado")
        print("5. Eliminar una venta")
        print("6. Volver al menu principal")
        
        opcion = input("Seleccione una opcion: ")

        match opcion:
            case "1":
                f_registrar_venta()
            case "2":
                f_ver_ventas()
            case "3":
                f_buscar_ventas_por_criterio()
            case "4":
                f_buscar_venta()
            case "5":
                f_eliminar_venta()
            case "6":
                break
            case _:
                print("Opcion invalida, intente de nuevo")

def f_crear_venta(id_auto, id_cliente, id_vendedor, precio_final, forma_pago):
    ventas = f_cargar_ventas()

    # Verificar que el auto no haya sido vendido
    for v in ventas:
        if v["id_auto"] == id_auto:
            print(f"\n¡Error! El auto con ID {id_auto} ya fue vendido.")
            return None

    estado_pago = f_estado_pago(forma_pago)
    fecha_venta = date.today().isoformat()

    # Generar ID autoincremental
    if ventas:
        id_venta = max(v["id_venta"] for v in ventas) + 1
    else:
        id_venta = 1

    venta = {
        "id_venta": id_venta,
        "id_auto": id_auto,
        "id_cliente": id_cliente,
        "id_vendedor": id_vendedor,
        "fecha_venta": fecha_venta,
        "precio_final": precio_final,
        "forma_pago": forma_pago,
        "estado_pago": estado_pago
    }

    ventas.append(venta)
    f_guardar_ventas(ventas)

    return venta



def f_registrar_venta():
    print("\nComplete los siguientes datos")

    id_auto = f_pedir_entero("Ingrese el ID del auto: ")
    id_cliente = f_pedir_entero("Ingrese el ID del cliente: ")
    id_vendedor = f_pedir_entero("Ingrese el ID del vendedor: ")
    precio_final = f_pedir_entero("Ingrese el precio final: ")
    forma_pago = f_forma_pago()

    if not f_pedir_confirmacion("\n¿Desea registrar esta venta? (s/n): "):
        print("\nOperación cancelada.")
        return

    venta = f_crear_venta(
        id_auto,
        id_cliente,
        id_vendedor,
        precio_final,
        forma_pago
    )

    if venta:
        print(
            f"\n¡Venta registrada con éxito! "
            f"ID asignado: {venta['id_venta']}"
        )


def f_ver_ventas():
    ventas = f_cargar_ventas()
    if not ventas:
        print("\nNo hay ventas registradas.")
        return
        
    print("\n--- LISTADO DE VENTAS ---")
    for v in ventas:
        f_imprimir_resumen_venta(v)
        


def f_buscar_ventas_por_criterio():
    """Interface to search sales by auto ID, client DNI, or vendor ID."""
    print("\n--- BUSCAR VENTAS POR CRITERIO ---")
    print("Seleccione el criterio de búsqueda:")
    print("1. Patente (ID del auto)")
    print("2. DNI (ID del cliente)")
    print("3. Vendedor (ID del vendedor)")
    opcion = input("Ingrese una opción: ").strip()
    if opcion == "1":
        id_auto = f_pedir_entero("Ingrese el ID de la patente del auto: ")
        resultados = buscar_ventas_por_auto(id_auto)
    elif opcion == "2":
        id_cliente = f_pedir_entero("Ingrese el DNI del cliente: ")
        resultados = buscar_ventas_por_cliente(id_cliente)
    elif opcion == "3":
        id_vendedor = f_pedir_entero("Ingrese el ID del vendedor: ")
        resultados = buscar_ventas_por_vendedor(id_vendedor)
    else:
        print("Opción inválida.")
        return
    if resultados:
        print(f"\nSe encontraron {len(resultados)} venta(s):")
        for v in resultados:
            f_imprimir_resumen_venta(v)
            
    else:
        print("No se encontraron ventas con el criterio especificado.")

def f_buscar_venta():
    ventas = f_cargar_ventas()
    if not ventas:
        print("\nNo hay ventas registradas.")
        return
        
    id_buscar = f_pedir_entero("\nIngrese el ID de la venta a buscar: ")
    
    # Buscar en la lista de diccionarios
    encontrada = None
    for v in ventas:
        if v["id_venta"] == id_buscar:
            encontrada = v
            break
            
    if encontrada:
        print("\n--- DETALLE DE LA VENTA ---")
        f_imprimir_resumen_venta(encontrada)
        
        # Si el estado de pago es "En cuotas" o "Pendiente", permitir modificar el estado
        if encontrada['estado_pago'] in ["En cuotas", "Pendiente"]:
            print(f"\nEl estado de pago actual es '{encontrada['estado_pago']}'.")
            print("Seleccione el nuevo estado de pago:")
            print("1. Cobrado")
            print("2. Pendiente")
            print("3. En cuotas")
            opcion_estado = input("Seleccione una opción: ").strip()
            
            nuevo_estado = None
            
    # Tupla de tuplas que mapea la opción ingresada con el nuevo estado de pago
    opciones_estado = (
        ("1", "Cobrado"),
        ("2", "Pendiente"),
        ("3", "En cuotas")
    )
    nuevo_estado = None
    for opt, est in opciones_estado:
        if opt == opcion_estado:
            nuevo_estado = est
            break
    if nuevo_estado is None:
        print("Opción inválida. No se realizaron cambios.")

            
    if nuevo_estado:
        if f_pedir_confirmacion(f"\n¿Desea cambiar el estado de pago a '{nuevo_estado}'? (s/n): "):
            encontrada['estado_pago'] = nuevo_estado
            f_guardar_ventas(ventas)
            print(f"¡Estado de pago actualizado con éxito a '{nuevo_estado}'!")
        else:
            print("Operación cancelada. No se realizaron cambios.")
    else:
        print(f"\nNo se encontró ninguna venta con el ID {id_buscar}.")


def f_eliminar_venta():
    ventas = f_cargar_ventas()
    if not ventas:
        print("\nNo hay ventas registradas.")
        return
        
    id_eliminar = f_pedir_entero("\nIngrese el ID de la venta a eliminar: ")
    
    # Buscar en la lista de diccionarios
    encontrada = None
    for v in ventas:
        if v["id_venta"] == id_eliminar:
            encontrada = v
            break
            
    if encontrada:
        f_imprimir_detalle(encontrada, titulo="DETALLE DE LA VENTA A ELIMINAR")
        
        confirmar = input("\n¿Está seguro de que desea eliminar esta venta? (s/n): ").strip().lower()
        if confirmar == "s":
            ventas.remove(encontrada)
            f_guardar_ventas(ventas)
            print("¡Venta eliminada con éxito!")
        else:
            print("Operación cancelada. No se eliminó la venta.")
    else:
        print(f"\nNo se encontró ninguna venta con el ID {id_eliminar}.")

#Si se ejecuta este archivo directamente
def buscar_ventas_por_auto(id_auto):
    """Return a list of sales matching the given auto ID."""
    ventas = f_cargar_ventas()
    return [v for v in ventas if v.get("id_auto") == id_auto]


def buscar_ventas_por_cliente(id_cliente):
    """Return a list of sales matching the given client ID (DNI)."""
    ventas = f_cargar_ventas()
    return [v for v in ventas if v.get("id_cliente") == id_cliente]


def buscar_ventas_por_vendedor(id_vendedor):
    """Return a list of sales matching the given vendor ID."""
    ventas = f_cargar_ventas()
    return [v for v in ventas if v.get("id_vendedor") == id_vendedor]

if __name__ == "__main__":
    f_menu_ventas()




# def f_registrar_venta():
#     # Cargar las ventas existentes (lista de diccionarios) al inicio para validar
#     ventas = f_cargar_ventas()

#     print("\nComplete los siguientes datos")
#     id_auto = f_pedir_entero("Ingrese el ID del auto: ")

#     # Controlar que no se vendan autos ya vendidos
#     for v in ventas:
#         if v["id_auto"] == id_auto:
#             print(f"\n¡Error! El auto con ID {id_auto} ya ha sido vendido y no se puede registrar otra venta.")
#             return

#     id_cliente = f_pedir_entero("Ingrese el ID del cliente: ")
#     id_vendedor = f_pedir_entero("Ingrese el ID del vendedor: ")
#     fecha_venta = date.today().isoformat()
#     precio_final = f_pedir_entero("Ingrese el precio final: ")
#     forma_pago = f_forma_pago()
#     estado_pago = f_estado_pago(forma_pago)
    
#     # Calcular el siguiente ID de venta (autoincremental)
#     if ventas:
#         id_venta = max(v["id_venta"] for v in ventas) + 1
#     else:
#         id_venta = 1
        
#     # Crear una tupla para empaquetar los datos de la venta (uso didáctico de tuplas)
#     venta_tupla = (id_venta, id_auto, id_cliente, id_vendedor, fecha_venta, precio_final, forma_pago, estado_pago)
    
#     # Convertir la tupla a un diccionario para poder guardarlo en JSON
#     venta_dict = {
#         "id_venta": venta_tupla[0],
#         "id_auto": venta_tupla[1],
#         "id_cliente": venta_tupla[2],
#         "id_vendedor": venta_tupla[3],
#         "fecha_venta": venta_tupla[4],
#         "precio_final": venta_tupla[5],
#         "forma_pago": venta_tupla[6],
#         "estado_pago": venta_tupla[7]
#     }
    
#     # Confirmar la venta antes de registrarla
#     if f_pedir_confirmacion("\n¿Desea registrar esta venta? (s/n): "):
#         # Agregar a la lista
#         ventas.append(venta_dict)
#         # Guardar en el archivo JSON
#         f_guardar_ventas(ventas)
#         print(f"\n¡Venta registrada con éxito! ID de venta asignado: {id_venta}")
#     else:
#         print("\nOperación cancelada. No se registró la venta.")


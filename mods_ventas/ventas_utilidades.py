def f_pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un número entero.")

def f_pedir_confirmacion(mensaje):
    """Pide al usuario confirmación s/n y retorna True si es sí o False si es no."""
    while True:
        confirmar = input(mensaje).strip().lower()
        if confirmar in ["s", "si", "sí"]:
            return True
        if confirmar in ["n", "no"]:
            return False
        print("Opción inválida. Ingrese 's' para Sí o 'n' para No.")

def f_forma_pago():
    # Tupla con opciones de pago inmutables
    opciones = ("Contado", "Financiado", "Parte de pago con otro auto")
    
    print("Seleccione una forma de pago")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")
        
    opcion_usuario = input("Seleccione una opcion: ")
    try:
        indice = int(opcion_usuario) - 1
        if 0 <= indice < len(opciones):
            return opciones[indice]
    except ValueError:
        pass

    print("Opcion invalida, intente de nuevo")
    return f_forma_pago()

def f_estado_pago(forma_pago):
    # Tupla de tuplas que mapea forma_pago con su respectivo estado de pago
    relacion_pago_estado = (
        ("Contado", "Cobrado"),
        ("Financiado", "En cuotas"),
        ("Parte de pago con otro auto", "Pendiente")
    )

    for fp, ep in relacion_pago_estado:
        if fp == forma_pago:
            return ep

    return "Opcion invalida"


def f_imprimir_detalle(venta, titulo="DETALLE DE LA VENTA"):
    """Imprime los campos de un diccionario de venta de forma formateada.

    Args:
        venta (dict): Diccionario que contiene los datos de la venta.
        titulo (str, optional): Título que se muestra antes del detalle. Por defecto "DETALLE DE LA VENTA".
    """
    print(f"\n--- {titulo} ---")
    print(f"ID Venta:      {venta['id_venta']}")
    print(f"ID Auto:       {venta['id_auto']}")
    print(f"ID Cliente:    {venta['id_cliente']}")
    print(f"ID Vendedor:   {venta['id_vendedor']}")
    print(f"Fecha:         {venta['fecha_venta']}")
    print(f"Precio Final:  ${venta['precio_final']}")
    print(f"Forma de Pago: {venta['forma_pago']}")
    print(f"Estado de Pago:{venta['estado_pago']}")

def f_imprimir_resumen_venta(venta):
    """Imprime una venta en una sola línea horizontal resumida."""
    print(f"ID Venta: {venta['id_venta']} | Auto ID: {venta['id_auto']} | Cliente ID: {venta['id_cliente']} | Vendedor ID: {venta['id_vendedor']} | Fecha: {venta['fecha_venta']} | Precio: ${venta['precio_final']} | Pago: {venta['forma_pago']} | Estado: {venta['estado_pago']}")
    print("-" * 40)

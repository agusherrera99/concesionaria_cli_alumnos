"""
Este es el punto de inicio de nuestro programa.
Desde acá el usuario puede elegir si quiere ir a la sección de Autos 
o a la sección de Clientes.
"""

import os
from inspect import cleandoc
import menu_autos
import menu_clientes


def iniciar():
    """Esta es la función que arranca todo el sistema."""
    mostrar_menu_principal()


def limpiar_menu():
    """Función para limpiar la pantalla y que el menú se vea prolijo."""
    # 'cls' es para Windows, 'clear' es para Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_menu_principal():
    """Dibuja el menú principal en la pantalla."""
    
    # Usamos cleandoc para que el texto multilínea no tenga espacios raros al principio
    mensaje = """
    =========================
    SISTEMA DE CONCESIONARIA
    =========================

    1. Gestión de Autos (Stock)
    2. Gestión de Clientes
    0. Salir del sistema

    ¿Qué quieres hacer hoy? """

    # El ciclo 'while True' hace que el menú se repita hasta que el usuario elija salir
    while True:
        limpiar_menu()
        opcion_seleccionada = input(cleandoc(mensaje))

        # El 'match' es como un 'if' pero más ordenado para elegir opciones
        match opcion_seleccionada:
            case "1":
                limpiar_menu()
                menu_autos.iniciar() # Nos vamos al menú de autos
            case "2":
                limpiar_menu()
                menu_clientes.iniciar() # Nos vamos al menú de clientes
            case "0":
                print("\n¡Gracias por usar el sistema! Hasta pronto.")
                break # Sale del ciclo y termina el programa
            case _:
                print("\nEsa opción no es válida. ¡Intentá de nuevo!")
                input("Presiona Enter para continuar...")

import os
from inspect import cleandoc
import menu_autos
import menu_clientes


def iniciar():
    """Punto de entrada para el programa."""
    mostrar_menu_principal()

def limpiar_menu():
    """Limpia la terminal."""
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu_principal():
    """Muestra el menú de nivel superior de la aplicación."""
    mensaje = """
    =============
    CONCESIONARIA
    =============

    1. Autos en stock
    2. Gestión de Clientes
    0. Salir

    ¿Qué quieres hacer? """

    while True:
        limpiar_menu()
        opcion_seleccionada = input(cleandoc(mensaje))

        match opcion_seleccionada:
            case "1":
                limpiar_menu()
                menu_autos.iniciar()
            case "2":
                limpiar_menu()
                menu_clientes.iniciar()
            case "0":
                print("\n¡Gracias por usar el sistema! Hasta pronto.")
                break
            case _:
                print("\nOpción no válida.")
                input("Presiona Enter para volver a intentarlo...")

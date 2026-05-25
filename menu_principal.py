import os

from inspect import cleandoc

from menu_autos import MenuAutos


class MenuPrincipal:
    def __init__(self):
        pass

    def iniciar(self):
        self.principal()

    def limpiar_menu(self):
        os.system("cls" if os.name == "nt" else "clear")

    def principal(self):
        mensaje = """
        =============
        CONCESIONARIA
        =============

        1. Autos en stock
        0. Salir

        ¿Qué quieres hacer? """

        while True:
            self.limpiar_menu()
            opcion_seleccionada = input(cleandoc(mensaje))

            match opcion_seleccionada:
                case "1":
                    self.limpiar_menu()
                    MenuAutos().iniciar()
                case "0":
                    break
                case _:
                    print("Opción no valida.")
                    input(cleandoc("Presiona Enter para volver a intentarlo..."))

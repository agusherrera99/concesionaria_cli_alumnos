import os

from inspect import cleandoc

from auto import Auto


class MenuAutos:
    def __init__(self):
        self.auto = Auto()

    def iniciar(self):
        self.principal()

    def limpiar_menu(self):
        os.system("cls" if os.name == "nt" else "clear")

    def ver_listado(self):
        self.limpiar_menu()
        listado = self.auto.seleccionar_todos()
        print(listado)

        mensaje = """
        0. Volver
        
        ¿Qué quieres hacer? """

        while True:
            opcion_seleccionada = input(cleandoc(mensaje))
            match opcion_seleccionada:
                case "0":
                    break
                case _:
                    print("Opción no válida.")
                    input(cleandoc("Presiona Enter para volver a intentarlo..."))


    def cargar_auto_nuevo(self):
        print("\nCompleta los siguientes campos")

        try:
            patente = input(cleandoc("Patente: "))
            marca = input(cleandoc("Marca: "))
            modelo = input(cleandoc("Modelo: "))
            anio = int(input(cleandoc("Año: ")))
            kilometros = int(input(cleandoc("Kilometros: ")))
            precio = int(input(cleandoc("Precio: ")))
            estado = input(cleandoc("Estado: "))
            fecha_ingreso = input(cleandoc("Fecha de Ingreso: "))

            mensaje = """

            1. Confirmar
            0. Cancelar

            ¿Qué quieres hacer? """

            while True:
                opcion_seleccionada = input(cleandoc(mensaje))
                match opcion_seleccionada:
                    case "1":
                        datos = (
                            patente,
                            marca,
                            modelo,
                            anio,
                            kilometros,
                            precio,
                            estado,
                            fecha_ingreso,
                        )
                        self.auto.guardar_auto(datos)
                        break
                    case "0":
                        break
                    case _:
                        print("Opción no válida.")
                        input(cleandoc("Presiona Enter para volver a intentarlo..."))

        except Exception as error:
            print(error)

    def principal(self):
        mensaje = """
        ==============
        AUTOS EN STOCK
        ==============

        1. Cargar un auto nuevo
        2. Ver listado de autos
        0. Volver

        ¿Qué quieres hacer? """

        while True:
            self.limpiar_menu()
            opcion_seleccionada = input(cleandoc(mensaje))

            match opcion_seleccionada:
                case "1":
                    self.cargar_auto_nuevo()
                    break
                case "2":
                    self.ver_listado()
                    break
                case "0":
                    break
                case _:
                    print("Opción no válida.")
                    input(cleandoc("Presiona Enter para volver a intentarlo..."))

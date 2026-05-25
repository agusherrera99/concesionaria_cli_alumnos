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

    def cargar_auto_nuevo(self):
        print("Completa los siguientes campos")

        try:
            patente = input("Patente: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            anio = int(input("Año: "))
            kilometros = int(input("Kilometros: "))
            precio = int(input("Precio: "))
            estado = input("Estado: ")
            fecha_ingreso = input("Fecha de Ingreso: ")

            mensaje = """
            1. Confirmar
            0. Cancelar

            ¿Qué quieres hacer? """

            while True:
                opcion_seleccionada = input(mensaje)
                match opcion_seleccionada:
                    case "1":
                        datos = {
                            "patente": patente,
                            "marca": marca,
                            "modelo": modelo,
                            "año": anio,
                            "kilometros": kilometros,
                            "precio": precio,
                            "estado": estado,
                            "fecha_ingreso": fecha_ingreso,
                        }
                        self.auto.nuevo(datos)
                    case "0":
                        break
                    case _:
                        print("Opción no válida.")
                        input("Presiona Enter para volver a intentarlo...")

        except Exception as error:
            print(error)

    def principal(self):
        mensaje = """
        ==============
        AUTOS EN STOCK
        ==============

        1. Cargar un auto nuevo
        0. Volver

        ¿Qué quieres hacer? """

        while True:
            self.limpiar_menu()
            opcion_seleccionada = input(mensaje)

            match opcion_seleccionada:
                case "1":
                    self.cargar_auto_nuevo()
                case "0":
                    break
                case _:
                    print("Opción no válida.")
                    input("Presiona Enter para volver a intentarlo...")

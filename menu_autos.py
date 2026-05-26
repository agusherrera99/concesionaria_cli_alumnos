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

    def seleccionar_estado(self):
        mensaje = """
        1. Disponible
        2. Reservado
        3. Vendido
        4. En taller

        Seleccionar un estado: """

        while True:
            opcion_seleccionada = input(cleandoc(mensaje))
            match opcion_seleccionada:
                case "1":
                    return "disponible"
                case "2":
                    return "reservado"
                case "3":
                    return "vendido"
                case "4":
                    return "en taller"
                case _:
                    print("Opción no válida")
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
            estado = self.seleccionar_estado()
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

    def filtrar_listado(self):
        mensaje = """
        ===============
        FILTRAR LISTADO
        ===============

        1. Por marca
        2. Por rango de precio
        3. Por estado
        0. Volver

        ¿Qué quieres hacer? """

        while True:
            self.limpiar_menu()
            opcion_seleccionada = input(cleandoc(mensaje))
            match opcion_seleccionada:
                case "1":
                    marca = input(cleandoc("Ingresa la marca: "))
                    listado = self.auto.seleccionar_por("marca", marca)
                    if listado:
                        for auto in listado:
                            print(auto)
                        input(cleandoc("Presiona Enter para volver"))
                case "2":
                    minimo = input(cleandoc("Ingresa el mínimo del rango: "))
                    maximo = input(cleandoc("Ingresa el máximo del rango: "))
                    listado = self.auto.seleccionar_por_rango(minimo, maximo)
                    if listado:
                        for auto in listado:
                            print(auto)
                        input("Presionar Enter para volver")
                case "3":
                    estado = self.seleccionar_estado()
                    listado = self.auto.seleccionar_por("estado", estado)
                    if listado:
                        for auto in listado:
                            print(auto)
                        input(cleandoc("Presiona Enter para volver"))
                case "0":
                    break
                case _:
                    print("Opción no válida")
                    input(cleandoc("Presiona Enter para volver a intentarlo..."))

    def ver_listado(self):
        mensaje = """
        ================
        LISTADO DE AUTOS
        ================

        1. Ver listado completo
        2. Filtrar listado
        0. Volver

        ¿Qué quieres hacer? """

        while True:
            self.limpiar_menu()
            opcion_seleccionada = input(cleandoc(mensaje))
            match opcion_seleccionada:
                case "1":
                    self.limpiar_menu()
                    listado_completo = self.auto.seleccionar_todos()
                    for auto in listado_completo:
                        print(auto)
                    input(cleandoc("Presiona Enter para volver"))
                case "2":
                    self.filtrar_listado()
                case "0":
                    break
                case _:
                    print("Opción no válida.")
                    input(cleandoc("Presiona Enter para volver a intentarlo..."))

    def buscar_auto_por(self, tipo):
        try:
            if tipo == "patente":
                patente = input(cleandoc("Ingrese la patente: "))
                auto = self.auto.seleccionar_auto_por_patente(patente)
            else:
                numero_interno = int(input(cleandoc("Ingrese el número interno: ")))
                auto = self.auto.seleccionar_auto_por_numero_interno(numero_interno)

            self.limpiar_menu()

            if auto:
                print(cleandoc(f"""
                AUTO ENCONTRADO

                {auto}
                """))
            else:
                print("No se pudo encontrar un auto")
                return None
            return auto
        except Exception as error:
            print(error)

    def buscar_auto(self, con_pausa=True):
        mensaje = """
        =============
        BUSCAR AUTO
        =============

        1. Por patente
        2. Por número interno
        0. Volver

        ¿Qué quieres hacer? """

        while True:
            self.limpiar_menu()
            opcion_seleccionada = input(cleandoc(mensaje))
            match opcion_seleccionada:
                case "1":
                    auto = self.buscar_auto_por("patente")
                    if con_pausa:
                        input("Presionar Enter para volver")
                    return auto
                case "2":
                    auto = self.buscar_auto_por("numero_interno")
                    if con_pausa:
                        input("Presionar Enter para volver")
                    return auto
                case "0":
                    break
                case _:
                    print("Opción no válida.")
                    input(cleandoc("Presiona Enter para volver a intentarlo..."))

    def cambiar_estado(self):
        mensaje = """
        =========================
        CAMBIAR ESTADO DE UN AUTO
        =========================

        1. Seleccionar auto
        0. Volver

        ¿Qué quieres hacer? """

        while True:
            self.limpiar_menu()
            opcion_seleccionada = input(cleandoc(mensaje))
            match opcion_seleccionada:
                case "1":
                    auto = self.buscar_auto(con_pausa=False)
                    if auto:
                        numero_interno = auto[0]
                        estado = self.seleccionar_estado()
                        self.auto.cambiar_estado(numero_interno, estado)
                    input("Presionar Enter para volver")
                case "0":
                    break
                case _:
                    print("Opción no válida.")
                    input(cleandoc("Presiona Enter para volver a intentarlo..."))

    def pedir_confirmacion(self):
        mensaje = """
        ************
        CONFIRMACION
        ************

        1. Confirmar
        0. Cancelar

        ¿Qué quiere hacer? """

        while True:
            self.limpiar_menu()
            opcion_seleccionada = input(cleandoc(mensaje))
            match opcion_seleccionada:
                case "1":
                    return True
                case "0":
                    return False
                case _:
                    print("Opción no válida")
                    input(cleandoc("Presiona Enter para volver a intentarlo..."))

    def dar_de_baja_un_auto(self):
        mensaje = """
        ===================
        DAR DE BAJA UN AUTO
        ===================

        1. Seleccionar auto
        0. Volver

        ¿Qué quieres hacer? """

        while True:
            self.limpiar_menu()
            opcion_seleccionada = input(cleandoc(mensaje))
            match opcion_seleccionada:
                case "1":
                    auto = self.buscar_auto(con_pausa=False)
                    if auto:
                        numero_interno = auto[0]
                        confirmacion = self.pedir_confirmacion()

                        if confirmacion:
                            self.auto.dar_de_baja(numero_interno)

                    input("Presionar Enter para volver")
                    self.limpiar_menu()
                case "0":
                    break
                case _:
                    print("Opción no válida")
                    input(cleandoc("Presiona Enter para volver a intentarlo..."))

    def principal(self):
        mensaje = """
        ==============
        AUTOS EN STOCK
        ==============

        1. Cargar un auto nuevo
        2. Ver listado de autos
        3. Buscar un auto
        4. Cambiar estado de un auto
        5. Dar de baja un auto
        0. Volver a la pantalla principal

        ¿Qué quieres hacer? """

        while True:
            self.limpiar_menu()
            opcion_seleccionada = input(cleandoc(mensaje))
            match opcion_seleccionada:
                case "1":
                    self.cargar_auto_nuevo()
                case "2":
                    self.ver_listado()
                case "3":
                    self.buscar_auto()
                case "4":
                    self.cambiar_estado()
                case "5":
                    self.dar_de_baja_un_auto()
                case "0":
                    break
                case _:
                    print("Opción no válida.")
                    input(cleandoc("Presiona Enter para volver a intentarlo..."))

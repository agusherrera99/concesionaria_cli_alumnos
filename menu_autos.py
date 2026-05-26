import os
from inspect import cleandoc
from auto import Auto

# La clase MenuAutos se encarga de toda la interacción con el usuario (Command Line Interface o CLI).
# Se divide en funciones claras para entender la responsabilidad de cada parte.
class MenuAutos:
    def __init__(self):
        # Instanciamos la clase Auto para manejar la lógica de datos.
        # Esto separa la "Vista" (menús) del "Modelo" (datos).
        self.auto = Auto()

    def iniciar(self):
        """Punto de entrada para este menú."""
        self.principal()

    # --- Métodos de Ayuda (Helper Methods) ---
    # Estos métodos facilitan tareas repetitivas como limpiar pantalla o validar números.
    def limpiar_menu(self):
        """Limpia la terminal dependiendo del sistema operativo (Windows o Linux/Mac)."""
        os.system("cls" if os.name == "nt" else "clear")

    def leer_entero(self, mensaje):
        """
        Pide un dato y verifica que sea un número entero.
        Si el usuario ingresa letras, informa con 'buena onda' y vuelve a preguntar.
        Esto cumple con el requisito de validación de números.
        """
        while True:
            valor = input(cleandoc(mensaje))
            if valor.isdigit():
                return int(valor)
            print("\nEso no parece un número. Por favor, intenta de nuevo con números solamente.")
    # -----------------------------------------

    def seleccionar_estado(self):
        """Sub-menú para elegir un estado válido de la lista predefinida."""
        mensaje = """
        1. Disponible
        2. Reservado
        3. Vendido
        4. En taller

        Seleccionar un estado: """

        while True:
            # No limpiamos pantalla aquí para no perder el contexto de lo que estábamos haciendo arriba
            opcion_seleccionada = input(cleandoc(mensaje))
            match opcion_seleccionada:
                case "1": return "disponible"
                case "2": return "reservado"
                case "3": return "vendido"
                case "4": return "en taller"
                case _:
                    print("\nEsa opción no es válida. ¡Probá con una del 1 al 4!")
                    input("Presioná Enter para intentar de nuevo...")

    # --- Operaciones Principales (CRUD) ---
    def cargar_auto_nuevo(self):
        """CARGAR (Alta): Pide los datos y los guarda en la base de datos."""
        print("\n--- COMPLETAR DATOS DEL NUEVO AUTO ---")

        try:
            patente = input("Patente: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")

            # Usamos leer_entero para asegurar que no se rompa el programa
            # al validar que el dado ingresado sea un entero
            anio = self.leer_entero("Año: ")
            kilometros = self.leer_entero("Kilometros: ")
            precio = self.leer_entero("Precio: ")

            estado = self.seleccionar_estado()
            fecha_ingreso = input("Fecha de Ingreso (DD/MM/AAAA): ")

            print("\n¿Confirmas la carga de este auto?")
            if self.pedir_confirmacion():
                datos = (patente, marca, modelo, anio, kilometros, precio, estado, fecha_ingreso)
                self.auto.guardar_auto(datos)
                print("\n¡Excelente! El auto se guardó correctamente.")
            else:
                print("\nCarga cancelada. Volviendo al menú...")

            input("\nPresioná Enter para continuar...")
        except Exception as error:
            print(f"\nOcurrió un error inesperado: {error}")
            input("Presioná Enter para volver...")

    def filtrar_listado(self):
        """CONSULTAR (Filtros): Permite buscar grupos de autos por criterios."""
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
                    marca = input("\nIngresa la marca a buscar: ")
                    listado = self.auto.seleccionar_por("marca", marca)
                    self._mostrar_resultados(listado, f"marca '{marca}'")
                case "2":
                    minimo = self.leer_entero("\nPrecio mínimo: ")
                    maximo = self.leer_entero("Precio máximo: ")
                    listado = self.auto.seleccionar_por_rango(minimo, maximo)
                    self._mostrar_resultados(listado, f"rango ${minimo} - ${maximo}")
                case "3":
                    estado = self.seleccionar_estado()
                    listado = self.auto.seleccionar_por("estado", estado)
                    self._mostrar_resultados(listado, f"estado '{estado}'")
                case "0":
                    break
                case _:
                    print("\n¡Oops! Esa opción no existe. Probá con una del menú. 😊")
                    input("Presiona Enter para volver a intentarlo...")

    def _mostrar_resultados(self, listado, criterio):
        """Función interna para mostrar los resultados de una búsqueda de forma prolija."""
        if listado:
            print(f"\nResultados encontrados para {criterio}:")
            for auto in listado:
                print(auto)
        else:
            print(f"\nNo encontré resultados para {criterio}.")
        input("\nPresiona Enter para volver")

    def ver_listado(self):
        """LISTAR: Muestra todos los autos o deriva al menú de filtros."""
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
                    listado = self.auto.seleccionar_todos()
                    if listado:
                        print("\n--- Listado Completo de Autos ---")
                        for auto in listado: print(auto)
                    else:
                        print("\nTodavía no hay autos cargados.")
                    input("\nPresiona Enter para volver")
                case "2":
                    self.filtrar_listado()
                case "0":
                    break
                case _:
                    print("\nEsa opción no es válida.")
                    input("Presiona Enter para intentar de nuevo...")

    def buscar_auto_por(self, tipo):
        """BUSCAR: Busca un solo auto. Se usa tanto para consultar como para modificar/borrar."""
        try:
            if tipo == "patente":
                patente = input("\nIngrese la patente: ")
                auto = self.auto.seleccionar_auto_por_patente(patente)
            else:
                numero_interno = self.leer_entero("\nIngrese el número interno: ")
                auto = self.auto.seleccionar_auto_por_numero_interno(numero_interno)

            if auto:
                print(f"\n¡AUTO ENCONTRADO!\n{auto}")
            else:
                print("\nLo siento, no pude encontrar ningún auto con ese dato.")
            return auto
        except Exception as error:
            print(f"Hubo un problemita al buscar: {error}")
            return None

    def buscar_auto(self, con_pausa=True):
        """Menú de búsqueda individual."""
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
                case "1" | "2":
                    tipo = "patente" if opcion_seleccionada == "1" else "numero_interno"
                    auto = self.buscar_auto_por(tipo)

                    # Si no lo encontró, pausamos para que lea el error y seguimos en el bucle
                    if not auto:
                        input("\nPresiona Enter para intentar de nuevo...")
                        continue

                    # Si lo encontró, pausamos (si corresponde) y lo devolvemos
                    if con_pausa: 
                        input("\nPresionar Enter para volver")
                    return auto
                case "0":
                    break
                case _:
                    print("\nEsa opción no es válida. 😊")
                    input("Presiona Enter para intentar de nuevo...")

    def cambiar_estado(self):
        """MODIFICAR (Actualizar): Permite cambiar el estado de un auto buscado."""
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
                        print("\nSelecciona el nuevo estado:")
                        nuevo_estado = self.seleccionar_estado()
                        self.auto.cambiar_estado(numero_interno, nuevo_estado)
                        print(f"\n¡Listo! Estado actualizado a '{nuevo_estado}'.")
                    input("\nPresionar Enter para volver")
                case "0":
                    break
                case _:
                    print("\n¡Oops! Opción no válida.")
                    input("Presiona Enter para intentar de nuevo...")

    def pedir_confirmacion(self):
        """MÉTODO DE SEGURIDAD: Pide confirmación antes de acciones críticas."""
        while True:
            confirmar = input("\n¿Confirmar acción? (1: Sí / 0: No): ")
            if confirmar == "1": return True
            if confirmar == "0": return False
            print("Por favor, ingresa 1 o 0.")

    def dar_de_baja_un_auto(self):
        """ELIMINAR (Baja): Borra un registro pidiendo confirmación previa."""
        mensaje = """
        ===================
        DAR DE BAJA UN AUTO
        ===================

        1. Seleccionar auto para eliminar
        0. Volver

        ¿Qué quieres hacer? """

        while True:
            self.limpiar_menu()
            opcion_seleccionada = input(cleandoc(mensaje))
            match opcion_seleccionada:
                case "1":
                    auto = self.buscar_auto(con_pausa=False)
                    if auto:
                        print("\n¡ATENCIÓN! Esta acción no se puede deshacer.")
                        if self.pedir_confirmacion():
                            self.auto.dar_de_baja(auto[0])
                            print("\nEl auto ha sido eliminado.")
                        else:
                            print("\nOperación cancelada. El auto sigue en el sistema.")
                    input("\nPresionar Enter para volver")
                case "0":
                    break
                case _:
                    print("\nOpción no válida.")
                    input("Presiona Enter para intentar de nuevo...")

    def principal(self):
        """MENU PRINCIPAL: El corazón del área de autos."""
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
                case "1": self.cargar_auto_nuevo()
                case "2": self.ver_listado()
                case "3": self.buscar_auto()
                case "4": self.cambiar_estado()
                case "5": self.dar_de_baja_un_auto()
                case "0": break
                case _:
                    print("\n¡Oops! Esa opción no existe.")
                    input("Presiona Enter para volver a intentarlo...")

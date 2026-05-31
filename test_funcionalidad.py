import auto
import os
import database
from datetime import date


def ejecutar_tests():
    print("=== INICIANDO PRUEBAS DE FUNCIONALIDAD (SIN CLASES / CON JSON) ===\n")

    # Limpiar archivos JSON de pruebas anteriores para empezar de cero
    if os.path.exists("autos.json"): os.remove("autos.json")
    if os.path.exists("clientes.json"): os.remove("clientes.json")
    
    # Reiniciamos la memoria de la "base de datos" para este test
    database.lista_de_autos = []
    database.contador_id_autos = 1
    database.lista_de_clientes = []
    database.contador_id_clientes = 1

    # 1. Test de Carga (Alta)
    print("1. Probando carga de autos...")
    datos_auto1 = (
        "ABC-123",
        "Toyota",
        "Corolla",
        2020,
        50000,
        15000,
        "disponible",
        date(2023, 5, 10),
    )
    datos_auto2 = (
        "DEF-456",
        "Ford",
        "Fiesta",
        2018,
        80000,
        10000,
        "vendido",
        date(2023, 6, 15),
    )

    auto.guardar_auto(datos_auto1)
    auto.guardar_auto(datos_auto2)

    todos = auto.seleccionar_todos()
    assert len(todos) == 2, f"Error: Se esperaban 2 autos, hay {len(todos)}"
    print("   [OK] Carga exitosa.")

    # 2. Test de Búsqueda por Patente
    print("2. Probando búsqueda por patente...")
    encontrado = auto.seleccionar_auto_por_patente("ABC-123")
    assert encontrado is not None, "Error: No se encontró el auto ABC-123"
    assert encontrado["marca"] == "Toyota", (
        f"Error: Marca incorrecta {encontrado['marca']}"
    )
    print("   [OK] Búsqueda por patente exitosa.")

    # 3. Test de Búsqueda por ID (Número Interno)
    print("3. Probando búsqueda por ID...")
    encontrado_id = auto.seleccionar_auto_por_numero_interno(1)
    assert encontrado_id is not None, "Error: No se encontró el auto con ID 1"
    assert encontrado_id["patente"] == "ABC-123", "Error: Patente no coincide para ID 1"
    print("   [OK] Búsqueda por ID exitosa.")

    # 4. Test de Filtros (Marca)
    print("4. Probando filtro por marca...")
    toyotas = auto.seleccionar_por("marca", "Toyota")
    assert len(toyotas) == 1, "Error: Se esperaba 1 Toyota"
    print("   [OK] Filtro por marca exitoso.")

    # 5. Test de Filtros (Rango de Precio)
    print("5. Probando filtro por rango de precio...")
    economicos = auto.seleccionar_por_rango(8000, 12000)
    assert len(economicos) == 1, "Error: Se esperaba 1 auto entre $8000 y $12000"
    assert economicos[0]["marca"] == "Ford", (
        "Error: El auto en rango debería ser el Ford"
    )
    print("   [OK] Filtro por precio exitoso.")

    # 6. Test de Cambio de Estado
    print("6. Probando cambio de estado...")
    auto.cambiar_estado(1, "reservado")
    actualizado = auto.seleccionar_auto_por_numero_interno(1)
    assert actualizado["estado"] == "reservado", (
        f"Error: El estado no cambió, es {actualizado['estado']}"
    )
    print("   [OK] Cambio de estado exitoso.")

    # 7. Test de Baja
    print("7. Probando dar de baja (eliminar)...")
    auto.dar_de_baja(2)
    despues_baja = auto.seleccionar_todos()
    assert len(despues_baja) == 1, (
        f"Error: Debería quedar 1 auto, hay {len(despues_baja)}"
    )
    no_existe = auto.seleccionar_auto_por_numero_interno(2)
    assert no_existe is None, "Error: El auto con ID 2 aún existe"
    print("   [OK] Baja exitosa.")

    # 8. Verificación de Tipos Nativos
    print("8. Verificando tipos nativos (Diccionarios y Fechas)...")
    un_auto = despues_baja[0]
    assert isinstance(un_auto, dict), "Error: El registro no es un diccionario"
    # Al usar JSON, las fechas se guardan como texto (str)
    assert isinstance(un_auto["fecha_ingreso"], (date, str)), (
        "Error: La fecha no es un objeto date ni un string"
    )
    print("   [OK] Tipos nativos verificados.")

    print("\n¡TODAS LAS PRUEBAS FUNCIONALES PASARON EXITOSAMENTE!")


if __name__ == "__main__":
    try:
        ejecutar_tests()
    except AssertionError as e:
        print(f"\n[FALLO] {e}")
    except Exception as e:
        print(f"\n[ERROR INESPERADO] {e}")

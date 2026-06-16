import json
import os

ARCHIVO_VENTAS = "ventas.json"


def f_cargar_ventas():
    if not os.path.exists(ARCHIVO_VENTAS):
        return []
    try:
        with open(ARCHIVO_VENTAS, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error al leer el archivo de ventas. Iniciando con lista vacía.")
        return []
    except Exception as e:
        print(f"Error inesperado al cargar ventas: {e}")
        return []


def f_guardar_ventas(ventas):
    try:
        with open(ARCHIVO_VENTAS, "w", encoding="utf-8") as f:
            json.dump(ventas, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar las ventas: {e}")
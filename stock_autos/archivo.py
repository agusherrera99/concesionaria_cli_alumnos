"""
Este módulo fue desarrollado por
BARBERIS Pablo Cesar
creado el 04/06/2026
última modificación 12/06/2026

"""

from .constantes import RUTA_STOCK, CARPETA_DATOS # se importan constantes
import json

CARPETA_DATOS.mkdir(parents=True, exist_ok=True) #crea la carpeta si no existe



def cargar_stock (): #función para cargar el archivo base de dato
    try:
        with open(RUTA_STOCK, 'r', encoding='utf-8') as archivo:
            return json.load (archivo)
    
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_stock (stock_autos):  #función para guardar el archivo base de dato
    with open(RUTA_STOCK, 'w', encoding='utf-8') as archivo:
        json.dump (stock_autos, archivo, indent=4, ensure_ascii=False)
        archivo.write ('\n')
    
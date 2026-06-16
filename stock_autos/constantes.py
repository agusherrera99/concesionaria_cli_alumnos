"""
Este módulo fue desarrollado por
BARBERIS Pablo Cesar
creado el 04/06/2026
última modificación 12/06/2026

"""

from pathlib import Path


#constantes
PATENTE = 'Patente'
MARCA = 'Marca'
MODELO = 'Modelo'
YEAR = 'Año'
KILOMETROS = 'Kilómetros'
PRECIO = 'Precio de venta'
ESTADO = 'Estado'
FECHA = 'Fecha ingreso stock'

BASE_DIR = Path(__file__).resolve().parent  #busca la ruta donde está el archivo que llama la constante
CARPETA_RAIZ = BASE_DIR.parent # subimos un nivel en la ruta
CARPETA_DATOS = CARPETA_RAIZ /'base_datos' #indicamos que ruta usar desde el nivel donde nos dejó la constante anterior
STOCK = 'stock-autos.json' # constante del nombre de la base de datos
RUTA_STOCK = CARPETA_DATOS / STOCK #ruta completa donde se guardará el archivo
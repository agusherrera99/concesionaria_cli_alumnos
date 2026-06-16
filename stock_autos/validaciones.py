"""
Este módulo fue desarrollado por
BARBERIS Pablo Cesar
creado el 04/06/2026
última modificación 12/06/2026

"""

from .mensaje_menu import mensaje

def ingresar_entero (msj:str)->int:
    while True:
        try:
            return int(input (msj))
        except ValueError:
            mensaje ('Debe ingresar un numero. Inténtelo nuevamente')
        

def ingresar_float (msj:str)->float:
    while True:
        try:
            return float(input (msj))
        except ValueError:
            mensaje ('Debe ingresar un numero. Inténtelo nuevamente')
            
def ingresar_year(msj: str) -> int:
    from datetime import datetime
    año_actual = datetime.now().year

    while True:
        year = ingresar_entero(msj)
            
        if 1900 <= year <= año_actual:
            return year
        else:
            mensaje (f"Ingrese un año válido entre 1900 y {año_actual}")

def confirmacion (msj:str):
    while True:
        conf = input (msj).upper()
    
        if conf in ['S', 'N']:
            return conf
        else:
            mensaje ('Debe elgir "S" o "N"')

def salir_prog ():
    conf = confirmacion ('Desea salir del programa? (S/N)')
    
    if conf == 'S':
        return True
    else:
        mensaje ('Operación cancelada')
        return False
    



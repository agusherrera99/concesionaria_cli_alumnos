from mensaje_menu2 import mensaje
from datetime import date

def ingresar_fecha(msj: str) -> date:
    while True:
        try:
            return date.fromisoformat(input(msj))
        except ValueError:
            mensaje("Fecha inválida. Formato: YYYY-MM-DD")

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
            print ('Debe elgir "S" o "N"')

def salir_prog ():
    conf = confirmacion ('Desea salir del programa? (S/N)')
    
    if conf == 'S':
        return True
    else:
        print ('Operación cancelada')
        return False
    



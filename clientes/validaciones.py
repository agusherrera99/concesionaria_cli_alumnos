"""
Este archivo funciona como nuestra base de datos.
Ahora usamos archivos JSON para que los datos NO se borren al cerrar el programa.

alumna: Maria Laura Castro
programacion I UNER
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
            

def confirmacion (msj:str):
    while True:
        conf = input (msj).upper()
    
        if conf in ['S', 'N']:
            return conf
        else:
            print ('Debe elgir "S" o "N"')


    



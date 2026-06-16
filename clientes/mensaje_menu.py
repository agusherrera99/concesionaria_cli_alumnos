"""
Este archivo funciona como nuestra base de datos.
Ahora usamos archivos JSON para que los datos NO se borren al cerrar el programa.

alumna: Maria Laura Castro
programacion I UNER
"""


def mensaje (txt, separador=True):
    
    if separador:
        print ('-'*50)
    print (txt)
    if separador:
        print ('-'*50)
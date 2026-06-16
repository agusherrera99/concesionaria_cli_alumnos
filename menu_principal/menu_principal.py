"""
Este módulo fue desarrollado por
BARBERIS Pablo Cesar
creado el 12/06/2026
última modificación 12/06/2026

"""

from stock_autos import main as stock
from clientes import main as cli
from .validaciones import ingresar_entero, salir_prog
from .mensaje_menu import mensaje




def menu_principal ():
    
    while True:
        print ('=============== SISTEMA CONCESIONARIA ===============')
        print ('1.- Ingreso al stock de vehículos')
        print ('2.- Clientes')
        print ('3.- Ventas')
        print ('4.- Reservas')
        print ('5.- Vendedores')
        print ('0.- Salir')
        print ('==================== UNER =====================')
        
        opcion = ingresar_entero ('Elija una opcion: ')
        
        match opcion:
            case 1:
                stock ()
            case 2:
                cli ()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 0:
                if salir_prog ():
                    mensaje ('Hasta luego')
                    break
            case _:
                mensaje ('Opción no válida. Intente nuevamente')
    

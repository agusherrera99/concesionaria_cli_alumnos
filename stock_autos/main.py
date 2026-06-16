"""
Este módulo fue desarrollado por
BARBERIS Pablo Cesar
creado el 04/06/2026
última modificación 12/06/2026

"""
#importamos funciones
from .archivo import cargar_stock
from .manejo_stock import menu_stock

def main (): #función para cargar el stock en memoria e ingresar al menú para el manejo del stock
    stock_autos = cargar_stock ()
    menu_stock (stock_autos)

if __name__=='__main__':   
    main ()
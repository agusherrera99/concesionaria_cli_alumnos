"""
Este módulo fue desarrollado por
BARBERIS Pablo Cesar
creado el 06/06/2026
última modificación 12/06/2026

"""

from .consulta import busqueda_patente
from .archivo import guardar_stock
from .mensaje_menu import mensaje

def auto_vendido (stock_autos, patente):
    
    patente = input ('Ingrese la patente del vehículo a consultar: ').upper ()
    auto = busqueda_patente (stock_autos, patente)
    
    if auto:
        id_auto = auto['Id']
        
        marcar_vendido (auto)
        guardar_stock (stock_autos)
        mensaje (f'Venta realizada. Número Interno del auto: {id_auto}')
    else:
        mensaje ('No se encontro vehículo')
    return id_auto


def marcar_vendido (auto):
    auto['Estado'] = 'Vendido'

def auto_reservado (stock_autos, patente):
    
    patente = input ('Ingrese la patente del vehículo a consultar: ').upper ()
    auto = busqueda_patente (stock_autos, patente)
    
    if auto:
        id_auto = auto['Id']
        
        marcar_reservado (auto)
        guardar_stock (stock_autos)
        mensaje (f'Reserva realizada. Número Interno del auto: {id_auto}')
    else:
        mensaje ('No se encontro vehículo')

def marcar_reservado (auto):
    auto['Estado'] = 'Reservado'
    
def auto_cliente (stock_autos, patente):
    patente = input ('Ingrese la patente del vehículo a consultar: ').upper ()
    auto = busqueda_patente (stock_autos, patente)
    
    if auto:
        return auto
    else:
        mensaje ('No se encontró un vehículo con esa patente')
    
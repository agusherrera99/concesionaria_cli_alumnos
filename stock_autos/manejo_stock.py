"""
Este módulo fue desarrollado por
BARBERIS Pablo Cesar
creado el 04/06/2026
última modificación 12/06/2026

"""
#importación de constantes y funciones
from .constantes import PATENTE, MARCA, MODELO, YEAR, KILOMETROS, PRECIO, ESTADO, FECHA
from .validaciones import ingresar_entero, ingresar_float, ingresar_year, salir_prog, mensaje, confirmacion
from .consulta import menu_consulta, busqueda_patente
from .archivo import guardar_stock


def menu_stock (stock_autos):
    
    while True:
        print ('=============== STOCK VEHÍCULOS ===============')
        print ('1.- Ingreso vehículo al stock.')
        print ('2.- Baja vehículo del stock')
        print ('3.- Modificación datos del vehículo')
        print ('4.- Consulta del stock')
        print ('0.- Salir')
        print ('==================== UNER =====================')
        
        opcion = ingresar_entero ('Elija una opcion: ')
        
        match opcion:
            case 1:
                ingreso_auto (stock_autos)
            case 2:
                menu_baja_auto (stock_autos)
            case 3:
                modifica_auto (stock_autos)
            case 4:
                menu_consulta (stock_autos)
            case 0:
                #if salir_prog ():
                break
            case _:
                mensaje ('Opción no válida. Intente nuevamente')



def ingreso_auto (stock_autos):
    id_auto = id_vehiculo (stock_autos)
    patente = ingreso_patente (stock_autos, 'Ingrese la patente del vehículo: ')
    marca = input ('Ingrese la marca del vehículo: ').upper ()
    modelo = input ('Ingrese el modelo del vehículo: ').upper ()
    year = ingresar_year ('Ingrese el año del vehículo: ')
    kilometros = ingresar_entero ('Ingrese el kilometraje del vehículo: ')
    precio = ingresar_float ('Ingrese el precio del vehículo: ')
    estado = estado_vehiculo ()
    fecha_ingreso = fecha ()
                    
    auto = {
        'Id':id_auto,
        PATENTE: patente,
        MARCA: marca, 
        MODELO: modelo,
        YEAR: year,
        KILOMETROS: kilometros,
        PRECIO: precio,
        ESTADO:estado,
        FECHA: fecha_ingreso
    }
    stock_autos.append (auto)
    guardar_stock (stock_autos)

def id_vehiculo (stock_autos):
    if len(stock_autos) == 0:
        id_auto = 1
    else:
        id_auto = max(auto['Id'] for auto in stock_autos) + 1
    return id_auto

def ingreso_patente (stock_autos, msj:str):
    while True:
        patente = input (msj).upper ()
                
        if busqueda_patente (stock_autos, patente):
            mensaje ('Patente existente. Debe ingresar una diferente')
        else:
            return patente

def fecha ():
    from datetime import datetime
    
    while True:
        fecha = input ('Ingrese la fecha de ingreso del vehículo (DD/MM/AAAA): ')
        formato = '%d/%m/%Y'
    
        try:
            datetime.strptime (fecha, formato)
            return fecha
        except ValueError:
            mensaje ('La fecha es inválida o el formato es incorrecto.')

def estado_vehiculo ():
    while True:
        print ('Elija el estado actual del vehículo')
        print ('1.- Disponible')
        print ('2.- Reservado')
        print ('3.- Vendido')
        print ('4.- En Taller')
        #print ('0.- salir')
        
        opcion = ingresar_entero ('Elija una opcion: ')
    
        match opcion:
            case 1:
                estado = 'DISPONIBLE'
                break
            case 2:
                estado = 'RESERVADO'
                break
            case 3:
                estado = 'VENDIDO'
                break
            case 4:
                estado = 'EN TALLER'
                break
            case _:
                mensaje ('Opción no válida. Intente nuevamente')
    return estado


def menu_baja_auto (stock_autos):
    if len (stock_autos) == 0:
        mensaje ('El stock se encuentra VACÍO')
        return

    while True:
        print ('========== Baja Vehículo =========')
        print ('1.- Baja por patente')
        print ('2.- Baja por modelo y año')
        print ('0.- Salir')
        print ('==================================')
        
        
        opcion = ingresar_entero ('Elija una opcion: ')
    
        match opcion:
            case 1:
                baja_patente (stock_autos)
            case 2:
                baja_modelo_year (stock_autos)
            case 0:
                break
            case _:
                mensaje ('Opción no válida. Intente nuevamente')
                
                
def baja_patente (stock_autos):
    patente = input ('Ingrese la patente del vehículo a dar de baja: ').upper ()
    
    auto = busqueda_patente (stock_autos, patente)
    
    if auto:
        conf = confirmacion ('Está seguro que quiere eliminar el vehículo? (S/N)')
        
        if conf == 'N':
            mensaje ('Operación cancelada')
            return
        
        else:
            stock_autos.remove (auto)
            guardar_stock (stock_autos)
            mensaje ('Vehículo eliminado')
    
    else:
        mensaje ('No se encontró vehículo')
         
def baja_modelo_year (stock_autos):
    modelo = input ('Ingrese el modelo del vehículo: ').upper ()
    year = ingresar_year ('Ingrese el año del vehículo: ')
    
    for auto in stock_autos:
        if modelo == auto[MODELO] and year == auto[YEAR]:
            conf = confirmacion ('Está seguro que quiere eliminar el vehículo? (S/N)')
            
            if conf == 'N':
                mensaje ('Operación cancelada')
                return
            
            else:
                stock_autos.remove (auto)
                guardar_stock (stock_autos)
                mensaje ('Vehículo eliminado')
                return
            
    mensaje ('No se encontró vehículo con esa descripción')

def modifica_auto (stock_autos):
    while True:
        print ('------------------------------------------------')
        print ('1.- Ingrese la patente del vehículo a modificar')
        print ('0.- Salir')
        
        opcion = ingresar_entero ('Elija una opcion: ')
        
        match opcion:
            case 1:
                patente = input ('Ingrese la patente de vehículo a modificar: ').upper ()
                auto = busqueda_patente (stock_autos, patente)
                
                if auto:
                    mensaje ('vehículo encontrado')
                    if modifica_variable (stock_autos, auto):
                        guardar_stock (stock_autos)
                else:
                    mensaje ('No se encontró el vehículo')
            case 0:
                break
            case _:
                mensaje ('Opción no válida. Intente nuevamente')
            
def modifica_variable (stock_autos, auto):
    cambio = False
    
    while True:
        if auto:
            print ('------------------------------')
            print ('Que elemento desea modificar?')
            print ('1.- Patente')
            print ('2.- Marca')
            print ('3.- Modelo')
            print ('4.- Año')
            print ('5.- Kilómetros')
            print ('6.- Precio de venta')
            print ('7.- Estado')
            print ('8.- Fecha de ingreso al stock')
            print ('0.- Salir')
            print ('------------------------------')
            
            opcion = ingresar_entero ('Elija una opcion: ')
            match opcion:
                
                case 1:
                    cambio_patente (stock_autos, auto)
                    cambio = True
                case 2:
                    auto[MARCA] = input ('Ingrese la marca del vehículo: ').upper ()
                    cambio = True
                case 3:
                    auto[MODELO] = input ('Ingrese el modelo del vehículo: ').upper ()
                    cambio = True
                case 4:
                    auto[YEAR] = ingresar_year ('Ingrese el año del vehículo: ')
                    cambio = True
                case 5:
                    auto[KILOMETROS] = ingresar_entero ('Ingrese el kilometraje del vehículo: ')
                    cambio = True
                case 6:
                    auto[PRECIO] = ingresar_float ('Ingrese el precio del vehículo: ')
                    cambio = True
                case 7:
                    auto[ESTADO] = estado_vehiculo ()
                    cambio = True
                case 8:
                    auto[FECHA] = fecha ()
                    cambio = True
                case 0:
                    return
                case _:
                    mensaje ('Opción no válida. Intente nuevamente')
            if cambio:
                mensaje ('Modificación realizada')
                guardar_stock (stock_autos)
    return cambio
                
def cambio_patente (stock_autos, auto):
    while True:
        nueva_patente = input ('Ingrese la patente del vehículo: ').upper ()
    
        if busqueda_patente (stock_autos, nueva_patente):
            mensaje ('La patente ya existe')
            
        else:
            auto[PATENTE] = nueva_patente
            return
    return





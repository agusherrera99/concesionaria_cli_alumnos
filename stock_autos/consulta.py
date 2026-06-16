"""
Este módulo fue desarrollado por
BARBERIS Pablo Cesar
creado el 04/06/2026
última modificación 13/06/2026

"""
from rich.table import Table
from rich.console import Console
console = Console ()
#importación de constantes y funciones
from .constantes import PATENTE, MARCA, MODELO, YEAR, KILOMETROS, PRECIO, ESTADO, FECHA
from .validaciones import mensaje, ingresar_entero, ingresar_float, ingresar_year

        
def menu_consulta (stock_autos):
    while True:
        print ('========== Consulta del Stock =========')
        print ('1.- Listado de los vehículos')
        print ('2.- Buscar vehículo')
        print ('3.- Filtrar vehículos')
        print ('0.- Salir')
        print ('======================================')
        
        
        opcion = ingresar_entero ('Elija una opcion: ')
    
        match opcion:
            case 1:
                listado_stock (stock_autos)
            case 2:    
                buscar_auto (stock_autos)
            case 3:
                consulta_stock (stock_autos)
            case 0:
                break
            case _:
                mensaje ('Opción no válida. Intente nuevamente')

def listado_stock (stock_autos): #esta función es para listar los autos en stock
    encontrados = []
    if len (stock_autos) == 0: # verificación si hay algo cargado en stock
        mensaje ('El stock se encuentra VACÍO')
        return
        
    else:
        #mensaje ('========== LISTADO DEL STOCK ==========', separador=False)
        for auto in stock_autos:
            encontrados.append (auto)
            
        if encontrados:    
            respuesta_pantalla (encontrados)  
  
def buscar_auto (stock_autos): #esta función es para consultar los autos en stock
    if len (stock_autos) == 0: # verificación si hay algo cargado en stock
        mensaje ('El stock se encuentra VACÍO')
        return

    while True:
        print ('========== Buescar Vehículo =========')
        print ('1.- Consulta por numero interno')
        print ('2.- Consulta por patente')
        print ('0.- Salir')
        print ('======================================')
        
        
        opcion = ingresar_entero ('Elija una opcion: ')
    
        match opcion:
            case 1:
                consulta_id (stock_autos)
            case 2:    
                consulta_patente (stock_autos)
            case 0:
                break
            case _:
                mensaje ('Opción no válida. Intente nuevamente')


def consulta_stock (stock_autos): #esta función es para consultar los autos en stock
    if len (stock_autos) == 0: # verificación si hay algo cargado en stock
        mensaje ('El stock se encuentra VACÍO')
        return

    while True:
        print ('========== Consulta Vehículo =========')
        print ('1.- Consulta por marca')
        print ('2.- Consulta por modelo')
        print ('3.- Consulta por año')
        print ('4.- Consulta por precio')
        print ('5.- Consulta por estado')
        print ('0.- Salir')
        print ('======================================')
        
        
        opcion = ingresar_entero ('Elija una opcion: ')
    
        match opcion:
            case 1:
                consulta_marca (stock_autos)
            case 2:
                consulta_modelo (stock_autos)
            case 3:
                consulta_year (stock_autos)
            case 4:
                consulta_precio (stock_autos)
            case 5:
                consulta_estado (stock_autos)
            case 0:
                break
            case _:
                mensaje ('Opción no válida. Intente nuevamente')

def consulta_id (stock_autos):
    id_auto = ingresar_entero ('Ingrese el número interno del vehículo: ')
    encontrados = []
    
    for auto in stock_autos:
        if id_auto == auto['Id']:
            encontrados.append (auto)
        
        if encontrados:    
            respuesta_pantalla (encontrados)
            return
        
        
    mensaje ('No se encontró un vehículo con ese número interno')
    return


def consulta_patente (stock_autos):
    patente = input ('Ingrese la patente del vehículo a consultar: ').upper ()
    encontrados = []
    
    for auto in stock_autos:
        if patente == auto[PATENTE]:
            encontrados.append (auto)
        
        if encontrados:    
            respuesta_pantalla (encontrados)
            return
    
    mensaje ('No se encontró un vehículo con esa patente')
    return

def consulta_marca (stock_autos):
    marca = input ('Ingrese la marca del vehículo a consultar: ').upper ()
    encontrados = []
    
    for auto in stock_autos:
        if marca == auto[MARCA]:
            encontrados.append (auto)
        
    if encontrados: 
        respuesta_pantalla (encontrados)
        #for auto in encontrados:   
        #    respuesta_pantalla (auto)
            
    else :
        mensaje ('No se encontraron vehículos de esa marca')
    return

def consulta_modelo (stock_autos):
    modelo = input ('Ingrese el modelo del vehículo a consultar: ').upper ()
    encontrados = []
    
    for auto in stock_autos:
        if modelo == auto[MODELO]:
            encontrados.append (auto)
        
    if encontrados:
        respuesta_pantalla (encontrados) 
        #for auto in encontrados:   
        #    respuesta_pantalla (auto)
        
    else :
        mensaje ('No se encontraron vehículos de ese modelo')
    return

def consulta_year (stock_autos):
    year = ingresar_year ('Ingrese el año del vehículo: ')
    encontrados = []
    
    for auto in stock_autos:
        if year == auto[YEAR]:
            encontrados.append (auto)
        
    if encontrados: 
        respuesta_pantalla (encontrados)
        #for auto in encontrados:   
        #    respuesta_pantalla (auto)
            
    else :
        mensaje ('No se encontraron vehículos de ese año')
    return

def consulta_precio (stock_autos):
    precio_min = ingresar_float ('Ingrese el precio mínimo: ')
    precio_max = ingresar_float ('Ingrese el precio máximo: ')
    encontrados = []
    
    for auto in stock_autos:
        if precio_min <= auto[PRECIO] <= precio_max:
           encontrados.append (auto)
        
    if encontrados: 
        respuesta_pantalla (encontrados)
        #for auto in encontrados:   
            #respuesta_pantalla (auto)
        
    else :
        mensaje ('No se encontraron vehículos de ese precio') 
    return

def consulta_estado (stock_autos):
    estado = input ('Ingrese el estado del vehículo: ').upper ()
    encontrados = []
    
    for auto in stock_autos:
        if estado == auto[ESTADO]:
            encontrados.append (auto)
        
    if encontrados: 
        respuesta_pantalla (encontrados)
            
    else :
        mensaje ('No se encontraron vehículos de ese año')
    return encontrados

def respuesta_pantalla (encontrados):
    #print ("--------------------------------------------------")
    #print (f"ID auto: {auto['Id']}")
    #print (f"Patente: {auto[PATENTE]}")
    #print (f"Marca: {auto[MARCA]}")
    #print (f"Modelo: {auto[MODELO]}")
    #print (f"Año: {auto[YEAR]}")
    #print (f"Kilómetros: {auto[KILOMETROS]}")            
    #print (f"Precio de venta: {auto[PRECIO]:.2f}")
    #print (f"Estado: {auto[ESTADO]}")
    #print (f"Fecha de ingreso al stock: {auto[FECHA]}")
    print ("="*100)
    table = Table(title="VEHÍCULOS EN STOCK")
    
    table.add_column ("N. INT")
    table.add_column ("PATENTE")
    table.add_column ("MARCA")
    table.add_column ("MODELO")
    table.add_column ("AÑO")
    table.add_column ("KILOMETROS")
    table.add_column ("PRECIO")
    table.add_column ("ESTADO")
    table.add_column ("FECHA INGRESO")
    
    for auto in encontrados:   
        table.add_row (str(auto['Id']), 
                       (auto[PATENTE]), 
                       (auto[MARCA]), 
                       (auto[MODELO]), 
                       str(auto[YEAR]), 
                       str(auto[KILOMETROS]), 
                       (f'{auto[PRECIO]:.2f}'), 
                       (auto[ESTADO]), 
                       (auto[FECHA]))
    
    console.print (table)
    return


    
    

def busqueda_patente (stock_autos, patente):
    for auto in stock_autos:
        if patente == auto [PATENTE]:
            return auto
    return None




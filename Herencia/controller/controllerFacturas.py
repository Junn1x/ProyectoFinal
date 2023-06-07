from datetime import datetime
import sys
import os
path = os.path.abspath('crud/')
sys.path.append(path)
import crudFacturas
productos = []

crud_facturas = crudFacturas.CrudDeFactura()

def crear_factura(listaProductos):
    fecha = datetime.now().strftime("%Y-%m-%d")
    respuesta = crud_facturas.crear(listaProductos , fecha)
    return respuesta

def datos_productos(factura):
    return crud_facturas.informacion_productos(factura)
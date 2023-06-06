from datetime import datetime
import sys
import os
path = os.path.abspath('crud/')
sys.path.append(path)
import crudFacturas
productos = []

crud_facturas = crudFacturas.CrudDeFactura()

def crear_factura(ListaProductos):
    fecha = datetime.now().strftime("%Y-%m-%d")
    respuesta = crud_facturas.crear(ListaProductos , fecha)
    return respuesta


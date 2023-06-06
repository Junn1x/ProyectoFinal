import sys
import os
path = os.path.abspath('crud/')
sys.path.append(path)
import crudProductos
productos = []

crud_productos = crudProductos.CrudProductos()

def crear_producto(tipo):
    mensaje = crud_productos.crear(**tipo)
    return mensaje

def obtener_productos():
    productos = crud_productos.obtener()
    return productos

def productos_objeto(productos_sujeridos):
    productos = crud_productos.cambiar(productos_sujeridos)
    return productos
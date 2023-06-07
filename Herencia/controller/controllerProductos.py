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

def productos_objeto(productos_sugeridos):
    productos = crud_productos.cambiar(productos_sugeridos)
    return productos

def obtener_id():
    productos = crud_productos.obtener_id()
    return productos

def obtener_id_individual(producto):
    id_producto = crud_productos.obtener_id_individual(producto)
    return id_producto

def informacion_producto(id_producto):
    resultado = crud_productos.buscar_informacion(id_producto)
    return resultado
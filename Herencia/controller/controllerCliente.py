import sys
import os
path = os.path.abspath('crud/')
sys.path.append(path)
import crudClientes
clientes = []

crud_cliente = crudClientes.CrudCliente()
def crear_cliente(datos):
    mensaje = crud_cliente.crear(**datos)
    return mensaje

def obtener_clientes():
    clientes = crud_cliente.obtener()
    return clientes

def buscar_cliente(cliente_seleccionado):
    cliente = crud_cliente.buscar(cliente_seleccionado)
    return cliente

def agregar_factura(cliente, factura):
    mensaje = crud_cliente.agregar(cliente, factura)

import icrud
import sys
import os
path = os.path.abspath('Modelo/')
sys.path.append(path)
import claseClientes 

class CrudCliente ( icrud.ICrud ) :
    def __init__(self):
        self.clientes = []

    def crear(self, **kwargs):
        nuevo_cliente = claseClientes.Cliente(kwargs['id'] , kwargs['nombre'],  kwargs['facturas'])
        self.clientes.append(nuevo_cliente)
        mensaje = "Se creo el cliente"
        return {'mensaje': mensaje, 'cliente_nuevo': nuevo_cliente}

    def agregar(self, cliente, factura):
        print("Factura antes es: ", cliente.facturas)
        cliente.agregarFactura(factura)
        print("Factura despues es: ", cliente.facturas)
        return {'mensaje': "Se ha agregado la factura"}

    def buscar(self, cliente_pedido):
        clientes = claseClientes.Cliente.cuentaClientes
        for cliente in clientes:
            if cliente.cedula == cliente_pedido:
                return cliente
    
    def obtener(self):
        id_clientes = []
        clientes = claseClientes.Cliente.cuentaClientes
        for cliente in clientes:
            id_clientes.append(cliente.cedula)
        return id_clientes
    
    def obtener_facturas(self, cuenta):
        lista_facturas = cuenta.facturas
        return lista_facturas

    def nombreCliente(self, cliente):
        return cliente.nombre

    def mostrar(self, **kwargs):
        id = kwargs.get('id')
        if id:
            for c in self.clientes:
                if c.idCliente == id:
                    datos = {'cliente': c, 'success' : True, 'mensaje': 'El cliente ya existe'}
                    return datos
            mensaje = "No se encontró al cliente"
        else:
            mensaje = "Digite una id"
        return {'mensaje': mensaje , 'success' : False}

    def actualizar(self, **kwargs):
        id = kwargs.get('id')
        nuevoNombre = kwargs.get('nuevoNombre')
        if id and nuevoNombre:
            for c in self.clientes:
                if c.id == id:
                    c.nombre = nuevoNombre
                    mensaje = 'Cliente actualizado exitosamente'
                    return {'mensaje': mensaje}
            mensaje = 'No se encontró al cliente'
        else:
            mensaje = 'No se ha proporcionado cédula o un nombre nuevo'
        return {'mensaje': mensaje}

    def eliminar(self, **kwargs):
        id = kwargs.get('id')
        if id:
            for c in self.clientes:
                if c.id == id:
                    self.clientes.remove(c)
                    mensaje = 'Se ha eliminado el cliente'
                    return {'mensaje': mensaje}
            mensaje = 'No se ha encontrado este cliente'
        else:
            mensaje = 'No se ha proporcionado cédula'
        return {'mensaje': mensaje}
    
    def relacion(self, **kwargs):
        id = kwargs.get('id')
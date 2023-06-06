import icrud
import sys
import os
path = os.path.abspath('Modelo/')
sys.path.append(path)
import claseFacturas 

class CrudDeFactura ( icrud.ICrud ) :
    def __init__(self):
        self.facturas = []

    def crear(self, productos , fecha):
        nuevaFactura = claseFacturas.Factura(productos['productos'], fecha , productos['costo'])
        self.facturas.append(nuevaFactura)
        mensaje = "Se creo el la nueva factura"
        return {'mensaje': mensaje, 'nueva_factura': nuevaFactura}

    def agregar(self, **kwargs):
        factura = kwargs.get('factura')
        cliente = kwargs.get('cliente')
        if cliente and factura:
            cliente.facturas.append(factura)
            mensaje = "Se ha agregado la factura"
        else:
            mensaje = "Digite cliente o factura"
        return {'mensaje': mensaje}

    def consultar(self, **kwargs):
        cedula = kwargs.get('cedula')
        if cedula:
            for c in self.clientes:
                if c.cedulaCliente == cedula:
                    datos = {'cliente': c, 'success' : True, 'mensaje': 'El cliente ya existe'}
                    return datos
            mensaje = "No se encontró al cliente"
        else:
            mensaje = "Digite una cedula"
        return {'mensaje': mensaje , 'success' : False}

    def actualizar(self, **kwargs):
        fechaCompra = kwargs.get('fechaCompra')
        if fechaCompra :
            for c in self.facturas:
                if c.fechaCompra== fechaCompra:
                    mensaje = 'Factura actualizada'
                    return {'mensaje': mensaje}
            mensaje = 'No se encontró la factura'
        else:
            mensaje = 'No se ha proporcionado fecha de compra'
        return {'mensaje': mensaje}

    def eliminar(self, **kwargs):
        fechaCompra = kwargs.get('fecha')
        if fechaCompra:
            for c in self.facturas:
                if c.cedula == fechaCompra:
                    self.facturas.remove(c)
                    mensaje = 'Se ha eliminado la factura'
                    return {'mensaje': mensaje}
            mensaje = 'No se ha encontrado la factura'
        else:
            mensaje = 'No se ha proporcionado fecha'
        return {'mensaje': mensaje}

    def mostrar(self, **kwargs):
        id = kwargs.get('id')
    
    def relacion(self, **kwargs):
        id = kwargs.get('id')
from crud import icrud
import sys
import os
path = os.path.abspath('clases/')
sys.path.append(path)
from Modelo import ControlDePlagas 

class CrudControlPlagas ( icrud.ICrud ) :
    def __init__(self):
        self.ControlDePlagas = []

    def crear(self, **kwargs):
        ncp = ControlDePlagas.ControlDePlagas(kwargs['idProducto'], kwargs['conombreProductosto'], kwargs['precio'], kwargs['ica'],kwargs['frecuenciaAplicacion'],kwargs['periodoCarencia'])
        self.ControlDePlagas.append(ncp)
        mensaje = "Se creo el cliente"
        return {'mensaje': mensaje, 'nueva factura': ncp}

    def agregar(self, **kwargs):
        factura = kwargs.get('factura')
        ncp = kwargs.get('ncp')
        if ncp and factura:
            cliente.facturas.append(factura)
            mensaje = "Se ha agregado la factura"
        else:
            mensaje = "Digite cliente o factura"
        return {'mensaje': mensaje}

    def consultar(self, **kwargs):
        idProducto = kwargs.get('idProducto')
        if idProducto:
            for c in self.ControlDePlagas:
                if c.idProducto == idProducto:
                    datos = {'producto': c, 'success' : True, 'mensaje': 'El producto ya existe'}
                    return datos
            mensaje = "No se encontró el producto"
        else:
            mensaje = "Digite un id de producto"
        return {'mensaje': mensaje , 'success' : False}


    def eliminar(self, **kwargs):
        idProducto = kwargs.get('idProducto')
        if idProducto:
            for c in self.facturas:
                if c.idProducto == idProducto:
                    self.ControlDePlagas.remove(c)
                    mensaje = 'Se ha eliminado el producto'
                    return {'mensaje': mensaje}
            mensaje = 'No se ha encontrado el producto'
        else:
            mensaje = 'No se ha proporcionado un id de producto'
        return {'mensaje': mensaje}
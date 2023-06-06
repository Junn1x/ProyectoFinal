import icrud
import sys
import os
path = os.path.abspath('Modelo/')
sys.path.append(path)
import medicina
import ControlDeFertilizantes
import ControlDePlagas 

class CrudProductos ( icrud.ICrud ) :
    def __init__(self):
        self.productos = []

    def crear(self, **kwargs):
        if kwargs['tipo'] == 0:
            nuevoProducto = medicina.Medicina(kwargs['id_producto'],kwargs['nombre_producto'],kwargs['precio'],kwargs['dosis'],kwargs['tipo_animal'])
            mensaje = "Se creo el producto"
        elif kwargs['tipo'] == 1:
            nuevoProducto = ControlDeFertilizantes.ControlDeFertilizantes(kwargs['id_producto'],kwargs['nombre_producto'],kwargs['precio'],kwargs['ica'],kwargs['frecuencia_aplicacion'],kwargs['ultima_aplicacion'])
            mensaje = "Se creo el producto"
        else:
            nuevoProducto = ControlDePlagas.ControlDePlagas(kwargs['id_producto'],kwargs['nombre_producto'],kwargs['precio'],kwargs['ica'],kwargs['frecuencia_aplicacion'],kwargs['periodo_carencia'])
            mensaje = "Se creo el producto"
        self.productos.append(nuevoProducto)
        return {'mensaje': mensaje, 'nuevo_producto': nuevoProducto}
    
    def mostrar(self, **kwargs):
        id = kwargs.get('id')
    
    def relacion(self, **kwargs):
        id = kwargs.get('id')
        
    def obtener(self):
        productos = []
        for producto in self.productos:
            productos.append(producto.nombreProducto)
        return productos
    
    def cambiar(self, listaProductos):
        productos_obtenidos = []
        costo = 0
        for pedido in listaProductos:
            for producto in self.productos:
                if producto.nombre == pedido:
                    productos_obtenidos.append(producto)
                    costo = costo + producto.precio
        return {'productos' : productos_obtenidos , 'costo': costo}


    
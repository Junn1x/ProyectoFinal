from clases import claseClientes
from clases import claseFacturas
from clases import claseProductos

class Crud:
    @classmethod
    def crear_cliente(cls,cedula,nombre,facturas):
        return claseClientes.Cliente(cedula,nombre,facturas)
    
    @classmethod
    def crear_producto_fertilizante(cls,idproducto,nombreProducto,precio,ica,frecuenciaAplicacion,ultimaAplicaion):
        return claseProductos.ControlDeFertelizantes(idproducto,nombreProducto,precio,ica,frecuenciaAplicacion,ultimaAplicaion)
    
    @classmethod
    def crear_producto_plagas(cls,idProducto,nombreProducto,precio,ica,frecuenciaAplicacion,periodoCarencia):
        return claseProductos.ControlDePlagas(idProducto,nombreProducto,precio,ica,frecuenciaAplicacion,periodoCarencia)
    
    @classmethod
    def crear_producto_medicina(cls,idProducto,nombreProducto,precio,dosis,tipoAnimal):
        return claseProductos.Medicina(idProducto,nombreProducto,precio,dosis,tipoAnimal)
    
    @classmethod
    def crear_factura(cls,productos,fechaCompra,costo):
        return claseFacturas.Factura(productos,fechaCompra,costo)
    
    @classmethod
    def leer_clientes(cls,cedula):
        for cliente in claseClientes.Cliente.cuentaClientes:
            if cliente.cedula == cedula:
                return cliente

    def leer_producto(self,idproducto):
        for producto in claseProductos.Producto.nombreProducto:
            if producto.idproducto == idproducto:
                return producto
            
    def leer_factura(self,fechaCompra,cedula):
        for cliente in claseClientes.Cliente.cuentaClientes:
            if cliente.cedula == cedula:
                for factura in claseFacturas.Factura.facturas:
                    if factura.fechaCompra == fechaCompra:
                        return factura
                    
    def update_cliente_nombre(self,cedula, nuevo_nombre):
        for cliente in claseClientes.Cliente.cuentaClientes:
            if cliente.cedula == cedula:
                cliente.nombre = nuevo_nombre
                return cliente

    def update_cliente_cedula(self,nueva_cedula, nombre):
        for cliente in claseClientes.Cliente.cuentaClientes:
            if cliente.nombre == nombre:
                cliente.cedula = nueva_cedula
                return cliente

    def update_producto_id(self,nuevo_idproducto,idProducto):
        for producto in claseProductos.Producto.productos:
            if producto.idProducto == idProducto:
                producto.idProducto == nuevo_idproducto
                return producto
            
    def update_producto_nombre(self,nuevo_nombre,idProducto):
        for producto in claseProductos.Producto.productos:
            if producto.idProducto == idProducto:
                producto.nombreProducto == nuevo_nombre
                return producto
            
    def update_producto_costo(self,nuevo_costo,idProducto):
        for producto in claseProductos.Producto.productos:
            if producto.idProducto == idProducto:
                producto.idProducto == nuevo_costo
                return producto
            
    def update_factura_fechaCompra(self,fechaCompra,nueva_fechaCompra):
        for factura in claseFacturas.Factura.facturas:
            if factura.fechaCompra == fechaCompra:
                factura.fechaCompra == nueva_fechaCompra
                return factura
            
    def delete_cliente(self, cedula):
        for numeroCliente, cliente in enumerate(claseClientes.Cliente.cuentaClientes):
            if cliente.cedula == cedula:
                del claseClientes.Cliente.cuentaClientes[numeroCliente]
                print("Cliente eliminado exitosamente")
                return
        print("No se encontró ningún cliente con esa cédula")

    def delete_producto(self,idProducto):
        for numeroProducto, producto in enumerate(claseProductos.Producto.productos):
            if producto.idProducto == idProducto:
                del claseProductos.Producto.productos[numeroProducto]
                return producto
            
    def delete_factura(self,cedula,fechaCompra):
        for cliente in claseClientes.Cliente.cuentaClientes:
            if cliente.cedula == cedula:
                for factura,numeroFactura in claseFacturas.Factura.facturas:
                    if factura.fechaCompra == fechaCompra:
                        del claseFacturas.Factura.facturas[numeroFactura]

class Factura:

    facturas = []
    def __init__(self, productos, fechaCompra, costo):
        if fechaCompra == "" or costo =="":
            raise(TypeError("Debes ingresar todos los campos"))
        try:
            int(costo)
        except ValueError:
            raise(ValueError("El costo solo debe contener numeros"))
        if productos == None:
            raise(TypeError("La factura debe tener productos"))
        self.__productos = productos
        self.__fechaCompra = fechaCompra
        self.__costo = costo
        self.__class__.facturas.append(self)

    @property
    def productos(self):
        return self.__productos

    @productos.setter
    def productos(self, productos):
        self.__productos = productos 
    
    @property
    def fechaCompra(self):
        return self.__fechaCompra

    @fechaCompra.setter
    def fechaCompra(self, fechaCompra):
        self.__fechaCompra = fechaCompra 

    @property
    def costo(self):
            return self.__costo

    @costo.setter
    def costo(self, costo):
        self.__costo = costo

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.costo += producto.precio

    @classmethod
    def obtenerFacturas(cls):
        return cls.facturas    

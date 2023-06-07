
class Producto:

    productos = []
    def __init__(self, idProducto, nombreProducto, precio):
        if idProducto == "" or nombreProducto =="" or precio=="":
                raise(TypeError("Debes ingresar todos los campos"))
        self.__idProducto = idProducto
        self.__nombreProducto = nombreProducto
        self.__precio = precio
        self.__class__.productos.append(self)

    @property
    def idProducto(self):
        return self.__idProducto

    @idProducto.setter
    def idProducto(self, idProducto):
        self.__idProducto = idProducto 

    @property
    def nombreProducto(self):
        return self.__nombreProducto

    @nombreProducto.setter
    def nombreProducto(self, nombreProducto):
        self.__nombreProducto = nombreProducto 

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio 

    @classmethod
    def obtenerProductos(cls):
        return cls.productos

class Medicina(Producto):
    def __init__(self, idProducto, nombreProducto, precio, dosis, tipoAnimal):
        super().__init__(idProducto, nombreProducto, precio)
        self.__dosis = dosis
        self.__tipoAnimal = tipoAnimal

    @property
    def dosis(self):
        return self.__dosis

    @dosis.setter
    def dosis(self, dosis):
        self.__dosis = dosis 

    @property
    def tipoAnimal(self):
        return self.__tipoAnimal

    @tipoAnimal.setter
    def tipoAnimal(self, tipoAnimal):
        self.__tipoAnimal = tipoAnimal 

class ProductosControl(Producto):
    def __init__(self,idProducto, nombreProducto, precio, ica, frecuenciaAplicacion):
        super().__init__(idProducto, nombreProducto, precio)
        self.__ica = ica
        self.__frecuenciaAplicacion = frecuenciaAplicacion

    @property
    def ica(self):
        return self.__ica

    @ica.setter
    def ica(self, ica):
        self.__ica = ica 

    @property
    def frecuenciaAplicacion(self):
        return self.__frecuenciaAplicacion

    @frecuenciaAplicacion.setter
    def frecuenciaAplicacion(self, frecuenciaAplicacion):
        self.__frecuenciaAplicacion = frecuenciaAplicacion 

class ControlDePlagas(ProductosControl):
    def __init__(self,idProducto, nombreProducto, precio, ica, frecuenciaAplicacion, periodoCarencia):
        super().__init__(idProducto, nombreProducto, precio, ica, frecuenciaAplicacion)
        self.__periodoCarencia = periodoCarencia

    @property
    def periodoCarencia(self):
        return self.__periodoCarencia

    @periodoCarencia.setter
    def periodoCarencia(self, periodoCarencia):
        self.__periodoCarencia = periodoCarencia 

class ControlDeFertelizantes(ProductosControl):
    def __init__(self,idProducto, nombreProducto, precio, ica, frecuenciaAplicacion, ultimaAplicaion):
        super().__init__(idProducto, nombreProducto, precio, ica, frecuenciaAplicacion)
        self.__ultimaAplicaion = ultimaAplicaion

    @property
    def ultimaAplicaion(self):
        return self.__ultimaAplicaion

    @ultimaAplicaion.setter
    def ultimaAplicaion(self, ultimaAplicaion):
        self.__ultimaAplicaion = ultimaAplicaion 

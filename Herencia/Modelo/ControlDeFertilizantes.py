from ProductosDeControl import ProductosControl

class ControlDeFertilizantes(ProductosControl):
    def __init__(self,idProducto, nombreProducto, precio, ica, frecuenciaAplicacion, ultimaAplicaion):
        super().__init__(idProducto, nombreProducto, precio, ica, frecuenciaAplicacion)
        if idProducto == "" or nombreProducto =="" or precio=="" or ica=="" or frecuenciaAplicacion=="" or ultimaAplicaion=="":
            raise(TypeError("Debes ingresar todos los campos"))
        if not nombreProducto.isalpha():
            raise ValueError("El nombre del producto debe tener solo letras")
        try:
            int(idProducto)
            int(precio)
            int(ica)
        except ValueError:
            raise(ValueError("El dato debe contener solo numeros"))
        
        self.__ultimaAplicaion = ultimaAplicaion

    @property
    def ultimaAplicaion(self):
        return self.__ultimaAplicaion

    @ultimaAplicaion.setter
    def ultimaAplicaion(self, ultimaAplicaion):
        self.__ultimaAplicaion = ultimaAplicaion 

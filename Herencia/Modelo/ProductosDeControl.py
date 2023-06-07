class ProductosControl:
    def __init__(self,idProducto, nombreProducto, precio, ica, frecuenciaAplicacion):
        if idProducto == "" or nombreProducto =="" or precio=="" or ica=="" or frecuenciaAplicacion=="":
            raise(TypeError("Debes ingresar todos los campos"))
        if not nombreProducto.isalpha():
            raise ValueError("El nombre del producto debe tener solo letras")
        try:
            int(idProducto)
            int(precio)
            int(ica)
            int(frecuenciaAplicacion)
        except ValueError:
            raise(ValueError("El dato debe contener solo numeros"))
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
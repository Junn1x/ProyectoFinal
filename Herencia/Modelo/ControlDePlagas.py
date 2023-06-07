from ProductosDeControl import ProductosControl

class ControlDePlagas(ProductosControl):
    def __init__(self,idProducto, nombreProducto, precio, ica, frecuenciaAplicacion, periodoCarencia):
        super().__init__(idProducto, nombreProducto, precio, ica, frecuenciaAplicacion)
        if idProducto == "" or nombreProducto =="" or precio=="" or ica=="" or frecuenciaAplicacion=="" or periodoCarencia=="":
            raise(TypeError("Debes ingresar todos los campos"))
        if not nombreProducto.isalpha():
            raise ValueError("El nombre del producto debe tener solo letras")
        try:
            int(idProducto)
            int(precio)
            int(ica)
            int(frecuenciaAplicacion)
            int(periodoCarencia)
        except ValueError:
            raise(ValueError("El dato debe contener solo numeros"))
        self.__periodoCarencia = periodoCarencia

    @property
    def periodoCarencia(self):
        return self.__periodoCarencia

    @periodoCarencia.setter
    def periodoCarencia(self, periodoCarencia):
        self.__periodoCarencia = periodoCarencia 

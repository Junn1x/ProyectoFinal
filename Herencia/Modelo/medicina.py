class Medicina:
    def __init__(self, idProducto, nombreProducto, precio, dosis, tipoAnimal):
        if idProducto== "" or nombreProducto== "" or precio== "" or dosis== "" or tipoAnimal== "":
            raise(TypeError("Debes ingresar todos los campos"))
        if not nombreProducto.isalpha():
            raise ValueError("El nombre del producto debe tener solo letras")
        try:
            int(idProducto)
            int(precio)
            int(dosis)
        except ValueError:
            raise(ValueError("El dato debe contener solo numeros"))
        if not tipoAnimal.isalpha():
            raise ValueError("El tipo de animal solo debe tener letras")
        self.__dosis = dosis
        self.__tipoAnimal = tipoAnimal
        self.__idProducto = idProducto
        self.__nombreProducto = nombreProducto
        self.__precio = precio
    @property
    def dosis(self):
        return self.__dosis

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, precio):
        self.__precio = precio 

    @property
    def idProducto(self):
        return self.__idProducto
    
    @property
    def nombreProducto(self):
        return self.__nombreProducto
    
    @dosis.setter
    def dosis(self, dosis):
        self.__dosis = dosis 

    @property
    def tipoAnimal(self):
        return self.__tipoAnimal

    @tipoAnimal.setter
    def tipoAnimal(self, tipoAnimal):
        self.__tipoAnimal = tipoAnimal 
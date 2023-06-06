class Cliente:

    cuentaClientes = []
    def __init__(self, cedula, nombre, facturas):
        if cedula == "" or nombre =="":
            raise(TypeError("Debes ingresar todos los campos"))
        if not nombre.isalpha():
            raise ValueError("El nombre debe tener solo letras")
        try:
            int(cedula)
        except ValueError:
            raise(ValueError("La cedula solo debe contener numeros"))
        
        self.__cedula = cedula
        self.__nombre = nombre
        self.__facturas = facturas or []
        self.__class__.cuentaClientes.append(self)

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, cedula):
        self.__cedula = cedula 

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre 

    @property
    def facturas(self):
        return self.__facturas
    
    @classmethod
    def obtenerCuentas(cls):
        return cls.cuentaClientes
    
    @classmethod
    def agregar_factura(self, factura):
        self.__facturas.append(factura)

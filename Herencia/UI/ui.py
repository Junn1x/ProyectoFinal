from Modelo.claseClientes import Cliente
from Modelo.claseFacturas import Factura
from Modelo.medicina import Medicina
from Modelo.ControlDePlagas import ControlDePlagas
from Modelo.ControlDeFertilizantes import ControlDeFertilizantes

listaProductos = []
listaFacturas = []
listaClientes = []

def realizarVenta(fechaHoy):
    if len(listaProductos) != 0:
        respuesta = "S"
        clienteEncontrado = 0
        productosComprados = []
        
        while respuesta == "S" or len(productosComprados) == 0:
            resultadoProducto = buscarProducto()
            if resultadoProducto != 0:
                productosComprados.append(resultadoProducto)

            respuesta = input("¿Desea agregar otro producto (S/N)?")
            if len(productosComprados) == 0:
                print("Todavía no has agregado ningún producto!!!")

        facturaActual = Factura(productosComprados, fechaHoy, costoProductos(productosComprados))
        listaFacturas.append(facturaActual)

        respuesta = input("¿El cliente se encuentra registrado en el sistema? (S/N)")
        if(respuesta == "N"):
            agregarCliente(facturaActual)
        if(respuesta == "S"):
            while clienteEncontrado == 0:
                clienteEncontrado = adjuntarFactura(facturaActual)
                if clienteEncontrado == 0:
                    if input("El cliente no ha sido encontrado o no coincide ¿Desea agregar un cliente (S/N)?") == "S":
                        agregarCliente(facturaActual)
                        clienteEncontrado = 1
    else:
        print("NO HAY PRODUCTOS QUE VENDER")
    
def adjuntarFactura(facturaActual):
    idCliente = input("Introduzca el ID del cliente:")
    for cliente in listaClientes:
        if cliente.cedula == idCliente:
            cliente.agregar_factura(facturaActual)
            return 1
    return 0

def buscarProducto():
    devolver = 0
    idProducto = input("Ingrese el ID del producto")
    for producto in listaProductos:
        if producto.idProducto == int(idProducto):
            devolver = producto
    if devolver == 0:
        print("Producto no encontrado")    
    return devolver

def costoProductos(productosComprados):
    costoTotal = 0 
    for costoProducto in productosComprados:
        costoTotal += int(costoProducto.precio)
    return costoTotal

def agregarCliente(facturaActual):
    cedulaCliente = input("Indique la cédula del cliente: ")
    nombreCliente = input("Indique el nombre del cliente: ")
    cliente = Cliente(cedulaCliente, nombreCliente, [facturaActual])
    listaClientes.append(cliente)
    return cedulaCliente
    
def agregarProducto():
    producto = []
    precio = ""
    
    nombre = input("Indique el nombre del producto: ")
    while True:
        precio_str = input("Indique el precio del producto: ")
        try:
            precio = int(precio_str)
            break
        except ValueError:
            print("Precio debe ser un número entero!!!")
    
    tipo = input("¿Es Medicina o Producto de Control? (M / P)")
    if tipo == "M":
        dosis = input("Indique la dosis: ")
        tipoAnimal = input("Indique el tipo de animal al cual va dirigido: ")
        producto.append(Medicina((len(listaProductos)+1), nombre, precio, dosis, tipoAnimal))
        listaProductos.append(producto)
    if tipo == "P":
        ica = input("Indique el registro ICA: ")
        frecuencia = input("Indique la frecuencia de aplicación: ")
        tipoProductoControl = input("Indique si es Control para Plagas o Control para Fertilizantes (P / F): ")
        if tipoProductoControl == "P":
            periodoCarencia = input("Indique el Periodo de carencia: ")
            producto.append(ControlDePlagas((len(listaProductos)+1), nombre, precio, ica, frecuencia, periodoCarencia))
            listaProductos.append(producto)
        if tipoProductoControl == "F":
            ultimaAplicacion = input("Indique la última aplicación: ")
            producto.append(ControlDeFertilizantes((len(listaProductos)+1), nombre, precio, ica, frecuencia, ultimaAplicacion))
            listaProductos.append(producto)

    
    

def mostrarProductos():
    for producto in listaProductos:
        print("Producto con ID: " + str(producto.idProducto) + " con el nombre " + producto.nombreProducto + " y cuesta " + str(producto.precio) + ".")

def mostrarClientes():
    for cliente in listaClientes:
        print(cliente.nombre + " identificado con el número: " + cliente.cedula)
        for facturasCliente in cliente.facturas:
            for productosFacturaCliente in facturasCliente.productos:
                #print("Compró " + productosFacturaCliente.nombreProducto + " identificado con el numero " + productosFacturaCliente.idProducto + " al precio de " + productosFacturaCliente.precio + ".")
                print("Producto Id:"+ str(productosFacturaCliente.idProducto))
                print("Nombre:" + str(productosFacturaCliente.nombreProducto))
                print("Precio: " + str(productosFacturaCliente.precio))
            
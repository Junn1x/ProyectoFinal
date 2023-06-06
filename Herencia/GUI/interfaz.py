import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QLabel, QLineEdit, QGroupBox, QComboBox
from PyQt5.QtGui import QFont

path = os.path.abspath('controller/')
sys.path.append(path)

import controllerCliente
import controllerProductos
import controllerFacturas

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('La Granjita de Anuel')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: rgb(93, 158, 104);font-family: Verdana;font-size: 12px")

        widgetPrincipal = QWidget(self) 
        self.setCentralWidget(widgetPrincipal) 

        layout = QGridLayout(widgetPrincipal)

        #Caja superior
        textoCajaSuperior = QLabel('   La granjita de Anuel 🌿')
        textoCajaSuperior.setStyleSheet("background-color: rgb(167, 219, 176);font-size: 40px")
        fuenteCajaSuperior = QFont()
        fuenteCajaSuperior.setBold(True)
        textoCajaSuperior.setFont(fuenteCajaSuperior)
        layout.addWidget(textoCajaSuperior, 0, 0, 1, 2) 

        #Caja donde se representan las funciones
        pantallaOperaciones = QGroupBox()
        pantallaOperaciones.setStyleSheet("background-color: white;")
        layout.addWidget(pantallaOperaciones, 1, 1, 4, 1)
        layoutPantallaOperaciones = QGridLayout(pantallaOperaciones)
        pantallaOperaciones.setLayout(layoutPantallaOperaciones) 

        #Definicion de los Botones
        boton1 = QPushButton('Realizar venta')
        boton2 = QPushButton('Registrar producto')
        boton3 = QPushButton('Mostrar producto')
        boton4 = QPushButton('Mostrar clientes')

        boton1.clicked.connect(lambda: self.borrarWidgetsPrevios(layoutPantallaOperaciones, 0))
        boton2.clicked.connect(lambda: self.borrarWidgetsPrevios(layoutPantallaOperaciones, 1))
        boton3.clicked.connect(lambda: self.borrarWidgetsPrevios(layoutPantallaOperaciones, 2))
        boton4.clicked.connect(lambda: self.borrarWidgetsPrevios(layoutPantallaOperaciones, 3))

        listaBotones = [boton1, boton2, boton3, boton4]

        posicionVertical = 0
        for boton in listaBotones:
            boton.setFixedSize(200, 100)
            boton.setStyleSheet("background-color: white; color: black; font-family: Verdana; font-size: 20px;")
            layout.addWidget(boton, posicionVertical+1, 0)
            posicionVertical += 1
        
    def borrarWidgetsPrevios(self,layoutPantallaOperaciones, seleccion):
        while layoutPantallaOperaciones.count() > 0:
            item = layoutPantallaOperaciones.takeAt(0)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

        if seleccion == 0:
            self.realizarVenta(layoutPantallaOperaciones)
        if seleccion == 1:
            self.registrarProducto(layoutPantallaOperaciones)
        if seleccion == 2:
            self.mostrarProducto(layoutPantallaOperaciones)
        if seleccion == 3:
            self.mostrarClientes(layoutPantallaOperaciones)
        if seleccion == 4:
            self.crearNuevoCliente(layoutPantallaOperaciones)
            
    def realizarVenta(self, layoutPantallaOperaciones):
        fechaHoy = ("06/06/23")

        clienteNombreTexto = QLabel("Id Cliente:")
        clientesLista = QComboBox()
        listaClientes = controllerCliente.obtener_clientes()
        #LISTA CLIENTES--------------------------------------------------------------------------------------------------------------
        for cliente in listaClientes:
            clientesLista.addItem(str(cliente))
        layoutPantallaOperaciones.addWidget(clienteNombreTexto, 0, 0)
        layoutPantallaOperaciones.addWidget(clientesLista, 0, 1)
        clientesLista.setObjectName("clientesLista")

        crearClienteBoton = QPushButton('Crear Cliente + ')
        crearClienteBoton.setFixedSize(120, 30)
        crearClienteBoton.setStyleSheet("background-color: black; color: white; font-family: Verdana; font-size: 15px;")
        layoutPantallaOperaciones.addWidget(crearClienteBoton, 0, 2) 

        crearClienteBoton.clicked.connect(lambda: self.borrarWidgetsPrevios(layoutPantallaOperaciones, 4))

        productoTexto = QLabel("Seleccione producto:")
        productoLista = QComboBox()

        #AGREGAR LISTA PRODUCTOS CONTROL Y LISTA MEDICINAS----------------------------------------------------------------
        listaProductos = controllerProductos.obtener_productos()
        
        if len(listaProductos) != 0:
            for producto in listaProductos:
                productoLista.addItem(str(producto))
        productoLista.setObjectName("productoDeLista")

        layoutPantallaOperaciones.addWidget(productoTexto, 2, 0)
        layoutPantallaOperaciones.addWidget(productoLista, 2, 1)

        guardarProductoBoton = QPushButton('Guardar Producto + ')
        guardarProductoBoton.setFixedSize(550, 30)
        guardarProductoBoton.setStyleSheet("background-color: black; color: white; font-family: Verdana; font-size: 15px;")
        layoutPantallaOperaciones.addWidget(guardarProductoBoton, 3, 0, 1, 3)

        global facturaProductosCliente 
        facturaProductosCliente = [] #Esta es la que se une a clientes-------------------------------------------------------
        
        guardarProductoBoton.clicked.connect(lambda: self.pulsado(listaProductos))
        resultado = 0
        productoAgregar = ""
        if resultado == 1:
            print()
            datoNombreProducto = self.findChild(QLineEdit, "productoDeLista").text()
            if len(listaProductos) != 0:
                for producto in listaProductos:
                    if producto == datoNombreProducto:
                        productoAgregar = producto
            resultado = 0

            facturaProductosCliente.append(productoAgregar)

        if len(facturaProductosCliente) != 0:
            for productosIndividuales in facturaProductosCliente:
                productoIDTexto = QLabel(str(productosIndividuales.ID))
                productoNombreTexto = QLabel(str(productosIndividuales.nombre))
                productoPrecioTexto = QLabel(str(productosIndividuales.precio))
                
                cantidadProductos += 1

                layoutPantallaOperaciones.addWidget(productoIDTexto, 4, cantidadProductos)
                layoutPantallaOperaciones.addWidget(productoNombreTexto, 4, cantidadProductos+1)
                layoutPantallaOperaciones.addWidget(productoPrecioTexto, 4, cantidadProductos+2)

                costoTotal += productosIndividuales.precio            

        #AQUI DEFINES FACTURA A PARTIR DE --------------------------------------------------------------------------------------
        #facturaProductosCliente
        #fechaHoy
        #costoTotal     
        # con este crear factura
        print("lista de productos: " , facturaProductosCliente)
        productosDic = controllerProductos.productos_objeto(facturaProductosCliente)
        facturaActual = controllerFacturas.crear_factura(productosDic)

        guardarClienteConFactura = QPushButton('Guardar Factura + ')
        guardarClienteConFactura.setFixedSize(550, 30)
        guardarClienteConFactura.setStyleSheet("background-color: black; color: white; font-family: Verdana; font-size: 15px;")
        layoutPantallaOperaciones.addWidget(guardarClienteConFactura, 5, 0, 1, 3)

        if len(facturaProductosCliente) != 0:
            guardarClienteConFactura.clicked.connect(lambda: self.guardarClienteConFactura(listaClientes, facturaActual['nueva_factura']))
        else:
            textoIDCliente = QLabel("Todavía no hay ninguna factura...")
            layoutPantallaOperaciones.addWidget(textoIDCliente, 6, 0)

    def pulsado(self, listaProductos):
        datoNombreProducto = self.findChild(QLineEdit, "productoDeLista").text()
        if len(listaProductos) != 0:
            for producto in listaProductos:
                if producto == datoNombreProducto:
                    productoAgregar = producto

            facturaProductosCliente.append(productoAgregar)  

    def crearNuevoCliente(self, layoutPantallaOperaciones):
        textoIDCliente = QLabel("Ingrese ID cliente:")
        inputIDCliente = QLineEdit()
        inputIDCliente.setObjectName("idCliente")
        layoutPantallaOperaciones.addWidget(textoIDCliente, 0, 0)
        layoutPantallaOperaciones.addWidget(inputIDCliente, 0, 1)

        textoNombreCliente = QLabel("Ingrese nombre cliente:")
        inputNombreCliente = QLineEdit()
        
        
        inputNombreCliente.setObjectName("nombreCliente")
        layoutPantallaOperaciones.addWidget(textoNombreCliente, 1, 0)
        layoutPantallaOperaciones.addWidget(inputNombreCliente, 1, 1)
        
        guardarNuevoClienteBoton = QPushButton('Guardar nuevo cliente ')
        guardarNuevoClienteBoton.setFixedSize(550, 30)
        guardarNuevoClienteBoton.setStyleSheet("background-color: black; color: white; font-family: Verdana; font-size: 15px;")
        layoutPantallaOperaciones.addWidget(guardarNuevoClienteBoton, 2, 0, 1, 2)

        guardarNuevoClienteBoton.clicked.connect(lambda: self.almacenarInformacionNuevoCliente(layoutPantallaOperaciones))
        
    def almacenarInformacionNuevoCliente(self, layoutPantallaOperaciones):
        datoIDCliente = self.findChild(QLineEdit, "idCliente").text()
        datoNombreCliente = self.findChild(QLineEdit, "nombreCliente").text()

        if datoIDCliente and datoNombreCliente:
            print()
            datos = {'nombre': datoNombreCliente , 'id': datoIDCliente , 'facturas': []}
            respuesta = controllerCliente.crear_cliente(datos)
            print('respuesta: ' , respuesta)
            #AQUI CONECTAS LA CLASE CLIENTE ---------------------------------------------------------------------
            #LO AÑADES A LA LISTA PARA QUE APAREZCA COMO OPCIÓN ------------------
            self.borrarWidgetsPrevios(layoutPantallaOperaciones, 0)

        
    def guardarClienteConFactura(self, listaClientes, facturaActual):
        nombreClienteSeleccionado = self.findChild(QLineEdit, "clientesLista").text()
        for clienteEncontrado in listaClientes:
            if clienteEncontrado == nombreClienteSeleccionado:
                cliente = controllerCliente.buscar_cliente(clienteEncontrado)
                factura_respuesta = controllerCliente.agregar_factura(cliente, facturaActual)

    def registrarProducto(self, layoutPantallaOperaciones):
        # Agregar QLineEdits al QGridLayout dentro de pantallaOperaciones
        textoNombreProducto = QLabel("Nombre:")
        inputNombreProducto = QLineEdit()
        inputNombreProducto.setObjectName("nombreProducto")
        layoutPantallaOperaciones.addWidget(textoNombreProducto, 0, 0)
        layoutPantallaOperaciones.addWidget(inputNombreProducto, 0, 1)

        textoPrecioProducto = QLabel("Precio:")
        inputPrecioProducto = QLineEdit()
        inputPrecioProducto.setObjectName("precioProducto")
        layoutPantallaOperaciones.addWidget(textoPrecioProducto, 1, 0) 
        layoutPantallaOperaciones.addWidget(inputPrecioProducto, 1, 1)

        textoidProducto = QLabel("id:")
        inputidProducto = QLineEdit()
        inputidProducto.setObjectName("idProducto")
        layoutPantallaOperaciones.addWidget(textoidProducto, 2, 0) 
        layoutPantallaOperaciones.addWidget(inputidProducto, 2, 1)

        tipoProductoTexto = QLabel("Tipo de Producto: ")
        layoutPantallaOperaciones.addWidget(tipoProductoTexto, 3, 0)
        tipoProductoLista = QComboBox()
        tipoProductoLista.addItem("Selecciona el tipo de Producto")
        tipoProductoLista.addItem("Medicina")
        tipoProductoLista.addItem("Producto de Control")
        tipoProductoLista.setObjectName("tipoProducto")
        layoutPantallaOperaciones.addWidget(tipoProductoLista, 3, 1)

        botonGuardar = QPushButton('Guardar')
        botonGuardar.setFixedSize(550, 30)
        botonGuardar.setStyleSheet("background-color: black; color: White; font-family: Verdana; font-size: 20px;")
        layoutPantallaOperaciones.addWidget(botonGuardar, 8, 0, 1, 2)

        tipoProductoLista.currentIndexChanged.connect(lambda: self.manejarTipoProducto(tipoProductoLista, layoutPantallaOperaciones, botonGuardar))      

    def manejarTipoProducto(self, tipoProductoLista, layoutPantallaOperaciones, botonGuardar):
        seleccion = tipoProductoLista.currentText()  # Obtener la opción seleccionada
        if seleccion == "Medicina":
            dosisTexto = QLabel("Dosis:")
            dosisInput = QLineEdit()
            dosisInput.setObjectName("dosisMedicina")
            layoutPantallaOperaciones.addWidget(dosisTexto, 3, 0)
            layoutPantallaOperaciones.addWidget(dosisInput, 3, 1)

            tipoAnimalTexto = QLabel("tipoAnimal:")
            tipoAnimalInput = QLineEdit()
            tipoAnimalInput.setObjectName("tipoAnimalMedicina")
            layoutPantallaOperaciones.addWidget(tipoAnimalTexto, 4, 0)
            layoutPantallaOperaciones.addWidget(tipoAnimalInput, 4, 1)

            botonGuardar.clicked.connect(lambda: self.guardarProductos(0))

        elif seleccion == "Producto de Control":
            registroICATexto = QLabel("Registro ICA:")
            registroICAInput = QLineEdit()
            registroICAInput.setObjectName("registroICAPc")
            layoutPantallaOperaciones.addWidget(registroICATexto, 3, 0)
            layoutPantallaOperaciones.addWidget(registroICAInput, 3, 1)

            frecuenciaAplicacionTexto = QLabel("Frecuencia Aplicacion:")
            frecuenciaAplicacionInput = QLineEdit()
            frecuenciaAplicacionInput.setObjectName("frecuenciaAplicacionICAPc")
            layoutPantallaOperaciones.addWidget(frecuenciaAplicacionTexto, 4, 0)
            layoutPantallaOperaciones.addWidget(frecuenciaAplicacionInput, 4, 1)

            tipoProductoControlTexto = QLabel("Tipo de Producto de control: ")
            layoutPantallaOperaciones.addWidget(tipoProductoControlTexto, 5, 0)

            tipoProductoControl = QComboBox()
            tipoProductoControl.addItem("Selecciona el tipo de Producto de Control")
            tipoProductoControl.addItem("Control para Plagas")
            tipoProductoControl.addItem("Control para Fertilizante")
            tipoProductoControl.setObjectName("tipoProductoPC")
            layoutPantallaOperaciones.addWidget(tipoProductoControl, 5, 1)
            
            tipoProductoControl.currentIndexChanged.connect(lambda: self.manejarTipoProductoControl(tipoProductoControl, layoutPantallaOperaciones, botonGuardar))

    def manejarTipoProductoControl(self, tipoProductoControl, layoutPantallaOperaciones, botonGuardar):
        seleccion = tipoProductoControl.currentText()  # Obtener la opción seleccionada
        if seleccion == "Control para Plagas":
            periodoCarenciaTexto = QLabel("Periodo Carencia:")
            periodoCarenciaInput = QLineEdit()
            periodoCarenciaInput.setObjectName("periodoCarenciaCP")
            layoutPantallaOperaciones.addWidget(periodoCarenciaTexto, 6, 0)
            layoutPantallaOperaciones.addWidget(periodoCarenciaInput, 6, 1)

            botonGuardar.clicked.connect(lambda: self.guardarProductos(1))

        elif seleccion == "Control para Fertilizante":
            ultimaAplicacionTexto = QLabel("Ultima Aplicacion:")
            ultimaAplicacionInput = QLineEdit()
            ultimaAplicacionInput.setObjectName("ultimaAplicacionCF")
            layoutPantallaOperaciones.addWidget(ultimaAplicacionTexto, 6, 0)
            layoutPantallaOperaciones.addWidget(ultimaAplicacionInput, 6, 1)

            botonGuardar.clicked.connect(lambda: self.guardarProductos(2))

    def guardarProductos(self, tipo):
        nombre = self.findChild(QLineEdit, "nombreProducto").text()
        precio = self.findChild(QLineEdit, "precioProducto").text()
        id_producto = self.findChild(QLineEdit, "idProducto").text()
        if tipo == 0:
            dosis = self.findChild(QLineEdit, "dosisMedicina").text()
            tipoAnimal = self.findChild(QLineEdit, "tipoAnimalMedicina").text()
            datos = {'tipo': 0 , 'id_producto': id_producto,'nombre_producto': nombre ,'precio': precio  , 'dosis': dosis,'tipo_animal':tipoAnimal}
            respuesta = controllerProductos.crear_producto(datos)
            print(respuesta)
            #AQUÍ CONECTAS CON LA CLASE MEDICINA-------------------------------------------------------------------------------------------
        if tipo == 1 or tipo == 2:
            registroICA = self.findChild(QLineEdit, "registroICAPc").text()
            frecuenciaAplicacion = self.findChild(QLineEdit, "frecuenciaAplicacionICAPc").text()
            if tipo == 1:
                periodoCarencia = self.findChild(QLineEdit, "periodoCarenciaCP").text()
                datos = {'tipo': 2 ,'id_producto': id_producto,'nombre_producto': nombre ,'precio': precio  , 'ica': registroICA,'frecuencia_aplicacion':frecuenciaAplicacion,'periodo_carencia':periodoCarencia}
                respuesta = controllerProductos.crear_producto(datos)
                print(respuesta)
                #AQUÍ CONECTAS CON LA CLASE CONTROL PLAGAS-------------------------------------------------------------------------------------------
            if tipo == 2:
                ultimaAplicacion = self.findChild(QLineEdit, "ultimaAplicacionCF").text()
                datos = {'tipo': 1 ,'id_producto': id_producto,'nombre_producto': nombre ,'precio': precio  , 'ica': registroICA,'frecuencia_aplicacion':frecuenciaAplicacion,'ultima_aplicacion':ultimaAplicacion}
                respuesta = controllerProductos.crear_producto(datos)
                print(respuesta)
                #AQUÍ CONECTAS CON LA CLASE CONTROL FERTILIZANTES-------------------------------------------------------------------------------------------

    def mostrarProducto(self, layoutPantallaOperaciones):
        idProductoTexto = QLabel("ID producto:")
        idProductoInput = QLineEdit()
        idProductoInput.setObjectName("IDproducto")
        layoutPantallaOperaciones.addWidget(idProductoTexto, 0, 0)
        layoutPantallaOperaciones.addWidget(idProductoInput, 0, 1)

        datoIDProducto = self.findChild(QLineEdit, "IDproducto").text() 

        #ESTE DATO ID PRODUCTO BUSCARLO EN LA LISTA DE MEDICINAS Y EN LA LISTA DE PRODUCTOS CONTROL ----------------------------------------------
        nombreProducto = 0
        costoProducto = 0

        nombreProductoMostrar = QLabel(str(nombreProducto))
        costoProductoMostrar = QLabel(str(costoProducto))
        layoutPantallaOperaciones.addWidget(nombreProductoMostrar, 1, 0)
        layoutPantallaOperaciones.addWidget(costoProductoMostrar, 1, 1)

    def mostrarClientes(self, layoutPantallaOperaciones):
        idClienteTexto = QLabel("ID Cliente:")
        idClienteInput = QLineEdit()
        idClienteInput.setObjectName("IDCliente")
        layoutPantallaOperaciones.addWidget(idClienteTexto, 0, 0)
        layoutPantallaOperaciones.addWidget(idClienteInput, 0, 1)

        datoIDProducto = self.findChild(QLineEdit, "IDCliente").text()

        #ESTE DATO ID CLIENTE BUSCARLO EN LA LISTA DE CLIENTES ------------------------------------------------------------

        idCliente = 0
        nombreCliente = 0

        idClienteoMostrar = QLabel(str(idCliente))
        nombreClienteMostrar = QLabel(str(nombreCliente))
        layoutPantallaOperaciones.addWidget(idClienteoMostrar, 1, 0)
        layoutPantallaOperaciones.addWidget(nombreClienteMostrar, 1, 1)

        factura = 0
        producto = 0
        #AQUI TRAES LA CLASE CLIENTE ------------------------------------------------------------------------------------------------------------------
        x = 2
        listaFacturas = []
        for factura in listaFacturas:
            for producto in factura:
                idProductoMostrar = QLabel(str(producto.id))
                nombreProductoMostrar = QLabel(str(producto.nombre))
                precioProductoMostrar = QLabel(str(producto.precio))
                layoutPantallaOperaciones.addWidget(idProductoMostrar, x, 0)
                layoutPantallaOperaciones.addWidget(nombreProductoMostrar, x, 1)
                layoutPantallaOperaciones.addWidget(precioProductoMostrar, x, 2)
                x += 1

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
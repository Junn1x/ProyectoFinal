from UI.ui import agregarProducto
from UI.ui import realizarVenta
from UI.ui import mostrarProductos
from UI.ui import mostrarClientes

def menu(opcion):
    
    while opcion != "5":
        print("1. Realizar venta")
        print("2. Registrar producto")
        print("3. Mostrar productos")
        print("4. Mostrar Clientes")
        print("5. Salir")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            realizarVenta("30/04/23")
        elif opcion == "2":
            agregarProducto()
        elif opcion == "3":
            mostrarProductos()
        elif opcion == "4":
            mostrarClientes()
        else:
            print("Opcion invalida, ingrese una opcion valida.")
    print("Gracias por usar nuestro sistema")

menu(0)
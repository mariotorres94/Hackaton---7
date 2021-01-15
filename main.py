from controller.cliente_controller import Cliente_Controller
from controller.producto_controller import Producto_Controller
from controller.order_controller import Orden_Controller
from controller.detalle_orden_controller import Detalle_Orden_Controller

cliente = Cliente_Controller()
producto = Producto_Controller()
orden = Orden_Controller()
detalle = Detalle_Orden_Controller()

while True:
    try:
        print("\n********************************")
        print("*        MENU PRINCIPAL        *")
        print("********************************")
        print("""
            1. CLIENTE
            2. PRODUCTO
            3. ORDEN
            4. SALIR
        """)
        opcion = int(input("Seleccione una opcion: "))
        
        if opcion == 1:
            cliente.menu_cliente()
        elif opcion == 2:
            producto.menu_producto()
        elif opcion == 3:
            orden.menu_orden()
        elif opcion == 4:
            print("Hasta Luego")
            exit()
        else:
            print("No se encuentra opcion elegida, Intente nuevamente ....")
    except Exception:
        print("No puede ingresar STRING en un dato entero, Intente de nuevo....")

from models.orden import Orden
from models.producto import Producto
from models.detalle_orden import Detalle_Orden
from controller.detalle_orden_controller import Detalle_Orden_Controller
import datetime

class Orden_Controller(Detalle_Orden):
    def __init__(self):
        self.orden = Orden()
        self.producto = Producto()
        self.detalle_orden = Detalle_Orden()
        self.detalle_orden_controller = Detalle_Orden_Controller()
        self.close = False

    def menu_orden(self):
        while True:
            try:
                print("\n******************************")
                print("*          MENU ORDEN          *")
                print("********************************")
                print("""
                    1. CREAR ORDEN
                    2. LEER ORDEN
                    3. LEER TODAS LAS ORDENES
                    4. LEER ORDENES POR FECHAS
                    5. LEER ORDENES DE UN CLIENTE
                    6. ACTUALIZAR STATUS DE UNA ORDEN 
                    7. AGREGAR PRODUCTOS A UNA ORDEN
                    8. MODIFICAR PRODUCTOS DE UNA ORDEN
                    9. BORRAR PRODUCTOS DE UNA ORDEN
                    10. BORRAR ORDEN
                    11. SALIR
                """)
                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.create_a_order()
                elif opcion == 2:
                    self.read_a_order()
                elif opcion == 3:
                    self.read_all_orders()
                elif opcion == 4:
                    fecha = input("Ingrese fecha de busqueda: ")
                    self.orden.fecha = fecha
                    print(f"\n-----                DATOS DE LA FECHA {fecha}                -----")
                    print("----------------------------------------------------------------------")
                    self.read_orders_for_date()
                elif opcion == 5:
                    id_cliente = int(input("Ingrese ID de cliente: "))
                    self.orden.id_cliente = id_cliente
                    self.read_orders_of_a_client()
                elif opcion == 6:
                    id_orden = int(input("Ingrese ID de orden para actualizar status: "))
                    self.orden.id_orden = id_orden
                    while True:
                        print("""
                            EN QUE ESTADO SE ENCUENTRA LA ORDEN
                            - PROCESSING
                            - ACCEPTED
                            - SEND
                            - RECEIVED
                        """)
                        status = (input("Igrese estado de la orden: ")).upper()
                        if status == 'PROCESSING':
                            self.orden.status = status
                            self.orden.update_data_of_a_order()
                            break
                        elif status == 'ACCEPTED':
                            self.orden.status = status
                            self.orden.update_data_of_a_order()
                            break
                        elif status == 'SEND':
                            self.orden.status = status
                            self.orden.update_data_of_a_order()
                            break
                        elif status == 'RECEIVED':
                            self.orden.status = status
                            self.orden.update_data_of_a_order()
                            break
                        else:
                            print("Estado no se encuentra, Intente de nuevo")
                elif opcion == 7:
                    pass
                elif opcion == 8:
                    pass
                elif opcion == 9:
                    pass
                elif opcion == 10:
                    self.delete_orden()
                elif opcion == 11:
                    self.close = True
                    return True
                else:
                    print("No se encuentra opcion elegida, Intente nuevamente ....")
            except Exception:
                print("Dato ingresado no es correcto, Intente de nuevo ...")

    def read_products(self):
        productos = self.producto.read_products()

        if productos:
            print("\n")
            print("\nID PRODUCTO      NOMBRE PRODUCTO     MARCA           DESCRIPCION         PRECIO")
            print("-------------------------------------------------------------------------------")
            for i in productos:
                print(f"{i[0]}\t         {i[1].ljust(20)}{i[2].ljust(16)}{i[3].ljust(20)}{i[4]}")

    def read_a_order(self):
        ordenes = self.orden.read_a_order()

        if ordenes:
            print("ID ORDEN      ID CLIENTE     STATUS           FECHA             TOTAL")
            print("----------------------------------------------------------------------")
            for i in ordenes:
                print(f"{i[0]}\t      {i[1]}\t             {i[2].ljust(17)}{i[3]}\t{i[4]}")

    def read_all_orders(self):
        ordenes = self.orden.read_all_orders()

        if ordenes:
            print("ID ORDEN      ID CLIENTE     STATUS           FECHA             TOTAL")
            print("----------------------------------------------------------------------")
            for i in ordenes:
                print(f"{i[0]}\t      {i[1]}\t             {i[2].ljust(17)}{i[3]}\t{i[4]}")

    def read_orders_for_date(self):
        ordenes = self.orden.read_orders_for_date()

        if ordenes:
            print("ID ORDEN      ID CLIENTE     STATUS           FECHA             TOTAL")
            print("----------------------------------------------------------------------")
            for i in ordenes:
                print(f"{i[0]}\t      {i[1]}\t             {i[2].ljust(17)}{i[3]}\t{i[4]}")

    def read_orders_of_a_client(self):
        ordenes_clientes = self.orden.read_orders_of_a_client()

        if ordenes_clientes:
            print("ID ORDEN      ID CLIENTE     NOMBRES           APELLIDO PAT         APELLIDO MAT         DIRECCION           CELULAR         STATUS          FECHA           TOTAL")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            for i in ordenes_clientes:
                print(f"{i[0]}\t      {i[1]}\t             {i[2].ljust(18)}{i[3].ljust(21)}{i[4].ljust(21)}{i[5].ljust(20)}{i[6].ljust(16)}{i[7].ljust(16)}{i[8]}\t     {i[9]}")

    def read_details_order(self):
        orden_detalle = self.orden.read_details_order()

        if orden_detalle:
            print("ID ORDEN         ID CLIENTE      ID PRODUCTO      CANTIDAD PRODUCTO       STATUS         FECHA       TOTAL")
            print("----------------------------------------------------------------------------------------------------------")
            for i in orden_detalle:
                print(f"{i[0]}{i[1]}{i[2]}{i[3]}{i[4]}{i[5]}{i[6]}")

    def create_a_order(self):
        productos = self.producto.read_products()        
        id_cliente = int(input("Ingrese ID de cliente: "))
        status = 'PROCESSING'
        fecha = datetime.datetime.now()
        total = 0.0

        self.orden.id_cliente = id_cliente
        self.orden.status = status
        self.orden.fecha = fecha
        self.orden.total = total

        self.read_products()
        id_orden = self.orden.create_a_order()
        self.detalle_orden_controller.id_orden = id_orden
    
        if type(id_orden) == int:
            id_producto = ' '
            while id_producto != '':
                id_producto = int(input("Elija producto por su ID: "))
                self.detalle_orden.id_producto = id_producto
                for i in productos:
                    if i[0] == id_producto:
                        precio = i[4]
                cantidad_producto = int(input("Ingrese cantidad: "))
                self.detalle_orden.cantidad_producto = cantidad_producto

                precio_cantidad = precio * cantidad_producto
                total_producto = precio_cantidad 
                total += total_producto
                self.orden.total = total
                self.detalle_orden.total_producto = total_producto
                
                respuesta = input("Seguira ingresando mas productos? Y/N:")
                if respuesta == 'Y' or respuesta == 'y':
                    self.read_products()
                    self.orden.update_a_order()
                    self.detalle_orden_controller.create_detail_order(id_orden,id_producto,cantidad_producto,total_producto,total)
                    pass
                elif respuesta == 'N' or respuesta == 'n':
                    self.detalle_orden_controller.create_detail_order(id_orden,id_producto,cantidad_producto,total_producto,total)
                    self.orden.update_a_order()
                    "self.detalle_orden.create_a_details_order()"
                    "self.detalle_orden.update_a_details_order()"
                    break 
        else:
            print("No se pudo crear orden. Revisa.")
    
    def delete_orden(self):
        while True:
            try:

                id_orden = int(input("Ingrese ID de orden a borrar: "))
                self.orden.id_orden = id_orden

                if id_orden > 0:
                    respuesta = input(f"Esta seguro de borrar la orden {id_orden}? Y/N: ")
                    if respuesta == 'Y' or respuesta == 'y':
                        self.orden.delete_a_orden()
                        break
                    elif respuesta == 'N' or respuesta == 'n':
                        self.menu_orden()
                        break
                    else:
                        print("Opcion digitada no es correcta, Intente de nuevo...")
                else:
                    print("ID orden no puede ser negativo, Intente de nuevo...")
            except Exception:
                print("No puede ingresar STRING en un dato entero, Intente de nuevo...")

                

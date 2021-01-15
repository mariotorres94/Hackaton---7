from models.detalle_orden import Detalle_Orden
from models.producto import Producto
from models.orden import Orden

class Detalle_Orden_Controller(Orden):
    def __init__(self):
        self.detalle_orden = Detalle_Orden()
        self.producto = Producto()
        self.orden = Orden()
        self.close = False

    def read_products(self):
        productos = self.producto.read_products()

        if productos:
            print("ID PRODUCTO      NOMBRE PRODUCTO     MARCA           DESCRIPCION         PRECIO")
            print("-------------------------------------------------------------------------------")
            for i in productos:
                print(f"{i[0]}\t         {i[1].ljust(20)}{i[2].ljust(16)}{i[3].ljust(20)}{i[4]}")

    
    def detail_order(self,id_orden,id_producto,cantidad_producto,total_producto,total):
        detail_order = self.detalle_orden.read_detail_order()

        if detail_order:
            print("\n")
            print("\nID ORDEN         ID PRODUCTO         ID CLIENTE      CANT. PRODUCTO      TOTAL POR PRODUCTO      STATUS           FECHA         TOTAL")
            print("---------------------------------------------------------------------------------------------------------------------------------------")
            for i in detail_order:
                print(f"{i[0]}\t         {i[1]}\t             {i[2]}\t             {i[3]}\t                  {i[4]}\t                 {i[5]}\t   {i[6]}\t{i[4]}")
            print("---------------------------------------------------------------------------------------------------------------------------------------")
            print("TOTAL PAGAR:                                                                                                                   ",total)

    def create_detail_order(self,id_orden,id_producto,cantidad_producto,total_producto,total):
        self.detalle_orden.id_orden = id_orden
        self.detalle_orden.id_producto = id_producto
        self.detalle_orden.cantidad_producto = cantidad_producto
        self.detalle_orden.total_producto = total_producto

        self.detalle_orden.create_a_details_order()
        self.detail_order(id_orden,id_producto,cantidad_producto,total_producto,total)
        """productos = self.producto.read_products()
        print(id_orden)
        self.detalle_orden.id_orden = id_orden
        total_producto = 0.0
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

                self.detalle_orden.total_producto = total_producto
                
                respuesta = input("Seguira ingresando mas productos? Y/N:")
                if respuesta == 'Y' or respuesta == 'y':
                    self.detalle_orden.create_a_details_order()
                    pass
                elif respuesta == 'N' or respuesta == 'n':
                    self.detalle_orden.create_a_details_order()
                    self.detail_order(total)
                    "self.detalle_orden.update_a_details_order()"
                    break 
        else:
            print("No se pudo crear orden. Revisa.")
"""
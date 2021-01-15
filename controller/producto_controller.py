from models.producto import Producto

class Producto_Controller:
    def __init__(self):
        self.producto = Producto()
        self.close = False

    def menu_producto(self):
        while True:
            try:
                print("\n******************************")
                print("*          MENU PRODUCTO       *")
                print("********************************")
                print("""
                    1. CREAR PRODUCTO
                    2. LEER TODOS LOS PRODUCTOS
                    3. LEER PRODUCTO
                    4. LEER PRODUCTO POR MARCA
                    5. LEER PRODUCTOS POR UN RANGO DE PRECIO
                    6. ACTUALIZAR CLIENTE
                    7. ELIMINAR CLIENTE
                    8. SALIR
                """)
                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.create_a_product()
                elif opcion == 2:
                    self.read_products()
                elif opcion == 3:
                    id_producto = int(input("Ingrese ID de producto a buscar: "))
                    self.producto.id_producto = id_producto
                    self.read_a_product()
                elif opcion == 4:
                    marca = input("Ingrese marca: ")
                    self.producto.marca = marca
                    self.read_a_product_for_brand()
                elif opcion == 5:
                    precio = float(input("Ingrese precio Inferior: "))
                    self.producto.precio = precio
                    precio = float(input("Ingrese precio Superior: "))
                    self.producto.precio = precio
                    self.read_a_product_for_price(precio)
                elif opcion == 6:
                    self.update_a_product()
                elif opcion == 7:
                    self.delete_a_product()
                elif opcion == 8:
                    self.close = True
                    return True
                else:
                    print("No se encuentra opcion elegida, Intente nuevamente ....")
            except Exception:
                print("Dato ingresado no es correcto, Intente de nuevo ...")

    def read_a_product(self, id_producto=''):
        productos = self.producto.read_a_product(id_producto)

        if productos:
            print("ID PRODUCTO      NOMBRE PRODUCTO     MARCA           DESCRIPCION         PRECIO")
            print("-------------------------------------------------------------------------------")
            for i in productos:
                print(f"{i[0]}\t         {i[1].ljust(20)}{i[2].ljust(16)}{i[3].ljust(20)}{i[4]}")
    
    def read_a_product_for_brand(self):
        productos = self.producto.read_a_product_for_brand()

        if productos:
            print("ID PRODUCTO      NOMBRE PRODUCTO     MARCA           DESCRIPCION         PRECIO")
            print("-------------------------------------------------------------------------------")
            for i in productos:
                print(f"{i[0]}\t         {i[1].ljust(20)}{i[2].ljust(16)}{i[3].ljust(20)}{i[4]}")

    def read_a_product_for_price(self, precio=''):
        productos = self.producto.read_a_product_for_price(precio)

        if productos:
            print("ID PRODUCTO      NOMBRE PRODUCTO     MARCA           DESCRIPCION         PRECIO")
            print("-------------------------------------------------------------------------------")
            for i in productos:
                print(f"{i[0]}\t         {i[1].ljust(20)}{i[2].ljust(16)}{i[3].ljust(20)}{i[4]}")

    def read_products(self):
        productos = self.producto.read_products()

        if productos:
            print("ID PRODUCTO      NOMBRE PRODUCTO     MARCA           DESCRIPCION         PRECIO")
            print("-------------------------------------------------------------------------------")
            for i in productos:
                print(f"{i[0]}\t         {i[1].ljust(20)}{i[2].ljust(16)}{i[3].ljust(20)}{i[4]}")

    def create_a_product(self):
        print("\nREGISTRO DE PRODUCTO")
        print("----------------------")
        nombre_producto = input("Ingrese nombre de producto: ")
        marca = input("Ingrese marca: ")
        descripcion = input(f"Ingrese descripcion de {nombre_producto}: ")
        precio = float(input("Ingrese precio: "))

        self.producto.nombre_producto = nombre_producto
        self.producto.marca = marca
        self.producto.descripcion = descripcion
        self.producto.precio = precio

        self.producto.create_a_product()

    def update_a_product(self):
        id_producto = int(input("Ingrese ID de cliente a buscar: "))
        self.producto.id_producto = id_producto
        productos = self.producto.read_a_product(id_producto)
        for i in productos:
            if id_producto == i[0]:
                nombre_producto = i[1]
                self.read_a_product()

        print(f"\nACTUALIZAR DATOS DE {nombre_producto.upper()}")
        print("------------------------------------")
        print("""
            1. Nombre 
            2. Marca
            3. Descripcion
            4. Precio
            5. Regresar
        """)
        opcion = int(input("Elija dato que actualizara: "))

        if opcion == 1:
            respuesta = input(f"Esta seguro de actualizar nombre? Y/N: ")
            if respuesta == 'Y' or respuesta == 'y':
                nombre_producto = input("Ingrese el nombre actualizado: ")
                self.producto.nombre_producto = nombre_producto
                for i in self.producto.read_a_product(id_producto):
                    if i[0] == id_producto:
                        id_producto = i[0]
                        self.producto.id_producto = id_producto
                        marca = i[2]
                        self.producto.marca = marca
                        descripcion = i[3]
                        self.producto.descripcion = descripcion
                        precio = i[4]
                        self.producto.precio = precio
            elif respuesta == 'N' or respuesta == 'n':
                for i in self.producto.read_a_product(id_producto):
                    if i[0] == id_producto:
                        id_producto = i[0]
                        self.producto.id_producto = id_producto
                        nombre_producto = i[1]
                        self.producto.nombre_producto = nombre_producto
                        marca = i[2]
                        self.producto.marca = marca
                        descripcion = i[3]
                        self.producto.descripcion = descripcion
                        precio = i[4]
                        self.producto.precio = precio
                    
        elif opcion == 2:
            respuesta = input(f"Esta seguro de actualizar marca? Y/N: ")
            if respuesta == 'Y' or respuesta == 'y':
                marca = input("Ingrese el apellido paterno actualizado: ")
                self.producto.marca = marca
                for i in self.producto.read_a_product(id_producto):
                    if i[0] == id_producto:
                        id_producto = i[0]
                        self.producto.id_producto = id_producto
                        nombre_producto = i[1]
                        self.producto.nombre_producto = nombre_producto
                        descripcion = i[3]
                        self.producto.descripcion = descripcion
                        precio = i[4]
                        self.producto.precio = precio

            elif respuesta == 'N' or respuesta == 'n':
                for i in self.producto.read_a_product(id_producto):
                    if i[0] == id_producto:
                        id_producto = i[0]
                        self.producto.id_producto = id_producto
                        nombre_producto = i[1]
                        self.producto.nombre_producto = nombre_producto
                        marca = i[2]
                        self.producto.marca = marca
                        descripcion = i[3]
                        self.producto.descripcion = descripcion
                        precio = i[4]
                        self.producto.precio = precio

        elif opcion == 3:
            respuesta = input(f"Esta seguro de actualizar apellido materno? Y/N: ")
            if respuesta == 'Y' or respuesta == 'y':
                descripcion = input("Ingrese el apellido materno actualizado: ")
                self.producto.descripcion = descripcion
                for i in self.producto.read_a_product(id_producto):
                    if i[0] == id_producto:
                        id_producto = i[0]
                        self.producto.id_producto = id_producto
                        nombre_producto = i[1]
                        self.producto.nombre_producto = nombre_producto
                        marca = i[2]
                        self.producto.marca = marca
                        precio = i[4]
                        self.producto.precio = precio

            elif respuesta == 'N' or respuesta == 'n':
                for i in self.producto.read_a_product(id_producto):
                    if i[0] == id_producto:
                        id_producto = i[0]
                        self.producto.id_producto = id_producto
                        nombre_producto = i[1]
                        self.producto.nombre_producto = nombre_producto
                        marca = i[2]
                        self.producto.marca = marca
                        descripcion = i[3]
                        self.producto.descripcion = descripcion
                        precio = i[4]
                        self.producto.precio = precio

        elif opcion == 4:
            respuesta = input(f"Esta seguro de actualizar direccion? Y/N: ")
            if respuesta == 'Y' or respuesta == 'y':
                precio = input("Ingrese la direccion actualizada: ")
                self.producto.precio = precio
                for i in self.producto.read_a_product(id_producto):
                    if i[0] == id_producto:
                        id_producto = i[0]
                        self.producto.id_producto = id_producto
                        nombre_producto = i[1]
                        self.producto.nombre_producto = nombre_producto
                        marca = i[2]
                        self.producto.marca = marca
                        descripcion = i[3]
                        self.producto.descripcion = descripcion

            elif respuesta == 'N' or respuesta == 'n':
                for i in self.producto.read_a_product(id_producto):
                    if i[0] == id_producto:
                            id_producto = i[0]
                            self.producto.id_producto = id_producto
                            nombre_producto = i[1]
                            self.producto.nombre_producto = nombre_producto
                            marca = i[2]
                            self.producto.marca = marca
                            descripcion = i[3]
                            self.producto.descripcion = descripcion
                            precio = i[4]
                            self.producto.precio = precio

        self.producto.update_a_product()
    
    def delete_a_product(self):
        id_producto = int(input("Ingrese ID de cliente a buscar: "))
        self.producto.id_producto = id_producto
        productos = self.producto.read_a_product(id_producto)
        for i in productos:
            if id_producto == i[0]:
                nombre_producto = i[1]
                self.read_a_product()
        
        respuesta = input(f"Esta seguro de eliminar los datos de producto {nombre_producto}? Y/N:")
        if respuesta == 'Y' or respuesta == 'y':
            self.producto.delete_a_product()
        elif respuesta == 'N' or respuesta == 'n':  
            self.menu_producto()
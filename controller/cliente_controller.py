from models.cliente import Cliente

class Cliente_Controller:
    def __init__(self):
        self.cliente = Cliente()
        self.close = False

    def menu_cliente(self):
        while True:
            try:
                print("\n******************************")
                print("*          MENU CLIENTE        *")
                print("********************************")
                print("""
                    1. CREAR CLIENTE
                    2. LEER TODOS LOS CLIENTES
                    3. LEER CLIENTE
                    4. ACTUALIZAR CLIENTE
                    5. ELIMINAR CLIENTE
                    6. SALIR
                """)
                opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    self.create_a_client()
                elif opcion == 2:
                    self.read_clients()
                elif opcion == 3:
                    id_cliente = int(input("Ingrese ID de cliente a buscar: "))
                    self.cliente.id_cliente = id_cliente
                    self.read_a_client()
                elif opcion == 4:
                    self.update_a_client()
                elif opcion == 5:
                    self.delete_a_client()
                elif opcion == 6:
                    self.close = True
                    return True
                else:
                    print("No se encuentra opcion elegida, Intente nuevamente ....")
            except Exception:
                print("Dato ingresado no es correcto, Intente de nuevo ...")

    def read_clients(self):
        clientes = self.cliente.read_clients()
        if clientes:
            print("ID       NOMBRES         APELLIDO PAT.       APELLIDO MAT.       DIRECCION                CELULAR")
            print("---------------------------------------------------------------------------------------------------")
            for i in clientes:
                print(f"{i[0]}\t {i[1].ljust(16)}{i[2].ljust(20)}{i[3].ljust(20)}{i[4].ljust(25)}{i[5].ljust(20)}")

    def read_a_client(self,id_cliente=''):
        clientes = self.cliente.read_a_client(id_cliente)

        if clientes:
            print("ID       NOMBRES         APELLIDO PAT.       APELLIDO MAT.       DIRECCION                CELULAR")
            print("---------------------------------------------------------------------------------------------------")
            for i in clientes:
                print(f"{i[0]}\t {i[1].ljust(16)}{i[2].ljust(20)}{i[3].ljust(20)}{i[4].ljust(25)}{i[5].ljust(20)}")
                
    def create_a_client(self):
        
        print("\nREGISTRO CLIENTE")
        print("------------------")

        nombres = input("Ingrese nombre: ")
        apellido_pat = input("Ingrese apellido paterno: ") 
        apellido_mat = input("Ingrese apellido materno: ")
        direccion = input("Ingrese direccion: ")
        celular = input("Ingrese celular: ")

        self.cliente.nombres = nombres
        self.cliente.apellido_pat = apellido_pat
        self.cliente.apellido_mat = apellido_mat
        self.cliente.direccion = direccion
        self.cliente.celular = celular

        self.cliente.create_client()
    
    def update_a_client(self):
        id_cliente = int(input("Ingrese ID de cliente a buscar: "))
        self.cliente.id_cliente = id_cliente
        clientes = self.cliente.read_a_client(id_cliente)
        for i in clientes:
            if id_cliente == i[0]:
                nombres = i[1]
                self.read_a_client()

        print(f"\nACTUALIZAR DATOS DE {nombres.upper()}")
        print("------------------------------")
        print("""
            1. Nombres
            2. Apellido Pat.
            3. Apellido Mat.
            4. Direccion
            5. Celular
            6. Regresar
        """)
        opcion = int(input("Elija dato que actualizara: "))

        if opcion == 1:
            respuesta = input(f"Esta seguro de actualizar nombre? Y/N: ")
            if respuesta == 'Y' or respuesta == 'y':
                nombres = input("Ingrese el nombre actualizado: ")
                self.cliente.nombres = nombres
                for i in self.cliente.read_a_client(id_cliente):
                    if i[0] == id_cliente:
                        id_cliente = i[0]
                        print(id_cliente)
                        self.cliente.id_cliente = id_cliente
                        apellido_pat = i[2]
                        print(apellido_pat)
                        self.cliente.apellido_pat = apellido_pat
                        apellido_mat = i[3]
                        print(apellido_mat)
                        self.cliente.apellido_mat = apellido_mat
                        direccion = i[4]
                        print(direccion)
                        self.cliente.direccion = direccion
                        celular = i[5]
                        print(celular)
                        self.cliente.celular = celular
            elif respuesta == 'N' or respuesta == 'n':
                for i in self.cliente.read_a_client(id_cliente):
                    if i[0] == id_cliente:
                        id_cliente = i[0]
                        self.cliente.id_cliente = id_cliente
                        nombres = i[1]
                        self.cliente.nombres = nombres
                        apellido_pat = i[2]
                        self.cliente.apellido_pat = apellido_pat
                        apellido_mat = i[3]
                        self.cliente.apellido_mat = apellido_mat
                        direccion = i[4]
                        self.cliente.direccion = direccion
                        celular = i[5]
                        self.cliente.celular = celular
                    
        elif opcion == 2:
            respuesta = input(f"Esta seguro de actualizar apellido parterno? Y/N: ")
            if respuesta == 'Y' or respuesta == 'y':
                apellido_pat = input("Ingrese el apellido paterno actualizado: ")
                self.cliente.apellido_pat = apellido_pat
                for i in self.cliente.read_a_client(id_cliente):
                    if i[0] == id_cliente:
                        id_cliente = i[0]
                        print(id_cliente)
                        self.cliente.id_cliente = id_cliente
                        nombres = i[1]
                        print(nombres)
                        self.cliente.nombres = nombres
                        apellido_mat = i[3]
                        print(apellido_mat)
                        self.cliente.apellido_mat = apellido_mat
                        direccion = i[4]
                        print(direccion)
                        self.cliente.direccion = direccion
                        celular = i[5]
                        print(celular)
                        self.cliente.celular = celular
            elif respuesta == 'N' or respuesta == 'n':
                for i in self.cliente.read_a_client(id_cliente):
                    if i[0] == id_cliente:
                        id_cliente = i[0]
                        self.cliente.id_cliente = id_cliente
                        nombres = i[1]
                        self.cliente.nombres = nombres
                        apellido_pat = i[2]
                        self.cliente.apellido_pat = apellido_pat
                        apellido_mat = i[3]
                        self.cliente.apellido_mat = apellido_mat
                        direccion = i[4]
                        self.cliente.direccion = direccion
                        celular = i[5]
                        self.cliente.celular = celular

        elif opcion == 3:
            respuesta = input(f"Esta seguro de actualizar apellido materno? Y/N: ")
            if respuesta == 'Y' or respuesta == 'y':
                apellido_mat = input("Ingrese el apellido materno actualizado: ")
                self.cliente.apellido_mat = apellido_mat
                for i in self.cliente.read_a_client(id_cliente):
                    if i[0] == id_cliente:
                        id_cliente = i[0]
                        self.cliente.id_cliente = id_cliente
                        nombres = i[1]
                        self.cliente.nombres = nombres
                        apellido_pat = i[2]
                        self.cliente.apellido_pat = apellido_pat
                        direccion = i[4]
                        self.cliente.direccion = direccion
                        celular = i[5]
                        self.cliente.celular = celular
            elif respuesta == 'N' or respuesta == 'n':
                for i in self.cliente.read_a_client(id_cliente):
                    if i[0] == id_cliente:
                        id_cliente = i[0]
                        self.cliente.id_cliente = id_cliente
                        nombres = i[1]
                        self.cliente.nombres = nombres
                        apellido_pat = i[2]
                        self.cliente.apellido_pat = apellido_pat
                        apellido_mat = i[3]
                        self.cliente.apellido_mat = apellido_mat
                        direccion = i[4]
                        self.cliente.direccion = direccion
                        celular = i[5]
                        self.cliente.celular = celular

        elif opcion == 4:
            respuesta = input(f"Esta seguro de actualizar direccion? Y/N: ")
            if respuesta == 'Y' or respuesta == 'y':
                direccion = input("Ingrese la direccion actualizada: ")
                self.cliente.direccion = direccion
                for i in self.cliente.read_a_client(id_cliente):
                    if i[0] == id_cliente:
                        id_cliente = i[0]
                        self.cliente.id_cliente = id_cliente
                        nombres = i[1]
                        self.cliente.nombres = nombres
                        apellido_pat = i[2]
                        self.cliente.apellido_pat = apellido_pat
                        apellido_mat = i[3]
                        self.cliente.apellido_mat = apellido_mat
                        celular = i[5]
                        self.cliente.celular = celular
            elif respuesta == 'N' or respuesta == 'n':
                if i[0] == id_cliente:
                        id_cliente = i[0]
                        self.cliente.id_cliente = id_cliente
                        nombres = i[1]
                        self.cliente.nombres = nombres
                        apellido_pat = i[2]
                        self.cliente.apellido_pat = apellido_pat
                        apellido_mat = i[3]
                        self.cliente.apellido_mat = apellido_mat
                        direccion = i[4]
                        self.cliente.direccion = direccion
                        celular = i[5]
                        self.cliente.celular = celular

        elif opcion == 5:
            respuesta = input(f"Esta seguro de actualizar numero de celular? Y/N: ")
            if respuesta == 'Y' or respuesta == 'y':
                celular = input("Ingrese el numero de celular actualizado: ")
                self.cliente.celular = celular
                for i in self.cliente.read_a_client(id_cliente):
                    if i[0] == id_cliente:
                        id_cliente = i[0]
                        self.cliente.id_cliente = id_cliente
                        nombres = i[1]
                        self.cliente.nombres = nombres
                        apellido_pat = i[2]
                        self.cliente.apellido_pat = apellido_pat
                        apellido_mat = i[3]
                        self.cliente.apellido_mat = apellido_mat
                        direccion = i[4]
                        self.cliente.direccion = direccion
            elif respuesta == 'N' or respuesta == 'n':
                if i[0] == id_cliente:
                        id_cliente = i[0]
                        self.cliente.id_cliente = id_cliente
                        nombres = i[1]
                        self.cliente.nombres = nombres
                        apellido_pat = i[2]
                        self.cliente.apellido_pat = apellido_pat
                        apellido_mat = i[3]
                        self.cliente.apellido_mat = apellido_mat
                        direccion = i[4]
                        self.cliente.direccion = direccion
                        celular = i[5]
                        self.cliente.celular = celular

        self.cliente.update_a_client()
    
    def delete_a_client(self):
        id_cliente = int(input("Ingrese ID de cliente a buscar: "))
        self.cliente.id_cliente = id_cliente
        clientes = self.cliente.read_a_client(id_cliente)
        for i in clientes:
            if id_cliente == i[0]:
                nombres = i[1]
                self.read_a_client()
        
        respuesta = input(f"Esta seguro de eliminar los datos de cliente {nombres}? Y/N:")
        if respuesta == 'Y' or respuesta == 'y':
            self.cliente.delete_a_client()
        elif respuesta == 'N' or respuesta == 'n':  
            self.menu_cliente()
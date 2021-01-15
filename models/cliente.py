from conexion.conn import Conexion

class Cliente:
    def __init__(self,id_cliente='',nombres='',apellido_pat='',apellido_mat='',direccion='',celular=''):
        self.model = Conexion('cliente')
        self.id_cliente = id_cliente
        self.nombres = nombres
        self.apellido_pat = apellido_pat
        self.apellido_mat = apellido_mat
        self.direccion = direccion
        self.celular = celular

    def read_clients(self):
        try:
            return self.model.get_all()
        except ConnectionError as err:
            return err

    def read_a_client(self,id_cliente):
        try:
            query = f"SELECT * FROM cliente WHERE id_cliente='{self.id_cliente}';"
            return self.model.execute_query(query)
        except ConnectionError as err:
            return err

    def create_client(self):
        try:
            query = f"""
                INSERT INTO cliente(nombres,apellido_pat,apellido_mat,direccion,celular)
                VALUES('{self.nombres}','{self.apellido_pat}','{self.apellido_mat}','{self.direccion}','{self.celular}');
            """
            self.model.execute_query(query)
            self.model.commit()
        except ConnectionError as err:
            return err

    def update_a_client(self):
        try:
            query = f"""
                UPDATE cliente SET nombres='{self.nombres}',apellido_pat='{self.apellido_pat}',apellido_mat='{self.apellido_mat}',
                direccion='{self.direccion}',celular='{self.celular}' WHERE id_cliente = '{self.id_cliente}';
            """
            self.model.execute_query(query)
            self.model.commit()
        except ConnectionError as err:
            self.model.rollback()
            return err

    def delete_a_client(self):
        try:
            query = f"""
                DELETE FROM cliente WHERE id_cliente = '{self.id_cliente}'
            """
            self.model.execute_query(query)
            self.model.commit()
        except ConnectionError as err:
            self.model.rollback()
            return err
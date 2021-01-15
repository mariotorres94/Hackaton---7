from conexion.conn import Conexion

class Producto:
    def __init__(self,id_producto='',nombre_producto='',marca='',descripcion='',precio=''):
        self.model = Conexion('producto')
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.marca = marca
        self.descripcion = descripcion
        self.precio = precio

    def read_a_product(self,id_producto):
        try:
            query = f"SELECT * FROM producto WHERE id_producto = '{self.id_producto}';"
            return self.model.execute_query(query)
        except ConnectionError as err:
            return err

    def read_products(self):
        try:
            return self.model.get_all()
        except ConnectionError as err:
            return err

    def create_a_product(self):
        try:
            query = f"""
                INSERT INTO producto(nombre_producto,marca,descripcion,precio)
                VALUES('{self.nombre_producto}','{self.marca}','{self.descripcion}','{self.precio}');
            """
            self.model.execute_query(query)
            self.model.commit()
        except ConnectionError as err:
            self.model.rollback()
            return err

    def read_a_product_for_brand(self):
        try:
            query = f"""
                SELECT * FROM producto 
                WHERE marca = '{self.marca}';
            """
            return self.model.execute_query(query)
        except ConnectionError as err:
            self.model.rollback()
            return err

    def read_a_product_for_price(self, precio):
        try:
            query = f"""
                SELECT * FROM producto
                WHERE precio >= '{self.precio}' and precio <= '{self.precio}'
            """
            return self.model.execute_query(query)
        except ConnectionError as err:
            self.model.rollback()
            return err

    def update_a_product(self):
        try:
            query = f"""
                UPDATE producto SET nombre_producto='{self.nombre_producto}',marca='{self.marca}',
                descripcion='{self.descripcion}',precio='{self.precio}' WHERE id_producto = '{self.id_producto}';
            """
            self.model.execute_query(query)
            self.model.commit()
        except ConnectionError as err:
            self.model.rollback()
            return err

    def delete_a_product(self):
        try:
            query = f"""
                DELETE FROM producto WHERE id_producto='{self.id_producto}';
            """
            self.model.execute_query(query)
            self.model.commit()
        except ConnectionError as err:
            self.model.rollback()
            return err

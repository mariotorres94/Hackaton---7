from conexion.conn import Conexion

class Detalle_Orden:
    def __init__(self,id_orden='',id_producto='',cantidad_producto='',total_producto=''):
        self.model = Conexion('detalle_orden')
        self.id_orden = id_orden
        self.id_producto = id_producto
        self.cantidad_producto = cantidad_producto
        self.total_producto = total_producto

    def read_detail_order(self):
        try:
            query = f"""
                SELECT o.id_orden,d.id_producto,o.id_cliente,d.cantidad_producto,d.total_producto,o.status,o.fecha,o.total FROM detalle_orden d
                INNER JOIN orden o
                ON d.id_orden = o.id_orden
                WHERE d.id_orden = {self.id_orden}
            """
            return self.model.execute_query(query)
        except ConnectionError as err:
            return err

    def create_a_details_order(self):
        try:
            query = f"""
                INSERT INTO detalle_orden(id_orden,id_producto,cantidad_producto,total_producto) 
                VALUES('{self.id_orden}','{self.id_producto}','{self.cantidad_producto}','{self.total_producto}');
            """
            self.model.execute_query(query)
            self.model.commit()
        except ConnectionError as err:
            self.model.rollback()
            return err

    def update_a_details_order(self):
        try:
            query = f"""
                UPDATE detalle_orden SET total_producto = '{self.total_producto}' 
                WHERE id_orden = (SELECT max(id_orden) FROM detalle_orden);
            """
            self.model.execute_query(query)
            self.model.commit()
        except ConnectionError as err:
            self.model.rollback()
            return err
    
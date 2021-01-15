from conexion.conn import Conexion

class Orden(Conexion):
    def __init__(self,id_orden='',id_cliente='',status='',fecha='',total='',id_producto='',cantidad_producto='',total_producto=''):
        self.model = Conexion('orden')
        self.model1 = Conexion('detalle_orden')
        self.model1 = Conexion('')
        self.id_orden = id_orden
        self.id_cliente = id_cliente
        self.status = status
        self.fecha = fecha
        self.total = total
        self.id_producto = id_producto
        self.cantidad_producto = cantidad_producto
        self.total_producto = total_producto

    def read_all_orders(self):
        try:
            return self.model.get_all()
        except ConnectionError as err:
            return err

    def read_a_order(self):
        try:
            query = """
                SELECT * FROM orden ORDER BY id_orden DESC LIMIT 1
            """
            return self.model.execute_query(query)
        except ConnectionError as err:
            return err

    def read_orders_for_date(self):
        try:
            query = f"""
                SELECT * FROM orden 
                WHERE fecha = '{self.fecha}'
            """
            return self.model.execute_query(query)
        except ConnectionError as err:
            return err

    def read_orders_of_a_client(self):
        try:
            query = f"""
            select o.id_orden,cl.id_cliente,cl.nombres,cl.apellido_pat,cl.apellido_mat,cl.direccion,cl.celular,o.status,o.fecha,o.total 
            from cliente cl
            inner join orden o
            on cl.id_cliente = o.id_cliente
            where o.id_cliente = '{self.id_cliente}'
            """
            return self.model.execute_query(query)
        except ConnectionError as err:
            return err

    def update_data_of_a_order(self):
        try:
            query = f"""
                UPDATE orden SET status = '{self.status}'
                WHERE id_orden = '{self.id_orden}'
            """
            self.model.execute_query(query)
            self.model.commit()
        except ConnectionError as err:
            self.model.rollback()
            return err

    def create_a_order(self):
        try:
            query = f"""
                INSERT INTO orden(id_cliente,status,fecha,total) 
                VALUES('{self.id_cliente}','{self.status}','{self.fecha}','{self.total}')
                RETURNING id_orden;
            """
            self.model.execute_query(query)
            self.model.commit()
            id_orden = self.model.cursor.fetchone()[0]
            return id_orden
        except ConnectionError as err:
            self.model.rollback()
            return err

    def update_a_order(self):
        try:
            query = f"""
                UPDATE orden SET total = '{self.total}' 
                WHERE id_orden = (SELECT max(id_orden) FROM orden);
            """
            self.model.execute_query(query)
            self.model.commit()
        except ConnectionError as err:
            self.model.rollback()
            return err

    def read_details_order(self):
        try:
            query = f"""
            select * from orden o
            inner join detalle_orden d
            on d.id_orden = o.id_orden
            where o.id_orden = '{self.id_orden}'
            """
            return self.model1.execute_query(query)
        except ConnectionError as err:
            self.model1.rollback
            return err
    
    def delete_a_orden(self):
        try:
            query = f"DELETE FROM orden WHERE id_orden='{self.id_orden}';"
            self.model.execute_query(query)
            self.model.commit()
        except ConnectionError as err:
            self.model.rollback()
            return err
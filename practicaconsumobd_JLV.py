import mysql.connector


class PracticaConsumoBD:

    def __init__(self, user, password, host, port, service):
        try:
            self.connection = mysql.connector.connect(
                user=user,
                password=password,
                host=host, port=port,
                database=service
            )
            self.cursor = self.connection.cursor()
            print("coneccion correcta")
        except mysql.connector.Error as error:
            print("Error coneccion")

    def guardar_cliente(self, nombre, fecha_nac,domicilio):
        self.cursor.execute(
        """
        INSERT INTO CUSTOMERS (NOMBRE, FECHA_NAC,DOMICILIO) VALUES (%s,%s,%s)
        """, (nombre, fecha_nac, domicilio)
        )
        self.connection.commit()
        print("Actualizado Correctamente")

    def guardar_proveedor(self, nombre, telefono, correo):
        self.cursor.execute(
        """
        INSERT INTO PROVEEDOR (NOMBRE, TELEFONO,CORREO) VALUES (%s,%s,%s)
        """, (nombre, telefono, correo)
        )
        self.connection.commit()
        print("Actualizado Correctamente")

    def mostrar_cliente(self):
        self.cursor.execute(
        """
        select * from customers 
        """
        )
        for fila in self.cursor.fetchall():
            print(fila)

    def mostrar_proveedor(self):
        self.cursor.execute(
        """
        select * from proveedor 
        """
        )
        for fila in self.cursor.fetchall():
            print(fila)

    def actualizar_cliente(self, customer_id, nombre, fecha_nac, domicilio):
        self.cursor.execute(
        """
        UPDATE CUSTOMERS SET NOMBRE = %s, FECHA_NAC = %s, DOMICILIO = %s
        WHERE CUSTOMER_ID = %s
        """, (nombre, fecha_nac, domicilio,customer_id)
        )
        self.connection.commit()
        print("Actualizado Correctamente")

    def actualizar_proveedor(self, proveedor_id, nombre, telefono, correo):
        self.cursor.execute(
        """
        UPDATE PROVEEDOR SET NOMBRE = %s, TELEFONO = %s, CORREO = %s
        WHERE PROVEEDOR_ID = %s
        """, (nombre, telefono, correo,proveedor_id)
        )
        self.connection.commit()
        print("Actualizado Correctamente")

    def eliminar_cliente(self, customer_id):
        self.cursor.execute(
        """
        DELETE FROM CUSTOMERS WHERE CUSTOMER_ID = %s
        """,(customer_id,)
        )
        self.connection.commit()
        print("eLIMINADO Correctamente")


    def eliminar_proveedor(self, proveedor_id):
        self.cursor.execute(
        """
        DELETE FROM PROVEEDOR WHERE PROVEEDOR_ID = %s
        """,(proveedor_id,)
        )
        self.connection.commit()
        print("Eliminado Correctamente")
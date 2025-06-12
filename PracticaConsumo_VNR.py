import mysql.connector

class PracticaConsumoDB:
    # Necesito datos elementales
    def __init__(self, user, password, host, port, service):
        #INTENTO CARGAR UNA CONEXIÓN
        try:
            self.connection = mysql.connector.connect(
                host = host,
                port = port,
                user = user,
                password=password,
                database = service,
            )
            self.cursor = self.connection.cursor()
            print("Conexión correcta")

        except mysql.connector.Error as error:
            print("Error conectado a la db")

#FUNCIÓN PARA GUARDAR
    def guardar_cliente(self,nombre,fecha_nac,domicilio):
        self.cursor.execute(
"""
        INSERT INTO CUSTOMERS (NOMBRE,FECHA_NAC,DOMICILIO) VALUES (%s,%s,%s)
        """,(nombre,fecha_nac,domicilio))
        self.connection.commit()
        print("Insertado con exito")
        #FUNCIÓN PARA LEER A LOS CLIENTES

    def mostrar_clientes(self):
        self.cursor.execute(
        """
        SELECT * FROM CUSTOMERS
        """
        )
        for fila in self.cursor.fetchall():
            print(fila)

    #ACTUALIZAR UN CLIENTE}
    def actualizar_cliente(self,customer_id,nombre,fecha_nac,domicilio):
        self.cursor.execute(
        """UPDATE CUSTOMERS SET NOMBRE = %s, FECHA_NAC = %s,
        DOMICILIO= %s WHERE CUSTOMER_ID = %s
        """,(nombre,fecha_nac,domicilio,customer_id))
        self.connection.commit()
        print("Actualizado correctamente")

    #ELIMINAR CLIENTE
    def eliminar_cliente(self,customer_id):
        self.cursor.execute(
        """
        DELETE FROM CUSTOMERS WHERE CUSTOMER_ID = %s
        """,(customer_id, ))
        self.connection.commit()
        print("Eliminado corretamente")

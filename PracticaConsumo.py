import oracledb

class PracticaConsumoDB:

    #Necesito datos elementales
    def __init__(self, user, password, host, puerto, service):
        #Intento cargar la conexion
        try:
            self.connection = oracledb.connect(
                user = user,
                password = password,
                dsn = f"{host}:{puerto}/{service}"
            )
            self.cursor = self.connection.cursor()
            print("Conexion correcta")

        except oracledb.DatabaseError as error:
            print(error)

    #Funcion para guardar
    def guardar_cliente(self, nombre, fecha_nac, domicilio):
        self.cursor.execute(
            """
            INSERT INTO CUSTOMERS (NOMBRE, FECHA_NAC, DOMICILIO)
            VALUES(:1, :2, :3)
            """, (nombre, fecha_nac, domicilio)
        )
        self.connection.commit()
        print("Insertado con exito")
        #Funcion para leer todos los clientes
    def mostrar_clientes(self):
        self.cursor.execute(
            """
            SELECT * FROM CUSTOMERS
            """
        )
        for fila in self.cursor.fetchall():
            print(fila)
    #Actualizar un cliente
    def actualizar_cliente(self, customer_id, nombre, fecha_nac, domicilio):
        self.cursor.execute(
            """
            UPDATE CUSTOMERS SET NOMBRE = :1, FECHA_NAC = :2, DOMICILIO = :3
            WHERE CUSTOMER_ID = :4  
            """, (nombre, fecha_nac, domicilio,customer_id)
        )
        self.connection.commit()
        print("Actualizado correctamente")

    def eliminar_cliente(self, customer_id):
        self.cursor.execute(
            """
            DELETE FROM CUSTOMERS WHERE CUSTOMER_ID = :1
            """, (customer_id,)
        )
        self.connection.commit()
        print("Eliminado correctamente")



import oracledb

class PracticaConsumoDB:
    def __init__(self, user, password, host, port, service):
        # Intento cargar la conexión
        try:
            self.connection = oracledb.connect(
                user = user,
                password = password,
                dsn = f"{host}:{port}/{service}"
                # encoding = "utf8"
            )
            self.cursor = self.connection.cursor()
            print("Conexión correcta.")
        except oracledb.DatabaseError as error:
            print("Error al conectar la db")

    # Función para guardar
    def guardar_cliente(self, nombre, fecha_nac, domicilio):
        self.cursor.execute(
        """
            INSERT INTO CUSTOMERS(NOMBRE, FECHA_NAC, DOMICILIO)
            VALUES (:1, :2, :3)
            """, (nombre, fecha_nac, domicilio)
        )
        self.connection.commit()
        print("Insertado con éxito.")

    # Función para leer todos los clientes
    def mostrar_cliente(self):
        self.cursor.execute(
            """
            SELECT * FROM CUSTOMERS
            """
        )
        for fila in self.cursor.fetchall():
            print(fila)

    # Actualizar un cliente
    def actualizar_cliente(self, customer_id, nombre, fecha_nac, domicilio):
        self.cursor.execute(
            """
            UPDATE CUSTOMERS
            SET NOMBRE = :1, FECHA_NAC = :2, DOMICILIO = :3
            WHERE CUSTOMER_ID = :4
            """
        , (nombre, fecha_nac, domicilio, customer_id))
        self.connection.commit()
        print("Actualizado correctamente")

    def eliminar_cliente(self, customer_id):
        self.cursor.execute(
            """
            DELETE FROM CUSTOMERS
            WHERE CUSTOMER_ID = :1
            """, (customer_id, ))
        self.connection.commit()
        print("Eliminado correctamente")

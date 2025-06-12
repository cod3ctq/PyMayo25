import pymysql


class PracticaConsumoDB:
    def __init__(self, user, password, host, service):
        try:
            self.con=pymysql.connect(
                host = host,

                user =  user,
                password = password,
                database = service

            )
            self.cursor = self.con.cursor()
            print ("Conexión establecida")
        except Exception as error:
            print("Error al conectar la db")


    #Funcion para guardar
    def guardar_cliente(self,nombre,fecha_nac,domicilio):
        self.cursor.execute(
        """
        INSERT INTO CUSTOMERS (NOMBRE,FECHA_NAC,DOMICILIO) VALUES (%s,%s,%s)
        """,(nombre,fecha_nac,domicilio))
        self.con.commit()
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
        self.con.commit()
        print("Actualizado correctamente")

    def eliminar_cliente (self, customer_id):
        self.cursor.execute(
            """DELETE FROM CUSTOMERS WHERE CUSTOMER_ID = %s
            """, (customer_id,)

        )
        self.con.commit()
        print("Eliminado correctamente")


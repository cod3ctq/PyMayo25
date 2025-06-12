import mysql.connector

class PruebaMusic:
    def __init__(self, user, password, host, port, service):
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

    def guardar_cancion(self,TITULO,DURACION,ALBUM_ID):
        self.cursor.execute("""
        INSERT INTO CANCION (TITULO,DURACION,ALBUM_ID) VALUES (%s,%s,%s)
        """,(TITULO,DURACION,ALBUM_ID))
        self.connection.commit()
        print("Insertado con exito")

    def mostrar_cancion(self):
        self.cursor.execute(
            """
        SELECT * FROM CANCION 
        """
        )
        for fila in self.cursor.fetchall():
            print(fila)

    def actualizar_cancion(self,TITULO,DURACION,ALBUM_ID,CANCION_ID):
        self.cursor.execute(
            """
            UPDATE CANCION SET TITULO =%s, DURACION =%s, ALBUM_ID =%s WHERE CANCION_ID =%s
            """, (TITULO, DURACION, ALBUM_ID,CANCION_ID))
        self.connection.commit()
        print("Actualizado con exito")

    def eliminar_cancion(self,CANCION_ID):
        self.cursor.execute(
            """
            DELETE FROM CANCION WHERE CANCION_ID =%s
            """, (CANCION_ID,))
        self.connection.commit()
        print("Eliminado con exito")
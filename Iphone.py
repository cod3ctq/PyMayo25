class Iphone:
    #atributos de clase
    #Reciben valor al interor de las clases
    #El valor es compartido por todos los objetos de la clase
    sistema_operativo = "iOs"
    marca = "Apple"


    #atributos de instancia
    def __init__(self, modelo, color, precio):
        self.modelo = modelo
        self.color = color
        self.precio = precio

        """Convierte en texto el estado del objeto"""
    """def __str__(self):
        return f"Marca->{self.marca}",f"Color->{self.color}",f"Precio->{self.precio}"
"""
    #Getter
    @property
    def obtener_precio(self):
        return self.precio

    #Setter
    @obtener_precio.setter
    def establecer_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    @property
    def obtener_modelo(self):
        return self.modelo

    #Setter
    @obtener_modelo.setter
    def establecer_modelo(self, nuevo_modelo):
        self.modelo = nuevo_modelo

    @property
    def obtener_color(self):
        return self.color

    # Setter
    @obtener_color.setter
    def establecer_color(self, nuevo_color):
        self.color = nuevo_color

    #Funcion de clase, accede unicamente a componentes estaticos
    @classmethod
    def obtener_marca(cls):
        return Iphone.marca

    @classmethod
    def obtener_so(cls):
        return Iphone.sistema_operativo

    #Funcion estatica
    #Son funciones donde podemos programar logica, pueden recibir argumentos pero no pueden acceder a los miembros de clase o de instancia
    @staticmethod
    def mostrar_imei(imei):
        #return "7265984657"
        return imei
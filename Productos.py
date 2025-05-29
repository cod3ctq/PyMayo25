class Product:

    """
    Métodos:
    @property y @property.setter para manejar los atributos
    @classmethod para crear un producto genérico
    @staticmethod para validar el precio (mayor que 0)
    str() para imprimir la información del producto
    """

#Atributos de clase

    costo_base_envio = 150

#atributos de instancia

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio


    def __(self):
     return f"Nombre ->{self.nombre}", f"Categoria ->{self.categoria}", f"Precio ->{self.precio}"

    #Getter
    @property
    def obtener_nombre(self):
        return self.nombre
    #Setter
    @obtener_nombre.setter
    def establecer_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    #Getter
    @property
    def obtener_categoria(self):
        return self.categoria
    #Setter
    @obtener_categoria.setter
    def establecer_categoria(self, nuevo_categoria):
        self.categoria = nuevo_categoria

    #Getter
    @property
    def obtener_precio(self):
        return self.precio
    # Setter
    @obtener_precio.setter
    def establecer_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    @staticmethod
    def costo_base_envio(costo_base_envio):
        return 345


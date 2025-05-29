class Producto:

    #Atributos de clase
    costo_base_envio = 150

    # Atributos de instancia
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        return f"Nombre->{self.nombre}, Categoria->{self.categoria}, Precio->{self.precio}"

    @property
    def obtener_nombre(self):
        return self.nombre

    @obtener_nombre.setter
    def obtener_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    @property
    def obtener_categoria(self):
        return self.categoria

    @obtener_categoria.setter
    def obtener_categoria(self, nueva_categoria):
        self.categoria = nueva_categoria

    @property
    def obtener_precio(self):
        return self.precio

    @obtener_precio.setter
    def obtener_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    @classmethod
    def mostrar_costo_base_envio(cls):
        print(Producto.costo_base_envio)
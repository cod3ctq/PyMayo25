class Iphone:
    # Atributos de clase
    # El valor es compartido por todos los objetos de la clase

    sistema_operativo = "iOS"
    marca = "Apple"

    # Atributos de instancia
    def __init__(self, modelo, color, precio):
        self.modelo = modelo
        self.color = color
        self.precio = precio

    def __str__(self):
        return f"Modelo: {self.modelo}, Color: {self.color}, Precio: {self.precio}"

    @property   #getters
    def get_precio(self):
        return self.precio

    @property # getters
    def get_modelo(self):
        return self.modelo

    @property #getters
    def get_color(self):
        return self.color

    @get_precio.setter # setter
    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    @get_modelo.setter  # setter
    def set_modelo(self, nuevo_modelo):
        self.modelo = nuevo_modelo

    @get_color.setter  # setter
    def set_color(self, nuevo_color):
        self.color = nuevo_color

    # Función de clase:
    # Accede solo a componentes de clase
    @classmethod
    def get_marca(cls):
        return Iphone.marca

    @classmethod
    def get_so(cls):
        return Iphone.sistema_operativo

    # Función estática
    # Pueden recibir argumentos pero, no pueden acceder a los
    # miembros de clase o de instancia.
    @staticmethod
    def mostrar_imei(imei):
        # return "0123456789"
        return imei
        # return self.color # No se puede acceder
        # return cls.marca # No se puede acceder
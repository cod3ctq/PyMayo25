class Iphone:

    #Atributos de Clase
    marca = "apple"
    sistema_operativo = "ios"   #Son atributos que comparten todos los objetos instanciados

    #Atributos de instancia
    def __init__(self, color, modelo, precio):
        self.color = color
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f"Modelo->{self.modelo},Color->{self.color},Precio->{self.precio}"
                #f antes significa que se va a presentar en ese formato

    @property
    def obtener_precio(self):
        return self.precio


    @obtener_precio.setter
    def establecer_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    @property
    def obtener_modelo(self):
        return self.modelo

    @obtener_modelo.setter
    def establecer_modelo(self, nuevo_modelo):
        self.modelo = nuevo_modelo

    @property
    def obtener_color(self):
        return self.color

    @obtener_color.setter
    def establecer_color(self, nuevo_color):
        self.color = nuevo_color




    #Función de clase, aacede unicamente a componentes
    @classmethod
    def obtener_marca(cls):
        return Iphone.marca

    @classmethod
    def obtener_so(cls):
        return Iphone.sistema_operativo

    # Función estática
    # Son funciones donde podemos programar lógica, pueden recibir argumentos pero
    # no pueden acceder a los miembros de clase o onstancia

    @staticmethod
    def mostrar_imei():
        return "3454655767"
        # return self.color .... no se puede acceder a miembros de la clase

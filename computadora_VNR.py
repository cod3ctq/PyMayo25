class Computadora:

    #Atributos QUE

    #Metodo constructor: mecanismo para definir estado inicial
    #de los objetos
    def __init__(self, marca,modelo,precio):
        self.marca = marca     #Público
        self._modelo = modelo  #Protegida convención: _nombre
        self.precio = precio #Protegida convención: nombre

#Mecanismo para extraer informacion puntual de los atributos del modelo

    #Getter
    #self significa el objeto mismo
    @property  #Indica que esta funcion es mas bien una propiedad
    def get_precio(self):
        return self.__precio
    #Setter
    #Mecanismo para inyectar informacion puntual a los atributos del modelo
    @get_precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self,nuevo_modelo):
        self._modelo = nuevo_modelo


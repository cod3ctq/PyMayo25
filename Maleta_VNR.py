from importlib.util import source_hash


class Maleta:

    costo_base_envio=150 #Miembros de clase

    def __init__(self,color,marca,peso): #atributos de instancia.
        self.color = color
        self.marca = marca
        self.peso = peso


    def __str__(self):
      return f"Maleta color -> {self.color}",f"marca->{self.marca}",f"peso->{self.peso}"
#GETTER
    @property
    def obtener_color(self):
        return self.color
#SETTER
    @obtener_color.setter
    def obtener_color(self,nuevo_color):
        self.color = nuevo_color
#GETTER
    @property
    def obtener_marca(self):
        return self.marca
#SETTER
    @obtener_marca.setter
    def obtener_marca(self,nueva_marca):
        self.marca = nueva_marca
#GETTER
    @property
    def obtener_peso(self):
        return self.peso
#SETTER
    @obtener_peso.setter
    def obtener_peso(self,nuevo_peso):
        self.peso = nuevo_peso
#CLASSMETHOD
    @classmethod
    def obtener_costo_base_envio(cls):
        return cls.costo_base_envio
#STATICMETHOD
    @staticmethod #No puede acceder a los miembros de clase o de instacia.
    def abrir_con_contraseña(contraseña):
        if contraseña == 48398:
            print("Maleta abierta")
        else:
            print("Contraseña incorrecta")
        #Validar con un if, si la contraseña es correcta


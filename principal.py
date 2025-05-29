from computadora import Computadora
from Iphone import Iphone
from producto import Producto

#Crear un objeto de clase Computadora
computadora = Computadora("Hp","Pavilion 17",3000)

#Imprime la llamada a un atributo publico
print(computadora.marca)
#Imprime la llamada a un atributo protegido
print(computadora._modelo)  #forma incorrecta de acceder
#Imprime la llamada a un atributo privado, en realidad se llama a
#la funcion configurada como setter (@property.setter)
print(computadora._Computadora__precio)
print(computadora.get_precio)
#-----------------------------------------------
ip1 = Iphone("7","Gris",5000)
ip2 = Iphone("12","Rojo",15000)
ip3 = Iphone("10","Azul",11000)
ip4 = Iphone("8","Negro",9000)
ip5 = Producto("Silla", "Muebles", 5000)

#Cuando varios objetos tiene valores diferentes para el mismo
#atributo, se les conoce como atributos de instancia
print(ip1.obtener_modelo)
print(ip2.obtener_modelo)
print(ip3.obtener_modelo)
print(ip4.obtener_modelo)

print(ip1.obtener_marca())
print(ip2.obtener_marca())
print(ip3.obtener_marca())
print(ip4.obtener_marca())


print(Iphone.mostrar_imei())
print(ip1.mostrar_imei())

print(ip5.nombre)
print(ip5.categoria)
print(ip5.precio)

print(Producto.mostrar_costo_base_envio())

print(ip5)

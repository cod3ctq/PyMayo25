from Maleta import Maleta
from Computadora import Computadora
from Iphone import Iphone

#Crear un objeto de clase Computadora
computadora = Computadora("HP","Pavilion 17",3000)

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

#Cuando varios objetos tiene valores diferentes para el mismo
#atributo, se les conoce como atributos de instancia
print(ip1.obtener_modelo)
print(ip2.obtener_modelo)
print(ip3.obtener_modelo)
print(ip4.obtener_modelo)
#Ejecuta e imprime el valor de clases compartido
#por todos los objetos hechos de ella
print(ip1.obtener_marca())
print(ip2.obtener_marca())
print(ip3.obtener_marca())
print(ip4.obtener_marca())
##Ejecuta e imprime el valor de clases compartido
#por todos los objetos hechos de ella
print(ip1.obtener_so())
print(ip2.obtener_so())
print(ip3.obtener_so())
print(ip4.obtener_so())

#Llamado a un MIEMBRO ESTÁTICO
print(Iphone.mostrar_imei('98475204'))
print(ip1.mostrar_imei('3450945'))

#----------------------------------------------#
maleta = Maleta("Rojo","Prada","25kg")

print(maleta.obtener_color)
print(maleta.obtener_marca)
print(maleta.obtener_peso)

print(maleta.obtener_costo_base_envio())
print(maleta.abrir_con_contraseña(489798))



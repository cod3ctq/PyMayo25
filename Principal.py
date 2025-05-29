#Crear un objeto de clase Computadora
from Computadora import Computadora
from Iphone import Iphone
from Producto import Producto

computadora = Computadora(marca="Hp", modelo="Pavillon", precio=3000)

#Imprime la llamada a un atributo publico
print(computadora.marca)
#Imprime la llamada a un atributo protegido
print(computadora._modelo)
#Imprime la llamada a un atributo privado, en realidad se llama a la funcion configurada como setter
print(computadora.get_precio)

ip1= Iphone(modelo="7",color="Gris",precio=5000)
ip2= Iphone(modelo="12",color="Rojo",precio=15000)
ip3= Iphone(modelo="10",color="Azul",precio=11000)
ip4= Iphone(modelo="8",color="Negro",precio=9000)

#Cuando varios objetos tienen valores diferentes para el mismo atributo, se les conoce como atributos instancia
print(ip1.obtener_modelo)
print(ip2.obtener_modelo)
print(ip3.obtener_modelo)
print(ip4.obtener_modelo)

#Ejecuta e imprime el valor de clase compartido por todos los objetos hechos de ella
print(Iphone.obtener_marca())

#Ejecuta e imprime el valor de clase compartido por todos los objetos hechos de ella
print(ip1.obtener_so())

#Llamado a un miembri estatico
print(Iphone.mostrar_imei("979283495"))
print(ip1.mostrar_imei("979283495"))

print("------------------------------------")
p1 = Producto(nombre="Laptop", categoria="Electronica", precio=10000)
print(p1)

prod_generico = Producto.producto_generico()
print(prod_generico)
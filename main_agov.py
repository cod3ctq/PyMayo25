# Crear un objeto de clase Computadora
from pickle import FALSE

from Computadora import Computadora
from Iphone import Iphone
from producto import Producto

computadora = Computadora("HP", "Pavilion 17", 3000)

# Imprime la llamada a un atributo público
# print(computadora.marca)
# print(computadora._modelo) # manera incorrecta de acceder
# print(computadora.precio) # manera incorrecta de acceder
# print(computadora.get_precio)

###############################################
### Iphone ###
ip1 = Iphone("7", "Gris", 5000)
ip2 = Iphone("12", "Rojo", 15000)
ip3 = Iphone("10", "Azul", 11000)
ip4 = Iphone("8", "Negro", 9000)
#
# # Cuando varios objetos tienen valores diferentes para
# # el mismo atributo, son atributos de instancia
#
# print(f"{ip1}, Marca: {ip1.get_marca()}, SO:{ip1.get_so()}")
# print(ip2.get_modelo)
# print(ip3.get_modelo)
# print(ip4.get_modelo)
#
# print(f"{ip1.get_modelo}, {ip1.get_color}, {ip1.get_precio}, {ip1.get_marca()}, {ip1.get_so()}")
# print(ip2.get_marca())
# print(ip2.get_marca())
# print(ip3.get_marca())
#
# print(ip2.get_so())
# print(ip2.get_so())
# print(ip3.get_so())
#
# # print(Iphone.mostrar_imei())
# # print(ip1.mostrar_imei())
# print(Iphone.mostrar_imei("9876543210"))
# print(ip1.mostrar_imei(1234567890))

###############################################
### Producto ###
p1 = Producto("Juguete", "Niños", 1000)
p2 = Producto("Herramienta", "Ferretería", 2000)

print(p1)
print(f"{p1}, Genérico: {p1.get_generico()}, Industrial: {Producto.tipo_industrial(False)}, Envío: {p1.get_costo_base_envio()}")
print(p2)
print(f"Genérico: {p2.get_generico()}, Industrial: {Producto.tipo_industrial(True)}, Envío: {p1.get_costo_base_envio()}")

prod_generico =Producto.get_generico()
print(prod_generico)
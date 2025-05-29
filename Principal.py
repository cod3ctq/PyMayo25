"""

str() para imprimir la información del producto

"""
from Productos import Product

prod1=Product("Cafe", "electrodomesticos", 1500)

print(prod1.obtener_nombre)
print(prod1.obtener_categoria)
print(prod1.obtener_precio)

print(Product.costo_base_envio(prod1))
"""Tenemos los precios de miles de productos.
Cada Producto tiene un precio de compra y un precio de venta
Calcular de forma vectorial, el margen de ganancia por producto"""
import numpy as np
from time import perf_counter

#Funcion tradicional
def calcula_margen(precio_compra, precio_venta):
    try:
        return round(((precio_venta-precio_compra) / precio_compra) * 100, 2)
    except ZeroDivisionError:
        return None

#Convierte la funcion tradicional en vectorial
calcular_margen_vectorial = np.frompyfunc(calcula_margen, 2, 1)

#Generar de manera simulada datos masivos
np.random.seed(50)
precios_compra = np.random.uniform(10, 100, 10000)
precio_venta = precios_compra + np.random.uniform(5, 50, 10000)

#Aplica la funcion vectorizada
margenes = calcular_margen_vectorial(precios_compra, precio_venta)
print("Precio Compra | Precio Venta | Margen (%)")
for i in range(50):
    print(f"{precios_compra[i]: >12.2f}  | {precio_venta[i]:>12.2f} | {margenes[i]:>10}")
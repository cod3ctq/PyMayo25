from time import perf_counter
import numpy as np

# habitantes_por_estado = np.array([   #manual
#     120, 305, 415, 187, 240, 320, 401, 102, 349, 277,
#     198, 432, 143, 368, 250, 411, 355, 221, 190, 405,
#     299, 134, 401, 449, 150, 390, 287, 310, 123, 330
# ])
#
# presupuesto_por_estado = np.array([
#     105000, 2300000, 1490000, 189500, 2043000, 1250000, 233000, 400000, 2450000, 1760000,
#     990000, 1100000, 2000000, 139000, 1820000, 125500, 500000, 2178000, 1650000, 300000,
#     1420000, 175000, 2490000, 212000, 1850000, 1345000, 920000, 195000, 2465000, 100000
# ])
#
# def calcular_pago (a, b):
#     return a/b
#
# # np.frompyfunc(FUNCIÓN, 2 argumentos de entrada y 1 de salida)
# calculo = np.frompyfunc(calcular_pago, 2, 1)
# print(type(calcular_pago)) # <class 'numpy.ufunc'>
# print(calcular_pago(presupuesto_por_estado, habitantes_por_estado))
#
# # Medir tiempos y performance de la ejecución
# inicio = perf_counter() # Inicia contador
# for i in range(10000):
#     calculo(presupuesto_por_estado, habitantes_por_estado)
# final = perf_counter() # Termina contador
# print("Ejecución con Numpy %0.4f" % (final - inicio))
#
# inicio_aux = perf_counter()
# lista_calculo = []
# for i in range(10000):
#     for j in range(len(habitantes_por_estado)):
#         # Añadir el resultado a una lista
#         lista_calculo.append(calcular_pago(presupuesto_por_estado[j], habitantes_por_estado[j]))
# final_aux = perf_counter()
# print("Ejecución con iteraciones %0.4f" % (final_aux - inicio_aux))
#####################################################################
"""
Tenemos los precios de miles de productos.
Cada producto tiene un precio de compra y un precio de venta
Calcular de forma vectorial el margen de ganancia por producto.
"""

def calcula_margen(precio_compra, precio_venta):
    try:
        return round(((precio_venta - precio_compra) / precio_compra) * 100, 2)
    except ZeroDivisionError:
        return None

# Convertir la función tradicional en función vectorial
calcula_margen_vectorial = np.frompyfunc(calcula_margen, 2, 1)

# Generar de manera simulada datos masivos
np.random.seed(50)
precios_compra = np.random.uniform(low=10, high=100.0, size=10000)
precios_venta = precios_compra + np.random.uniform(low=5, high=50, size=10000)

# Aplica la función vectorizada
margenes = calcula_margen_vectorial(precios_compra, precios_venta)
print(margenes)

print("Precio Compra | Precio Venta | Margen (%)")
for i in range (5):
    print(f"{precios_compra[i]:>13.2f} | {precios_venta[i]:>12.2f} | {margenes[i]:>10.2f}")
#####################################################################
"""
Tenemos miles de productos.
Cada uno tiene un precio original y un precio con descuento aplicado.
Se desea calcular, de forma vectorizada,
el porcentaje de descuento aplicado a cada producto.
"""

# Función para calcular el % de descuento
def calcula_descuento(precio_original, precio_descuento):
    try:
        return round(((precio_original - precio_descuento) / precio_original) * 100, 2)
    except ZeroDivisionError:
        return None

# Convertir la función tradicional en función vectorial
calcula_descuento_vectorial = np.frompyfunc(calcula_descuento, 2, 1)

# Generar datos simulados
np.random.seed(50)
precios_originales = np.random.uniform(low=100, high=500, size=10000)
precios_con_descuento = precios_originales - np.random.uniform(low=10, high=50, size=10000)

# Asegurarse que los precios con descuento no sean negativos, sino cero
precios_con_descuento = np.maximum(precios_con_descuento, 0)

# Aplicar función vectorizada
descuento = calcula_descuento_vectorial(precios_originales, precios_con_descuento)

# Mostrar resultados
print("Precio Original | Precio con Descuento | Descuento (%)")
for i in range(5):
    print(f"{precios_originales[i]:>15.2f} | {precios_con_descuento[i]:>20.2f} | {descuento[i]:>13.2f}")
#####################################################################
# n_scores = np.array([
#             [63, 72, 75, 51, 83],
#             [44, 53, 57, 56, 48],
#             [71, 77, 82, 91, 76],
#             [67, 56, 82, 33, 74],
#             [64, 76, 72, 63, 76],
#             [47, 56, 49, 53, 42],
#             [91, 93, 90, 88, 96],
#             [61, 56, 77, 74, 74],
# ])
# print(n_scores)
# print(n_scores.max())
# print(n_scores.max(axis=0)) # axis = 0 referencia a columnas
# print(n_scores.argmax(axis=0)) # index de los valores máximos
# print(n_scores.max(axis=1)) # axis = 1 referencia a filas
# print(n_scores.argmax(axis=1)) # index de los valores máximos
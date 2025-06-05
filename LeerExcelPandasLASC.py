import pandas as pd
import numpy as np

df = pd.read_excel("C:\\Users\\Principal\\Desktop\\ventas_10_productos.xlsx")

# 2. Separar nombres de productos y datos numéricos
productos = df['Producto'].values
datos_ventas = df.iloc[:, 1:].values  # Solo columnas de enero a diciembre

# Convertimos a un array NumPy por si fuera un objeto pandas
ventas_array = np.array(datos_ventas)

# 3. Promedio de ventas por producto
promedios = np.mean(ventas_array, axis=1)
for prod, prom in zip(productos, promedios):
    print(f"Promedio de ventas de {prod}: {prom:.2f}")

# 4. Producto con mayores ventas totales
totales = np.sum(ventas_array, axis=1)
indice_max = np.argmax(totales)
print(f"\nProducto con mayores ventas: {productos[indice_max]} ({totales[indice_max]} unidades)")

# 5. ¿Hubo alguna venta mensual mayor a 200?
ventas_mayores_200 = np.where(ventas_array > 200)
for i in range(len(ventas_mayores_200[0])):
    prod = productos[ventas_mayores_200[0][i]]
    mes = df.columns[1:][ventas_mayores_200[1][i]]
    valor = ventas_array[ventas_mayores_200[0][i], ventas_mayores_200[1][i]]
    print(f"{prod} vendió {valor} unidades en {mes}")

# 6. Diferencia mes a mes (incremento o decremento)
diferencias = np.diff(ventas_array, axis=1)
print("\nIncremento/decremento mensual por producto:")
for i, dif in enumerate(diferencias):
    print(f"{productos[i]}: {dif}")




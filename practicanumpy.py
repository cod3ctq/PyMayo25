import numpy as np

array1 = np.array([1,2,3,4,5,6,7,8,9,10])
array2 = np.array([10,20,30,40,50,60,70,80,90,100])
array3 = np.array([10,20,10,30,40,10,50,60,70,10,80,90,10,100])

#print("Arreglo 1", array1)
#print("Arreglo 2", array2)


matriz1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

#print("Matriz 1", matriz1)

"""
Operaciones
"""

print("Suma:", array1 + array2)
print("Multiplicacion:", array1 * array2)
print("Promedio:", np.mean(array2))
print("Raiz Cuadrada:", np.sqrt(array2))
print("Media: ", np.median(array2))
print("Desviación estandar: ", np.std(array2))


print(np.arange(0,25))
print(np.arange(0,25))

matriz_2 = np.reshape(array2,(2,5))
matriz_1 = array1.reshape(5,2)
print(str(matriz_1))

array_grande = np.dot(matriz_1,matriz_2)
print(str(array_grande))

print(array_grande[3,3]) #acceder a partes de un array
print(array_grande[:,1]) #Corte al eje X
print(array_grande[2,:]) #Corte al eje Y

n1 = np.append(array1,5000) # agregar un nuevo elemento al final

print(n1)

n2 = np.insert(array2,5,777)

print(n2)

n3 = np.delete(array2,5)

print(n3)

# BUSQUEDA Y FILTROS
# where devuelve los numeros que cumplen la condición

duplicados = np.where(array3==10)
print(duplicados)

pares = np.where(array3%3==0)
print(pares)

menores_que = np.where(array3<70)
print("Valores menores que 70:",menores_que)

valores_en_rango = np.where((array3>30) & (array3<100))
print("Valores en rango:",valores_en_rango)



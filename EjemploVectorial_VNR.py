import numpy as np


def calcular_ahorro(ahorro_grupal, total_alumnos):
    try:
        return round((ahorro_grupal / total_alumnos),2)
    except ZeroDivisionError:
        return None


#Convertir a vectorial

ahorro_individual = np.frompyfunc(calcular_ahorro, 2, 1)
np.random.seed(30)
total_alumnos = np.random.uniform(low=1, high=30, size=30)
ahorro_grupal = np.random.uniform(low=1000, high=5500, size=30)

ahorro_por_alumno = ahorro_individual(ahorro_grupal, total_alumnos)
print("Ahorro grupal"  , "Alumnos"  , "Ahorro Individual")
for i in range(30):
    print(f"{ahorro_grupal[i]:>9.2f} , {total_alumnos[i]:>7.0f} , {ahorro_por_alumno[i]:>9.2f}")


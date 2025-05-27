import csv
from pickle import TUPLE

mayores_de_cincuenta = []
mujeres_oax=[]

with open("C:\\Users\\barbi\\Desktop\\lectura.csv","r",encoding="utf8") as archivo_lectura:
    lineas = csv.reader(archivo_lectura)
    print(type(lineas)) #el tipo de dato de la variable
    for contador,linea in enumerate(lineas):
        if contador>0:
            print(linea)
            #Filtro de todas las personas >= 50
            if int(linea[2]) >= 50:
                mayores_de_cincuenta.append(linea)
                print("MAYORES DE CINCUENTA:")
            for value in mayores_de_cincuenta:
                print(value)
#Filtrar solo mujeres (SEXO = 'F') de Oaxaca.

        if linea[1] == 'Oaxaca' and linea[3]=='F':
            mujeres_oax.append(linea)
            for value in mujeres_oax:
                print(value)
                




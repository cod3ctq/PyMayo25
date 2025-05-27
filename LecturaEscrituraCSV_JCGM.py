#Leer datos desde un csv
import csv
sonorenses = []
with open("C:\\Users\\Bodok\\Downloads\\Herramientas CETEQ Curso\\Ejercicios\\lectura.csv","r", encoding="utf8") as archivo_lectura:
    lineas = csv.reader(archivo_lectura)
    #print(type(lineas)) #el tipo de dato de la variable
    for linea in lineas:
        print(linea)
        #Imprimir nombre y celular
        if(linea[1]=='Sonora'):
            sonorenses.append(linea)

print("------------------------")
for value in sonorenses:
    print(value)

#Escribir datos en un archivo
with open("C:\\Users\\Bodok\\Downloads\\Herramientas CETEQ Curso\\Ejercicios\\escritura.csv", "w",newline='') as archivo_escritura:
    escritor = csv.writer(archivo_escritura)
    for value in sonorenses:
        escritor.writerow(value)
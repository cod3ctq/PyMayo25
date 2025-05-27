# Leer datos desde un CSV
import csv

# ['NOMBRE', 'ESTADO_ORIGEN', 'EDAD', 'SEXO', 'NUM_CELULAR']
mayor_50 = []
mujeres_oaxaca = []
hombres_leon = []
cel_554 = []
with (open("C:\\Users\\adolf\\Documents\\173-May25\\colecciones\\practicas\\lectura.csv", "r", encoding="utf-8")
      as archivo_lectura):
    lineas = csv.reader(archivo_lectura)
    # print(type(lineas))
    # next(lineas)
    for count, linea in enumerate(lineas): # imprimir contenido completo
    #     print(linea)
        if count > 0:
            # imprimir mayores de 50
            linea[2] = int(linea[2])
            if linea[2] > 50:
                mayor_50.append(linea)
            # Mujeres de Oaxaca
            if (linea[1] == "Oaxaca") and (linea[3] == "F"):
                mujeres_oaxaca.append(linea)
            # Hombres 25 y 40 de Nuevo León
            if (linea[1] == "Nuevo León") and (linea[3] == "M") and (41 > linea[2] > 24):
                hombres_leon.append(linea)
            # Celulares inician 554
            if linea[4].startswith("554"):
                cel_554.append(linea)




print("Personas mayores de 50 años.")
for value in mayor_50:
    print(value)
print("###################################################")
print("Mujeres de Oaxaca.")
for value in mujeres_oaxaca:
    print(value)
print("###################################################")
print("Hombres 25 y 40 de Nuevo León.")
for value in hombres_leon:
    print(value)
print("###################################################")
print("Celulares empezando con ""554"".")
for value in cel_554:
    print(value)
print("###################################################")
print("Personas de Veracruz, Oaxaca, Puebla")

# Escribir datos en un archivo csv
# with (open("C:\\Users\\adolf\\Documents\\173-May25\\colecciones\\practicas\\escritura.csv", "w", newline="")
#       as archivo_escritura):
#     write = csv.writer(archivo_escritura)
#     for value in sonorenses:
#         write.writerow(value)
#############################
# Filtrar todas las personas mayores de 50 años.
# Filtrar solo mujeres (SEXO = 'F') de Oaxaca.
# Filtrar hombres entre 25 y 40 años de Nuevo León.
# Filtrar personas cuyo número de celular comienza con 554.
# Crear un mapa con todas las personas de solo los siguientes estados:
# Veracruz, Oaxaca, Puebla
# Lista de estados que queremos incluir
# estados_deseados = {"Veracruz", "Oaxaca", "Puebla"}
#
# # Diccionario para almacenar personas por estado
# mapa_personas = {
#     "Veracruz": [],
#     "Oaxaca": [],
#     "Puebla": []
# }
#
# # Abrimos y leemos el archivo
# with open("lectura.csv", "r", encoding="utf-8") as archivo:
#     next(archivo)  # Saltar encabezado
#     for linea in archivo:
#         nombre, estado, edad, sexo, celular = linea.strip().split(",")
#         if estado in estados_deseados:
#             mapa_personas[estado].append({
#                 "nombre": nombre,
#                 "edad": int(edad),
#                 "sexo": sexo,
#                 "celular": celular
#             })
#
# # Mostrar resultados
# for estado, personas in mapa_personas.items():
#     print(f"\n✅ {estado} ({len(personas)} personas)")
#     for persona in personas:
#         print(f"- {persona['nombre']}, {persona['edad']} años, {persona['sexo']}")

"""
Filtrar todas las personas mayores de 50 años.
Filtrar solo mujeres (SEXO = 'F') de Oaxaca.
Filtrar hombres entre 25 y 40 años de Nuevo León.
Filtrar personas cuyo número de celular comienza con 554.
Crear un mapa con todas las personas de solo los siguentes estados:
Veracruz, Oaxaca, Puebla

NOMBRE	ESTADO_ORIGEN	EDAD	SEXO	NUM_CELULAR

"""
import csv

# leer archivo CSV
with open("C:\\Users\\Principal\\Desktop\\lectura.csv", newline='', encoding='utf-8') as archivo_lectura:
    lector = csv.DictReader(archivo_lectura)
    datos = list(lector)
"""

for contador, linea in enumerate(lineas):
    if contador>0:
    if(linea[2]>50:)
    

"""
# Convertir edades a enteros para comparaciones
for persona in datos:
    persona['EDAD'] = int(persona['EDAD'])

# 1. Personas mayores de 50 años
mayores_50 = [p for p in datos if p['EDAD'] > 50]
print("Mayores de 50 años:")
for p in mayores_50:
    print(p)
print()

# 2. Mujeres de Oaxaca
mujeres_oaxaca = [p for p in datos if p['SEXO'] == 'F' and p['ESTADO_ORIGEN'] == 'Oaxaca']
print("Mujeres de Oaxaca:")
for p in mujeres_oaxaca:
    print(p)
print()

# 3. Hombres entre 25 y 40 años de Nuevo León
hombres_nl = [
    p for p in datos
    if p['SEXO'] == 'M' and p['ESTADO_ORIGEN'] == 'Nuevo León' and 25 <= p['EDAD'] <= 40
]
print("Hombres de 25 a 40 años de Nuevo León:")
for p in hombres_nl:
    print(p)
print()

# 4. Teléfonos que comienzan con 554
tel_554 = [p for p in datos if p['NUM_CELULAR'].startswith('554')]
print("Teléfonos que comienzan con 554:")
for p in tel_554:
    print(p)
print()

# 5. Mapa HTML con personas de Veracruz, Oaxaca y Puebla (ubicaciones aproximadas)
ubicaciones = {
    "Veracruz": [19.1738, -96.1342],
    "Oaxaca": [17.0732, -96.7266],
    "Puebla": [19.0414, -98.2063]
}

estados_mapa = ["Veracruz", "Oaxaca", "Puebla"]
personas_mapa = [p for p in datos if p['ESTADO_ORIGEN'] in estados_mapa]

# Crear archivo HTML
with open("personas_mapa.html", "w", encoding="utf-8") as mapa:
    mapa.write("""
<!DOCTYPE html>
<html>
<head>
    <title>Mapa de Personas</title>
</head>
<body>
    <h2>Personas en Veracruz, Oaxaca y Puebla</h2>
    <ul>
""")
    for persona in personas_mapa:
        estado = persona['ESTADO_ORIGEN']
        lat, lon = ubicaciones[estado]
        mapa.write(f"""
        <li>
            {persona['NOMBRE']} - {estado} <br>
            <a href="https://www.google.com/maps?q={lat},{lon}" target="_blank">Ver en mapa</a>
        </li>
""")
    mapa.write("""
    </ul>
</body>
</html>
""")
print("📍 Mapa generado como 'personas_mapa.html'")


with open("Datos_prueba.csv", "r", encoding='utf-8') as file:
    contenido = file.read()

# Escribe el contenido en un nuevo archivo en UTF-8
with open("Datos_prueba_utf8.csv", "w", encoding="utf-8") as file_utf8:
    file_utf8.write(contenido)
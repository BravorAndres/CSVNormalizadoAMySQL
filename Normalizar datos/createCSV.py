"""Modulo para crear nuevo csv con los datos normalizados

"""

import csv

def escribirCSV(datos, nombreArchivo):
    """Escribe los datos de los clientes en un nuevo csv, reemplaza posibles archivos existentes con el mismo nombre

        Args:
            datos (list of dict): Diccionario con los datos de los clientes.
            nombre_archivo (str): Nombre que recibirá el nuevo archivo CSV. 
    """
    with open(nombreArchivo, mode='w', newline='', encoding='utf-8') as file:

        campos = datos[0].keys()
        escritor_csv = csv.DictWriter(file, fieldnames=campos)
        escritor_csv.writeheader()
        escritor_csv.writerows(datos)


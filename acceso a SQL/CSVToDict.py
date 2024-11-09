"""Modulo para leer el clientes_normalizados y colocarlos en una lista de diccionarios
"""

import csv



def leerCSV(rutaCSV):
    clientes = []
    with open(rutaCSV, mode='r', newline='', encoding='latin-1') as file:
        lector_csv = csv.DictReader(file)
        for fila in lector_csv:
            cliente = {
                'Nombre': (fila['Nombre']),
                'Apellido': (fila['Apellido']),
                'Email': fila['Email'],
                'Telefono': fila['Telefono'],
                'Fecha_registro': fila['FechaRegistro']
            }
            clientes.append(cliente)
    return clientes


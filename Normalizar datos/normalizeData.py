"""Modulo para normalizar los datos de los clientes, capitalizar nombre, validar correos electronicos, dar
    formato estandar a los numeros telefonicos y fechas
"""

import re

from datetime import datetime


def normalizarTelefono(numero):
    """Estándar para números de Colombia:  XXX XXX XXX
    """

    if re.match(r'^\d{9}$', numero):
        return f"{numero[:3]} {numero[3:6]} {numero[6:]}"
    return None


def validarEmail(email):
    """validar formato de correo electronico 
    """
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if (re.match(patron, email)):
        return email
    return None


def normalizarFecha(fecha):
    """Normaliza las fechas a formato yyyy-mm-dd
    """

    formatos = ["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y"]  
    for formato in formatos:
        try:
            fecha_obj = datetime.strptime(fecha, formato)
            return fecha_obj.strftime("%Y-%m-%d")
        except ValueError:
            continue
    print(f"Formato de fecha no válido: {fecha}")
    return None  


def normalizarDatos(data):
    """Normaliza los datos de los cliente

        Args:
            datos (): Diccionario con los datos de los clientes.
             
    """

    clientes = []

    for cliente in data:
       # print(f" {cliente} \n")
        nombre = cliente['Nombre'].capitalize()
        apellido = cliente['Apellido'].capitalize()
        email = validarEmail(cliente['Email'])
        telefono = normalizarTelefono(cliente['Telefono'])
        fecha = normalizarFecha(cliente['FechaRegistro'])

        clientes.append({
            'Nombre': nombre,
            'Apellido': apellido,
            'Email': email,
            'Telefono': telefono,
            'FechaRegistro': fecha
        })
    return clientes
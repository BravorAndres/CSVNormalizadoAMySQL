"""Operaciones crus sobre la tabla clientes de la base de datos
"""

from app.DBConection import conectar, cerrarConexion
from app.models import Cliente
from app.schemas import clienteCreate

def getAllClientes():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    cerrarConexion(conn)
    return clientes

def getClienteByEmail(email: str):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes WHERE email = %s", (email,))
    cliente = cursor.fetchone()
    cursor.close()
    cerrarConexion(conn)
    return cliente

def insertarCliente(cliente: clienteCreate):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO clientes (nombre, apellido, email, telefono, fecha_registro)
        VALUES (%s, %s, %s, %s, NOW())
    """, (cliente.nombre, cliente.apellido, cliente.email, cliente.telefono))
    conn.commit()
    cursor.close()
    cerrarConexion(conn)
    return cursor.lastrowid

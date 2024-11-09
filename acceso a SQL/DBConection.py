import mysql.connector
from mysql.connector import Error
import configparser

def conectar():
    """Modulo para crear conexion a MySql con mysql-connector-python
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        conexion = mysql.connector.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            database=config['mysql']['database']
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error de conexión a MySQL: {e}")
        return None

def cerrarConexion(conexion):
    if conexion and conexion.is_connected():
        conexion.close()

# a,b = conectar()
# print(a,b)
# cerrarConexion(a)
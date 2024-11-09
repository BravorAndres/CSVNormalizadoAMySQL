"""Define funciones para las operaciones que se realizan en la base de datos, por ejemplo, 
    crear una tabla y cargar los datos del CSV:
"""

from DBConection import conectar, cerrarConexion

def crearTabla():
    """Crea tabla con una tabla clientes en la base de datos, con los siguientes atributos:
        id(autoincremental), nombre, apellido,email,telefono,fecha_registro
    """
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50),
                apellido VARCHAR(50),
                email VARCHAR(100),
                telefono VARCHAR(20),
                fecha_registro DATE
            )
        """)
        conexion.commit()
        cursor.close()
        cerrarConexion(conexion)


def insertarCliente(cliente):
    '''Inserta nuevo cliente en la base de datos cliente
    '''
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO clientes (nombre, apellido, email, telefono, fecha_registro)
            VALUES (%s, %s, %s, %s, %s)
        """, (cliente['Nombre'], cliente['Apellido'], cliente['Email'], cliente['Telefono'], cliente['Fecha_registro']))
        conexion.commit()
        cursor.close()
        cerrarConexion(conexion)


def consultarClientesPorcadaAño():
    """Devuelve el numero de clientes que se registraron en cada año
    """

    conexion = conectar()

    cursor = conexion.cursor()
    
    # Consulta SQL para contar clientes por año de registro
    consulta = """
        SELECT YEAR(fecha_registro) AS año, COUNT(*) AS numero_clientes
        FROM clientes
        GROUP BY año
        ORDER BY año;
    """
    
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    
    # Cerrar cursor y conexión
    cursor.close()
    cerrarConexion(conexion)
    #print(resultados)
    return resultados

def consultarPorAño(año):
    """Devuelve el número de clientes que se registraron en un año específico.
        Args:  
            año(int): Año que se desea consultar
    """
    conexion = conectar()
    cursor = conexion.cursor()
    
    # Consulta SQL para contar clientes en un año específico
    consulta = """
        SELECT COUNT(*) AS numero_clientes
        FROM clientes
        WHERE YEAR(fecha_registro) = %s;
    """
    
    cursor.execute(consulta, (año,))
    resultado = cursor.fetchone()
    
    # Cerrar cursor y conexión
    cursor.close()
    cerrarConexion(conexion)
    
    # Devuelve el número de clientes registrados en el año especificado
    numero_clientes = resultado[0] if resultado else 0
    return numero_clientes
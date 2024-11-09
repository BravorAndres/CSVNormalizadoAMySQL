"""Modulo principal, lee y guarda en la base de datos los clientes del archivo clientes_normalizados
"""

from DBOperations import crearTabla,insertarCliente,consultarClientesPorcadaAño,consultarPorAño
from CSVToDict import leerCSV

def main():
    crearTabla()  # Crea la tabla en caso de que no exista
    clientes = leerCSV('clientes_normalizados.csv')
    for cliente in clientes:
        insertarCliente(cliente)
    print("Datos cargados exitosamente.")
    print(f"Clietes registrados por cada año: {consultarClientesPorcadaAño()}")
    print(f"\nClientes registrado en el año 2022:{consultarPorAño(2022)}")


if __name__ == '__main__':
    main()

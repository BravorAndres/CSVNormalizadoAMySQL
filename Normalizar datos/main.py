
"""Modulo principal, ejecuta en secuencia los script para que se lean, normalicen y 
    guarden los datos de los clientes
"""

from CSVtoDict import CSVToDictionary
from normalizeData import normalizarDatos
from createCSV import escribirCSV


data = CSVToDictionary()
clientes = normalizarDatos(data)
escribirCSV(clientes,'clientes_normalizados.csv.')
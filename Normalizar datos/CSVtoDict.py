
import csv
import unicodedata
import chardet

def normalizarClave(clave):
    """Elimina tildes y convienrte a ASCII 
    """

    
    clave = unicodedata.normalize('NFD', clave).encode('ascii', 'ignore').decode('utf-8')
    clave = clave.replace(" ", "_")
   
    if (clave.lower() == 'telifono') or (clave.lower() == 'telfono') :
        clave = 'Telefono'

    return clave


def CSVToDictionary():
    """Lee el archivo csv de clientes y lo tranforma a una lista de diccionarios.
    """

    with open('Datos_prueba.csv', mode='r', newline='', encoding='utf-8') as file:
        lector_csv = csv.DictReader(file)
       # datos = [fila for fila in lector_csv

        #Normaliza claves del diccionario
        datos = [{normalizarClave(clave): valor for clave, valor in fila.items()} for fila in lector_csv]
    print(datos)
   
    return datos





# Escript para leer normalizar datos de clientes almacenados en un archivo csv


## Requerimientos

Python 3.11 o superior

## Formato del Archivo CSV de Origen

El archivo de origen `Datos_prueba.csv` debe tener el siguiente formato, con los datos delimitados por coma (`,`):

```
Nombre,Apellido,Email,Tel�fono,FechaRegistro
Juan,P�rez,juan.perez@email.com,612345678,2023-08-15
Mar�a,G�mez,maria.gomez@email.com,613456789,2023-09-10
Carlos,L�pez,carlos.lopez@email.com,614567890,2023-07-05
```

### Archivos de Script

- `CSVToDict.py`: Lee los datos del archivo `Datos_prueba.csv` y los retorna una lista de diccionarios con los datos de los clientes.
- `normalizeData.py`: Normaliza los datos de los clieten, capitaliza los nombres, alida los correo.
- `createCSV`: Crea un nuevo archivo llamado `clientes_normalizados.csv` con los datos normalizados de los clientes.
- `main.py`: Ejecuta en orden las tareas de leer el archivo csv, normalizar los datos de los clientes y guardarlos en el nuevo archivo



**Autor**: Leider Andres Bravo  
**Versión**: 1.0

# Accesos a la base de datos

## Configuración de la Base de Datos MySQL

Crear una base de datos llamada `clientes` creada en tu servidor MySQL. Si no la has creado, puedes utilizar el siguiente comando SQL:

```sql
CREATE DATABASE Clientes;
```

## Creación de la Tabla `clientes`

No es ecesario crear la tabla `clientes`, el script se encarga de ello en caso de que no este creada. En caso de que sea necesario crearla antes de se puede utilizar el sigueinte script sql: 

```sql
CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50),
                apellido VARCHAR(50),
                email VARCHAR(100),
                telefono VARCHAR(20),
                fecha_registro DATE
            )
```

## Descripción de Archivos

### Archivos de Script

- `CSVToDict.py`: Lee los datos del archivo `clientes_Normalizados.csv` y retorna una lista de diccionarios con los datos de los clientes.
- `DBContection.py`: Configura la conexion entre el script y la base de datos.
- `DBOperations`: Configura las operaciones, como consultas y instersion de clientes a ala base de datos.
- `config.ini`: Contien las configuraciones de host y usuario y contraseñas para acceder a la base de datos.        > ⚠️ **Atención**: se debe modificar este archivo segun la confugracion del motor de base de datos utilizado.
- `main.py`: Ejecuta en orden las tareas de leer el archivo csv, cargar los datos de los clientes y realizar consultas por año a la base de datos. 

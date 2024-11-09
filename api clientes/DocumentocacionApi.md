# Documentación de la API de Clientes

Esta API permite interactuar con la base de datos de clientes, incluyendo la consulta de todos los clientes, la búsqueda de clientes por correo electrónico y la adición de nuevos clientes.

## Base URL

La URL base para todas las solicitudes es `http://127.0.0.1:8000`.

## ¿Como levantar la api?

Se debe tener instalado python 3.11 o superior.

Dentro de la ruta `api clientes` ejecutar

```bash
  python -m venv venv
  .\venv\Scripts\activate
```

instalar dependencias

```bash
  pip install -r requirements.txt
```

Y levantar la aplicacion

```bash
  uvicorn app.main:app --reload
```


## Endpoints

### 1. Obtener todos los clientes

- **URL**: `/clientes`
- **Método**: `GET`
- **Descripción**: Devuelve todos los registros de la tabla de clientes.

#### Ejemplo de solicitud

```bash
curl -X GET "http://127.0.0.1:8000/clientes"
```

#### Ejemplo de respuesta

```json
[
  {
    "id": 22,
    "nombre": "Juan",
    "apellido": "Pï¿½rez",
    "email": "juan.perez@email.com",
    "telefono": "612 345 678",
    "fecha_registro": "2023-08-15"
  },
  {
    "id": 23,
    "nombre": "Marï¿½a",
    "apellido": "Gï¿½mez",
    "email": "maria.gomez@email.com",
    "telefono": "613 456 789",
    "fecha_registro": "2023-09-10"
  }
]
```

### 2. Obtener un cliente por correo electrónico

- **URL**: `/clientes/{email}`
- **Método**: `GET`
- **Descripción**: Devuelve la información de un cliente específico por su correo electrónico.
- **Parámetro de URL**:
  - `email` (string, requerido): Correo electrónico del cliente que deseas consultar.

#### Ejemplo de solicitud

```bash
curl -X GET "http://127.0.0.1:8000/clientes/bhima@me.com"
```

#### Ejemplo de respuesta exitosa

```json
  {
  "id": 23,
  "nombre": "Marï¿½a",
  "apellido": "Gï¿½mez",
  "email": "maria.gomez@email.com",
  "telefono": "613 456 789",
  "fecha_registro": "2023-09-10"
}
```

#### Ejemplo de respuesta cuando el cliente no se encuentra

```json
{
  "detail": "Cliente no encontrado"
}
```

### 3. Agregar un nuevo cliente

- **URL**: `/clientes`
- **Método**: `POST`
- **Descripción**: Permite agregar un nuevo cliente a la base de datos, recibiendo datos en formato JSON.
- **Cuerpo de la solicitud** (JSON):
  - `ID` (string, requerido): ID único del cliente,
  - `nombre`(string, requerido): nombre del nuevo cliente,
  - `apellido`(string, requerido): apellido del nuevo cliente,
  - `email`(string, requerido): email del nuevo cliente,
  - `telefono`(string, requerido): nuemero de telefono del nuevo cliente,


#### Ejemplo de solicitud

```bash
curl -X POST "http://127.0.0.1:8000/clientes" -H "Content-Type: application/json" -d '{
      "nombre": "nicolas",
      "apellido": "bravo",
      "email": "nicolas.bravo@gmail.com",
      "telefono": "673564982"
}'
```


#### Ejemplo de respuesta cuando ocurre un error

```json
{
  "detail": "Error al insertar el cliente"
}
```

## Errores Comunes

- **404 Not Found**: El cliente especificado por el correo electrónico no se encuentra en la base de datos.
- **400 Bad Request**: Error al intentar insertar el cliente (por ejemplo, ID duplicado o datos inválidos).
- **500 Internal Server Error**: Error al conectar con la base de datos.

## Notas

- El endpoint `/clientes/{email}` requiere que el correo electrónico sea exacto y no es sensible a mayúsculas/minúsculas.
- El campo `Fecha_Registro` en la base de datos se configura automáticamente y no se requiere en el cuerpo del POST.

---

**Autor**: Leider Andres Bravo
**Versión**: 1.0

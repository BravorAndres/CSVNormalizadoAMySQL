"""Define los esquemas de datos para validar las peticiones y respuestas de la API.
"""

from pydantic import BaseModel
from datetime import date

class clienteCreate(BaseModel):
    """Creacion de un nuevo cliente, define"""
    nombre: str
    apellido: str
    email: str
    telefono: str

class clienteOut(BaseModel):
    """Consulta de un cliente"""
    id: int
    nombre: str
    apellido: str
    email: str
    telefono: str
    fecha_registro: date


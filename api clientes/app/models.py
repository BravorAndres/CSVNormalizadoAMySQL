"""Modelos que utiliza la api para conectarse a la base de datos a travez de mysql-connector-python
"""


from pydantic import BaseModel
from typing import Optional
from datetime import date

class Cliente(BaseModel):
    id: Optional[int]
    nombre: str
    apellido: str
    email: str
    telefono: str
    fecha_registro: Optional[date] = None

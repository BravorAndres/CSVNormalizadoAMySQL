"""Modulo con las rutas de acceso para la api
"""

from typing import List
from fastapi import APIRouter, HTTPException, logger
from app.crud import getAllClientes,getClienteByEmail,insertarCliente
from app.schemas import clienteCreate, clienteOut


router = APIRouter()

@router.get("/clientes", response_model=List[clienteOut])
async def read_clientes():
    print(f"\nen la funcion read clientes")
    clientes = getAllClientes()
    return clientes

@router.get("/clientes/{email}", response_model=clienteOut)
async def read_cliente(email: str):
    print(f"\nen la funcion read clientes por email")
    cliente = getClienteByEmail(email)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return cliente

@router.post("/clientes", response_model=int)
async def create_cliente(cliente: clienteCreate):
    print(f"\nen la funcion crear cliente nuevo")
    cliente_id = insertarCliente(cliente)  # Llama a la función que inserta el cliente
    return cliente_id

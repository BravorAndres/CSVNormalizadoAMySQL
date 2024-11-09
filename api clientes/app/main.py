"""modulo principal de la api clientes
"""

from fastapi import FastAPI
from app.routes import router
app = FastAPI()

app.include_router(router)
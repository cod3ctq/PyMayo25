from app.db.database import Base, engine
from app.models.producto import Producto
from app.models.departamento import Departamento
from fastapi import FastAPI
from app.db.database import engine, Base
from app.models.producto import Producto
from app.models.departamento import Departamento
from app.routers import productos

# Crear las tablas si no existen
# Base.metadata.create_all(bind=engine)

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API de productos con FastAPI y Oracle"}

app.include_router(productos.router)


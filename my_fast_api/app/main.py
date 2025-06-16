from fastapi import FastAPI

from app.db.database import Base, engine_mysql
from app.models.departamento import Departamento
from app.models.producto import Producto
from app.routers import productos


app = FastAPI()
Base.metadata.create_all(engine_mysql)


@app.get("/")
def root():
    return {"message": "Api de Productos con Fastapi y mysql"}

app.include_router(productos.router)
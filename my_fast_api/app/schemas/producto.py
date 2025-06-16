from pydantic import BaseModel
from datetime import date
from typing import Optional
from app.schemas.departamento import DepartamentoRead

class ProductoCreate(BaseModel):
    nombre: str
    fecha_cad: Optional[date]
    precio_compra: float
    precio_venta: float
    depto_id: int

class ProductoRead(BaseModel):
    producto_id: int
    nombre: str
    fecha_cad: Optional[date]
    precio_compra: float
    precio_venta: float
    departamento: DepartamentoRead

class Config:
    orm_mode = True



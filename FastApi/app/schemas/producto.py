from pydantic import BaseModel
from datetime import date
from typing import Optional
from app.schemas.departamento import DepartamentoRead

# Para crear un producto
class ProductoCreate(BaseModel):
    producto_id: int
    nombre: str
    fecha_cad: Optional[date]
    precio_compra: float
    precio_venta: float
    depto_id: int

# Para leer un producto
class ProductoRead(BaseModel):
    producto_id: int
    nombre: str
    fecha_cad: Optional[date]
    precio_compra: float
    precio_venta: float
    departamento: DepartamentoRead  # Relación cargada

    class Config:
        from_attributes = True

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.producto import Producto
from app.schemas.producto import ProductoCreate, ProductoRead
from app.db.database import Session
from app.services import producto_service

router = APIRouter(prefix="/productos", tags=["productos"])

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[ProductoRead])
def listar_productos(db: Session = Depends(get_db)):
    return producto_service.get_all_productos(db)

@router.get("/{producto_id}", response_model=ProductoRead)
def obtener_productos(producto_id: int, db: Session = Depends(get_db)):
    producto = producto_service.get_producto_by_id(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/", response_model=ProductoRead)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return producto_service.create_producto(db, producto)


@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    ok = producto_service.delete_producto(db, producto_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"ok": True}
@router.get("/buscar/", response_model=List[ProductoRead])
def buscar_por_nombre_y_precio (nombre: str,precio_min: float, precio_max: float, db: Session = Depends(get_db)):
    return producto_service.get_productos_by_name_and_price_range(db, nombre, precio_min, precio_max)

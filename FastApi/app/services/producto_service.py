from sqlalchemy.orm import Session
from app.models.producto import Producto
from app.schemas.producto import ProductoCreate
from typing import List
from app.exceptions.http_exceptions import (
    producto_no_encontrado_exception,
    producto_existente_exception,
    error_crear_producto_exception,
    error_eliminar_producto_exception
)

def get_all_productos(db: Session) -> List[Producto]:
    return db.query(Producto).all()

def get_producto_by_id(db: Session, producto_id: int) -> Producto:
    producto = db.query(Producto).filter(Producto.producto_id == producto_id).first()
    if not producto:
        raise producto_no_encontrado_exception()
    return producto

def create_producto(db: Session, producto: ProductoCreate) -> Producto:
    try:
        # Verificación opcional: evitar duplicados por nombre
        producto_existente = db.query(Producto).filter(Producto.nombre == producto.nombre).first()
        if producto_existente:
            raise producto_existente_exception()

        db_producto = Producto(**producto.dict())
        db.add(db_producto)
        db.commit()
        db.refresh(db_producto)
        return db_producto
    except Exception:
        raise error_crear_producto_exception()
def delete_producto(db: Session, producto_id: int) -> bool:
    producto = db.query(Producto).filter(Producto.producto_id == producto_id).first()
    if not producto:
        raise producto_no_encontrado_exception()
    try:
        db.delete(producto)
        db.commit()
        return True
    except Exception:
        raise error_eliminar_producto_exception()

def get_productos_by_name_and_price_range(db: Session, name: str, min_price: float, max_price: float) -> List[Producto]:
    return db.query(Producto).filter(
        Producto.nombre.contains(name),
        Producto.precio_venta >= min_price,
        Producto.precio_venta <= max_price
    ).all()

from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Producto(Base):
    __tablename__ = "PRODUCTOS"

    producto_id = Column('PRODUCTO_ID',Integer, primary_key=True, index=True)
    nombre = Column('NOMBRE',String(100), nullable=False)
    fecha_cad = Column('FECHA_CAD',Date)
    precio_compra = Column('PRECIO_COMPRA',Float, nullable=False)
    precio_venta = Column('PRECIO_VENTA',Float, nullable=False)
    refrigerado = Column('REFRIGERADO',String(1), nullable=False)
    depto_id = Column('DEPTO_ID',Integer, ForeignKey("DEPARTAMENTO.DEPTO_ID"), nullable=False)

    departamento = relationship("Departamento", backref="productos")
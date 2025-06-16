from sqlalchemy import create_engine, Column, Integer, ForeignKey, String, Numeric, Date, Float
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

from app.db.database import Base

class Producto(Base):
    __tablename__ = 'productos'

    producto_id = Column('producto_id', Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column('nombre',String(100), nullable=False)
    fecha_cad = Column('FECHA_CAD',Date)
    precio_compra = Column('PRECIO_COMPRA',Float, nullable=False)
    precio_venta = Column('PRECIO_VENTA',Float, nullable=False)
    depto_id = Column("DEPTO_ID",Integer, ForeignKey("departamento.DEPTO_ID"), nullable=False)
    departamento = relationship("Departamento", backref="productos")

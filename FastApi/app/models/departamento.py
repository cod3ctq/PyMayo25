from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base

class Departamento(Base):
    __tablename__ = "DEPARTAMENTO"

    depto_id = Column('DEPTO_ID',Integer, primary_key=True, index=True)
    nombre = Column('NOMBRE',String(100), unique=True, nullable=False)
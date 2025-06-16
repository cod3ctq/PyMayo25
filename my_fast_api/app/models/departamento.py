import mysql.connector
from sqlalchemy import create_engine, Column, Integer, ForeignKey, String, Numeric, Date
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

from app.db.database import Base


class Departamento(Base):
    __tablename__ = 'departamento'
    id = Column('DEPTO_ID',Integer, primary_key=True, index=True)
    nombre = Column('NOMBRE',String(100), unique=True, nullable=False)

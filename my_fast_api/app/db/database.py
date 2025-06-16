import mysql.connector
from sqlalchemy import create_engine, Column, Integer, ForeignKey, String, Numeric, Date
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

database_url_mysql = "mysql+mysqlconnector://root:admin@localhost:3306/tienda"

engine_mysql = create_engine(database_url_mysql)

Session = sessionmaker(bind=engine_mysql)
session = Session()

Base = declarative_base()

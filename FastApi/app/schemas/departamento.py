from pydantic import BaseModel

# Para crear un departamento
class DepartamentoCreate(BaseModel):
    nombre: str

# Para leer un departamento
class DepartamentoRead(BaseModel):
    depto_id: int
    nombre: str

    class Config:
        from_attributes = True

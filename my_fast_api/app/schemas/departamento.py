from pydantic import BaseModel

class DepartamentoCreate(BaseModel):
    nombre: str

class DepartamentoRead(BaseModel):
    id: int
    nombre: str
    class Config:
        orm_mode = True

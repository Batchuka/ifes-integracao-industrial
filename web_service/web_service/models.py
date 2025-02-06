from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class DataSourceBase(BaseModel):
    nome: str
    tipo: str  # Exemplo: "modbus_tcp"
    host: str
    porta: int

class DataPointBase(BaseModel):
    datasource_id: int
    nome: str
    endereco: int  # O endereço do registrador Modbus
    unidade: Optional[str] = None  # Exemplo: "°C", "%", "bar"

class RegistroBase(BaseModel):
    datapoint_id: int
    valor: float
    timestamp: datetime

class DataSourceCreate(DataSourceBase):
    pass

class DataSource(DataSourceBase):
    id: int
    criado_em: datetime

    class Config:
        orm_mode = True  # Permite integração com SQLAlchemy

class DataPointCreate(DataPointBase):
    pass

class DataPoint(DataPointBase):
    id: int
    criado_em: datetime

    class Config:
        orm_mode = True

class RegistroCreate(RegistroBase):
    pass

class Registro(RegistroBase):
    id: int

    class Config:
        orm_mode = True

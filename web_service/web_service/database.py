from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DATABASE_URL = "sqlite:///./modbus_data.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class DataSource(Base):
    __tablename__ = "datasources"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    tipo = Column(String, nullable=False)  # Exemplo: "modbus_tcp"
    host = Column(String, nullable=False)
    porta = Column(Integer, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)

    datapoints = relationship("DataPoint", back_populates="datasource")


class DataPoint(Base):
    __tablename__ = "datapoints"

    id = Column(Integer, primary_key=True, index=True)
    datasource_id = Column(Integer, ForeignKey("datasources.id"))
    nome = Column(String, nullable=False)
    endereco = Column(Integer, nullable=False)  # O endereço Modbus do registrador
    unidade = Column(String, nullable=True)  # Exemplo: "°C", "%", "bar"
    criado_em = Column(DateTime, default=datetime.utcnow)

    datasource = relationship("DataSource", back_populates="datapoints")
    registros = relationship("Registro", back_populates="datapoint")

class Registro(Base):
    __tablename__ = "registros"

    id = Column(Integer, primary_key=True, index=True)
    datapoint_id = Column(Integer, ForeignKey("datapoints.id"))
    valor = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    datapoint = relationship("DataPoint", back_populates="registros")
    
def criar_banco():
    Base.metadata.create_all(bind=engine)
    print("Banco de dados criado com sucesso!")

if __name__ == "__main__":
    criar_banco()

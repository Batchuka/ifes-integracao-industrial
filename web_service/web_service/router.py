from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, criar_banco
import models
import schemas

# Criando a aplicação FastAPI
app = FastAPI(title="Modbus API", description="API para gerenciar DataSources, DataPoints e Registros")

# Função para obter a sessão do banco em cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar o banco ao iniciar a aplicação (opcional, pode rodar `criar_banco()` separadamente)
criar_banco()

# Criar um novo DataSource
@app.post("/datasources/", response_model=schemas.DataSource)
def criar_datasource(datasource: schemas.DataSourceCreate, db: Session = Depends(get_db)):
    db_datasource = models.DataSource(**datasource.dict())
    db.add(db_datasource)
    db.commit()
    db.refresh(db_datasource)
    return db_datasource

# Listar todos os DataSources
@app.get("/datasources/", response_model=list[schemas.DataSource])
def listar_datasources(db: Session = Depends(get_db)):
    return db.query(models.DataSource).all()

# Obter um DataSource por ID
@app.get("/datasources/{datasource_id}", response_model=schemas.DataSource)
def obter_datasource(datasource_id: int, db: Session = Depends(get_db)):
    datasource = db.query(models.DataSource).filter(models.DataSource.id == datasource_id).first()
    if not datasource:
        raise HTTPException(status_code=404, detail="DataSource não encontrado")
    return datasource
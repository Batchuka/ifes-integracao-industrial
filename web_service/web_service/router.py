import os
from fastapi import APIRouter, Depends, Header
from web_service.database import BancoDeDados
from web_service.modbus_client import ClienteModbus
from web_service.models import *

MODBUS_HOST = os.getenv("MODBUS_HOST", "localhost")

router = APIRouter()
client = ClienteModbus(host_ip=MODBUS_HOST, porta=502)
client.run()
banco = BancoDeDados()

def get_db():
    return banco

@router.get("/historico/temperatura_camara", response_model=list[TemperaturaCamaraResponse])
def get_temperatura_camara(db: BancoDeDados = Depends(get_db)):
    registros = db.obter_historico("temperatura_camara")
    return [TemperaturaCamaraResponse(temperatura_camara=int(row[0]) if str(row[0]).isdigit() else None, 
            timestamp=row[1]
        ) 
        for row in registros
    ]

@router.get("/historico/pressao_vapor", response_model=list[PressaoVaporResponse])
def get_pressao_vapor(db: BancoDeDados = Depends(get_db)):
    registros = db.obter_historico("pressao_vapor")
    return [PressaoVaporResponse(pressao_vapor=row[0], timestamp=row[1]) for row in registros]

@router.get("/historico/velocidade_blower", response_model=list[VelocidadeBlowerResponse])
def get_velocidade_blower(db: BancoDeDados = Depends(get_db)):
    registros = db.obter_historico("velocidade_blower")
    return [VelocidadeBlowerResponse(velocidade_blower=row[0], timestamp=row[1]) for row in registros]

@router.get("/historico/nivel_carga", response_model=list[NivelCargaResponse])
def get_nivel_carga(db: BancoDeDados = Depends(get_db)):
    registros = db.obter_historico("nivel_carga")
    return [NivelCargaResponse(nivel_carga=row[0], timestamp=row[1]) for row in registros]

@router.get("/historico/alerta_blower", response_model=list[AlertaBlowerResponse])
def get_alerta_blower(db: BancoDeDados = Depends(get_db)):
    registros = db.obter_historico("alerta_blower")
    return [AlertaBlowerResponse(alerta_blower=bool(row[0]), timestamp=row[1]) for row in registros]

@router.get("/historico/fluxo_gases", response_model=list[FluxoGasesResponse])
def get_fluxo_gases(db: BancoDeDados = Depends(get_db)):
    registros_a = db.obter_historico("fluxo_gas_a")
    registros_b = db.obter_historico("fluxo_gas_b")
    registros_c = db.obter_historico("fluxo_gas_c")

    return [
        FluxoGasesResponse(
            fluxo_gas_a=a[0], fluxo_gas_b=b[0], fluxo_gas_c=c[0], timestamp=a[1]
        )
        for a, b, c in zip(registros_a, registros_b, registros_c)
    ]

@router.put("/configuracao/oscilacao")
def set_fator_oscilacao(fator: int = Header(...)):
    sucesso = client.fator_oscilacao(fator)
    return {"mensagem": "Oscilação atualizada", "sucesso": sucesso, "novo_valor": fator}
from pydantic import BaseModel
from datetime import datetime

class HistoricoBase(BaseModel):
    timestamp: datetime

class TemperaturaCamaraResponse(HistoricoBase):
    temperatura_camara: int

class PressaoVaporResponse(HistoricoBase):
    pressao_vapor: int

class FluxoGasesResponse(HistoricoBase):
    fluxo_gas_a: int
    fluxo_gas_b: int
    fluxo_gas_c: int

class VelocidadeBlowerResponse(HistoricoBase):
    velocidade_blower: int

class NivelCargaResponse(HistoricoBase):
    nivel_carga: int

class AlertaBlowerResponse(HistoricoBase):
    alerta_blower: bool
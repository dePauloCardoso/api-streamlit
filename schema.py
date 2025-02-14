from pydantic import BaseModel
from typing import Optional
import uuid

# Modelo para entrada de dados ao criar/atualizar produtos
class ProdutoInput(BaseModel):
    cod_insersao: str
    descricao_kit: Optional[str]
    cod_kit: Optional[str]
    cod_sku: str
    descricao_sku: Optional[str]
    segmento: Optional[str]
    serie: Optional[str]
    volume: Optional[str]
    envio: Optional[str]
    frequencia: Optional[str]
    usuario: Optional[str]
    info_produto: Optional[str]
    tipo_material: Optional[str]
    classificacao_produto: Optional[str]
    personalizacao: Optional[str]

# Modelo para resposta ao cliente
class ProdutoOutput(ProdutoInput):
    id: uuid.UUID  # ID precisa ser retornado na saída

    class Config:
        from_attributes = True  # Permite conversão automática de modelos SQLAlchemy

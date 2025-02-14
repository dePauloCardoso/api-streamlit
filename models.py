import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()  # Certifique-se de que Base está definido corretamente

class Produto(Base):
    __tablename__ = "ppg_sae_2025"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cod_insersao = Column(String, index=True)
    descricao_kit = Column(String)
    cod_kit = Column(String)
    cod_sku = Column(String, index=True)
    descricao_sku = Column(String)
    segmento = Column(String)
    serie = Column(String)
    volume = Column(String)
    envio = Column(String)
    frequencia = Column(String)
    usuario = Column(String)
    info_produto = Column(String)
    tipo_material = Column(String)
    classificacao_produto = Column(String)
    personalizacao = Column(String)
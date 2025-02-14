import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()  # Define a base para os modelos SQLAlchemy

class Produto(Base):
    __tablename__ = "ppg_sae_2025"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    cod_insersao = Column(String, index=True, nullable=False)
    descricao_kit = Column(String, nullable=True)
    cod_kit = Column(String, nullable=True)
    cod_sku = Column(String, index=True, nullable=False)
    descricao_sku = Column(String, nullable=True)
    segmento = Column(String, nullable=True)
    serie = Column(String, nullable=True)
    volume = Column(String, nullable=True)
    envio = Column(String, nullable=True)
    frequencia = Column(String, nullable=True)
    usuario = Column(String, nullable=True)
    info_produto = Column(String, nullable=True)
    tipo_material = Column(String, nullable=True)
    classificacao_produto = Column(String, nullable=True)
    personalizacao = Column(String, nullable=True)

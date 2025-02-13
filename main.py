from fastapi import FastAPI
from pydantic import BaseModel
import database
# import uuid
# from dotenv import load_dotenv



# Definição do modelo da tabela ppg_sae_2025
class Produto(Base):
    __tablename__ = "ppg_sae_2025"
    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True) # Nova chave primária
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

# Criação da tabela (se não existir)
Base.metadata.create_all(bind=engine)

# Definição do modelo de entrada
class ProdutoInput(BaseModel):
    cod_insersao: str
    descricao_kit: str
    cod_kit: str
    cod_sku: str
    descricao_sku: str
    segmento: str
    serie: str
    volume: str
    envio: str
    frequencia: str
    usuario: str
    info_produto: str
    tipo_material: str
    classificacao_produto: str
    personalizacao: str

# Inicialização da API
app = FastAPI()

# Rota para obter todos os produtos
@app.get("/produtos")
def get_produtos(
    cod_insersao: str = None,
    cod_sku: str = None,
    segmento: str = None,
    serie: str = None,
    envio: str = None,
    usuario: str = None,
    personalizacao: str = None
):
    db = SessionLocal()
    query = db.query(Produto)

    if cod_insersao:
        query = query.filter(Produto.cod_insersao == cod_insersao)
    if cod_sku:
        query = query.filter(Produto.cod_sku == cod_sku)
    if segmento:
        query = query.filter(Produto.segmento == segmento)
    if serie:
        query = query.filter(Produto.serie == serie)
    if envio:
        query = query.filter(Produto.envio == envio)
    if usuario:
        query = query.filter(Produto.usuario == usuario)
    if personalizacao:
        query = query.filter(Produto.personalizacao == personalizacao)

    produtos = query.all()
    db.close()
    return produtos

# Rota para obter um produto pelo código de inserção
@app.get("/produtos/{cod_insersao}")
def get_produto(cod_insersao: str):
    db = SessionLocal()
    produto = db.query(Produto).filter(Produto.cod_insersao == cod_insersao).all()
    db.close()
    return produto

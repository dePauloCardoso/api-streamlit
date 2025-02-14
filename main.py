from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Produto
from schema import ProdutoInput
from typing import  List

# Inicialização da API
app = FastAPI()

# Rota para obter todos os produtos
@app.get("/produtos", response_model=List[Produto])  # Adicione response_model para tipagem
def get_produtos(
    cod_insersao: str = None,
    cod_sku: str = None,
    segmento: str = None,
    serie: str = None,
    envio: str = None,
    usuario: str = None,
    personalizacao: str = None,
    db: Session = Depends(get_db)
):
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
    return produtos

# Rota para obter um produto pelo código de inserção
@app.get("/produtos/{id}", response_model=Produto)  # Busca por ID (UUID)
def get_produto(id: str, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()  # Use first() para retornar um único produto
    return produto
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, init_db
from models import Produto
from schema import ProdutoInput, ProdutoOutput
from typing import List
import uuid

# Inicialização da API
app = FastAPI()

# Inicializa as tabelas do banco de dados ao iniciar a API
@app.on_event("startup")
def startup():
    init_db()

# Rota para obter todos os produtos (com filtros opcionais)
@app.get("/produtos", response_model=List[ProdutoOutput])
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

    # Aplicando filtros opcionais
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

# Rota para obter um produto pelo ID
@app.get("/produtos/{id}", response_model=ProdutoOutput)
def get_produto(id: uuid.UUID, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    return produto
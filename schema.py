from pydantic import BaseModel

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
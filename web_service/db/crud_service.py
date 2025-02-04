"""
    Instalação
        
        pip install fastapi
        pip install uvicorn
    
    Execução

        uvicorn caminho_arquivo_python:app --reload
"""
import uvicorn

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from produto_dao import ProdutoDAO


class Produto(BaseModel):
    id: int
    nome: str
    preco: float

class UpdateProduto(BaseModel):
    nome: Optional[str] = None
    preco: Optional[float] = None


app = FastAPI()

produto_dao = ProdutoDAO(caminho_bd='produtos.db')

@app.get('/')
def ola_mundo():
    return {
        'Mensagem': 'Olá Mundo!'
    }

@app.get('/listar_produtos')
def listar_produtos():
    
    lista_produtos = produto_dao.listar_produtos()
    
    lista_produtos_dict = [
        {
            'id': e[0],
            'nome': e[1],
            'preco': e[2],            
        } for e in lista_produtos
    ]
    
    return {
        'produtos': lista_produtos_dict
    }

@app.get('/buscar_produto/{id_produto}')
def buscar_produto(id_produto: int):    
    
    produto_existente = produto_dao.buscar_produto_by_id(id_produto)
   
    if produto_existente is None:
        return {
            'Erro': 'Produto não Encontrado!'
        }  
      
    return {
        'produto': produto_existente
    }

@app.get('/buscar_produto_by_nome')
def buscar_produto_by_nome(nome: Optional[str] = None):
    
    if nome is None:
        lista_produtos = produto_dao.listar_produtos()
    
        lista_produtos_dict = [
            {
                'id': e[0],
                'nome': e[1],
                'preco': e[2]
            } for e in lista_produtos
        ]
        
        return {
            'produtos': lista_produtos_dict
        }
        
    produtos_encontrados = produto_dao.buscar_produto_by_name(nome)
    
    return {
        'produtos': produtos_encontrados
    }

@app.post('/cadastrar_produto')
def cadastrar_produto(produto: Produto):
    
    produto_existente = produto_dao.buscar_produto_by_id(produto.id)
    
    if produto_existente is not None:
        return {
            'Erro': f'Já existe um produto cadastro com o ID {produto.id}'
        }    
    
    produto_dao.inserir_produto(produto)
    
    return produto

@app.put('/atualizar_produto/{id_produto}')
def atualizar_produto(id_produto: int, novo_produto: UpdateProduto):
    
    produto_aux = produto_dao.buscar_produto_by_id(id_produto)
    
    if produto_aux is None:
        return {
            'Erro': f'Nenhum produto com o ID "{id_produto}" foi encontrado'
        }
    
    produto_existente = {
        'id': produto_aux[0],
        'nome': produto_aux[1],
        'preco': produto_aux[2]
    }

    if novo_produto.nome is not None:
        produto_existente['nome'] = novo_produto.nome    
    
    if novo_produto.preco is not None:
        produto_existente['preco'] = novo_produto.preco    
    
    produto_dao.atualizar_produto(id_produto, produto_existente)
    
    return produto_existente

@app.delete('/remover_produto/{id_produto}')
def remover_produto(id_produto: int):
    
    produto_existente = produto_dao.buscar_produto_by_id(id_produto)
     
    if produto_existente is None:
        return {
            'Erro': f'Nenhum produto com o ID "{id_produto}" foi encontrado'
        }
    
    produto_dao.remover_produto(id_produto)
    
    return {
        'Mensagem': 'Produto Removido com Sucesso!'
    }


if __name__ == '__main__':
    
    uvicorn.run('crud_service:app', port=5000, log_level='info', reload=True)

from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@app.get('/')
def ola_mundo():
    return {
        'Mensagem': 'Olá Mundo!'
    }

@app.get('/listar_produtos')
def listar_produtos():
    return {
        'produtos': lista_produtos
    }

@app.get('/buscar_produto/{id_produto}')
def buscar_produto(id_produto: int):    
    produtos_encontrados = list(filter(lambda x: x['id'] == id_produto, lista_produtos))
    if len(produtos_encontrados) == 0:
        return {
            'Erro': 'Produto não Encontrado!'
        }    
    return {
        'produto': produtos_encontrados[0]
    }

@app.get('/buscar_produto_by_nome')
def buscar_produto_by_nome(nome: Optional[str] = None):
    if nome is None:
        return {
            'produtos': lista_produtos
        }
    produtos_encontrados = list(filter(lambda x: x['nome'] == nome, lista_produtos))
    if len(produtos_encontrados) == 0:
        return {
            'Erro': 'Nenhum Produto foi Encontrado!'
        }
    return {
        'produtos': produtos_encontrados
    }

@app.post('/cadastrar_produto')
def cadastrar_produto(produto: Produto):
    produtos_existentes = list(filter(lambda x: x['id'] == produto.id, lista_produtos))
    if len(produtos_existentes) >= 1:
        return {
            'Erro': f'Já existe um produto cadastro com o ID {produto.id}'
        }    
    produto_dict = produto.__dict__
    lista_produtos.append(produto_dict)
    return produto

@app.put('/atualizar_produto/{id_produto}')
def atualizar_produto(id_produto: int, novo_produto: UpdateProduto):
    produtos_existentes = list(filter(lambda x: x['id'] == id_produto, lista_produtos))
    if len(produtos_existentes) == 0:
        return {
            'Erro': f'Nenhum produto com o ID {id_produto} foi Encontrado'
        }
    if novo_produto.nome is not None:
        produtos_existentes[0]['nome'] = novo_produto.nome    
    if novo_produto.preco is not None:
        produtos_existentes[0]['preco'] = novo_produto.preco    
    return produtos_existentes[0]

@app.delete('/remover_produto/{id_produto}')
def remover_produto(id_produto: int):
    produto_existente = list(filter(lambda x: x['id'] == id_produto, lista_produtos))
    if len(produto_existente) == 0:
        return {
            'Erro': f'Nenhum produto com o ID "{id_produto}" foi encontrado'
        }
    produtos_aux = list(filter(lambda x: x['id'] != id_produto, lista_produtos))
    lista_produtos.clear()
    lista_produtos.extend(produtos_aux)
    return {
        'Mensagem': 'Produto Removido com Sucesso!'
    }


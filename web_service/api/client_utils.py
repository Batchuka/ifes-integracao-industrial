import requests


def cadastrar_produto(id_produto, nome, preco):
    url = 'http://127.0.0.1:5000/cadastrar_produto'
    produto_dict = {
        'id': id_produto,
        'nome': nome,
        'preco': preco
    }
    try:
        response = requests.post(url, json=produto_dict)
        if response.status_code != 200:
            return None
        if 'Erro' in response.json():
            return False
        return True
    except requests.ConnectionError:
        print('\nErro de Conexão')
        return None
    

def buscar_produto_by_id(id_produto):    
    url = f'http://127.0.0.1:5000/buscar_produto/{id_produto}'
    try:
        response = requests.get(url)
        if response.status_code != 200 or 'Erro' in response.json():
            return None
        return response.json()['produto']
    except requests.ConnectionError:
        print('\nErro de conexão.')
        return None


def buscar_produto_by_nome(nome):    
    url = f'http://127.0.0.1:5000/buscar_produto_by_nome'
    params = [
        ('nome', nome)
    ]
    try:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return None
        if 'Erro' in response.json():
            return None
        return response.json()['produtos']
    except requests.ConnectionError:
        print('\n\nErro de Conexão')
        return None


def listar_produtos():    
    url = 'http://127.0.0.1:5000/listar_produtos'
    try:
        response = requests.get(url)
    except requests.ConnectionError:
        print('\n\nErro na conexão')
        return None
    if response.status_code != 200:
        return None    
    return response.json()['produtos']


def atualizar_produto(id_produto, produto):    
    url = f'http://127.0.0.1:5000/atualizar_produto/{id_produto}'
    try:
        response = requests.put(url, json=produto)
        if response.status_code != 200:
            return None
        if 'Erro' in response.json():
            return False
        return True
    except requests.ConnectionError:
        print('\n\nErro na conexão')
        return None



def remover_produto(id_produto):
    url = f'http://127.0.0.1:5000/remover_produto/{id_produto}'   
    try:        
        response = requests.delete(url)
        if response.status_code != 200:
            return None
        if 'Erro' in response.json():
            return False
        return True
    except requests.ConnectionError:
        print('\nErro de Conexão')
        return None
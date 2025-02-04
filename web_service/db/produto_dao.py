"""
    DATA ACCESS OBJECT (DAO)
"""

import sqlite3


class ProdutoDAO:
    
    def __init__(self, caminho_bd):
        self.caminho_db = caminho_bd
            
    
    def buscar_produto_by_name(self, nome_produto):        
        connection = sqlite3.connect(self.caminho_db)        
        cursor = connection.cursor()        
        cursor.execute(
            """
                SELECT * FROM produtos WHERE nome = ?
            """,
            (nome_produto,)
        )        
        produtos_tuple = cursor.fetchall() 
        connection.close()        
        return produtos_tuple
    
    def buscar_produto_by_id(self, id_produto):        
        connection = sqlite3.connect(self.caminho_db)        
        cursor = connection.cursor()        
        cursor.execute(
            """
                SELECT * FROM produtos WHERE id = ?
            """,
            (id_produto,)
        )        
        produto_tuple = cursor.fetchone()        
        connection.close()        
        return produto_tuple
    
    
    def listar_produtos(self):
        connection = sqlite3.connect(self.caminho_db)        
        cursor = connection.cursor()        
        cursor.execute(
            """
                SELECT * FROM produtos
            """
        )        
        lista_produtos = cursor.fetchall()      
        connection.close()        
        return lista_produtos
    
    def inserir_produto(self, produto):        
        connection = sqlite3.connect(self.caminho_db)        
        cursor = connection.cursor()        
        cursor.execute(
            """INSERT INTO produtos (id, nome, preco) VALUES (?, ?, ?)""",
            (produto.id, produto.nome, produto.preco)
        )        
        connection.commit()        
        connection.close()        
        return cursor.lastrowid


    def atualizar_produto(self, id_produto, produto):        
        connection = sqlite3.connect(self.caminho_db)    
        print(produto)    
        cursor = connection.cursor()        
        cursor.execute(
            """UPDATE produtos SET nome = ?, preco = ? WHERE id = ?""",
            (produto['nome'], produto['preco'], id_produto)
        )        
        connection.commit()
        connection.close()
        return cursor.lastrowid

    def remover_produto(self, id_produto):
        
        connection = sqlite3.connect(self.caminho_db)
        
        cursor = connection.cursor()
        
        cursor.execute(
            """
                DELETE FROM produtos WHERE id = ?
            """,
            (id_produto, )
        )
        
        connection.commit()
        
        connection.close()
        
        return cursor.lastrowid

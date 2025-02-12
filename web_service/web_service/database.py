import sqlite3
import os
from datetime import datetime, timedelta

class BancoDeDados:
    _instance = None

    def __new__(cls, db_name="planta.db", recriar=False):
        if cls._instance is None:
            cls._instance = super(BancoDeDados, cls).__new__(cls)
            cls._instance.init_db(db_name, recriar)
        return cls._instance

    def init_db(self, db_name, recriar):
        self.db_name = db_name

        if recriar and os.path.exists(self.db_name):
            print("Removendo banco de dados existente...")
            os.remove(self.db_name)

        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.criar_tabela()
    
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS dados_planta (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                temperatura_camara INTEGER,
                pressao_vapor INTEGER,
                fluxo_gas_a INTEGER,
                fluxo_gas_b INTEGER,
                fluxo_gas_c INTEGER,
                velocidade_blower INTEGER,
                nivel_carga INTEGER,
                alerta_blower BOOLEAN
            )
        ''')
        self.conn.commit()
    
    def inserir_dados(self, dados):
        self.cursor.execute('''
            INSERT INTO dados_planta (
                temperatura_camara, pressao_vapor, fluxo_gas_a, fluxo_gas_b, fluxo_gas_c,
                velocidade_blower, nivel_carga, alerta_blower
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', dados)
        self.conn.commit()
    
    def limpar_registros_antigos(self):
        limite_tempo = datetime.now() - timedelta(minutes=60)
        self.cursor.execute("DELETE FROM dados_planta WHERE timestamp < ?", (limite_tempo,))
        self.conn.commit()

    def obter_historico(self, coluna: str):
        query = f"""
            SELECT {coluna}, timestamp 
            FROM dados_planta 
            WHERE timestamp IN (
                SELECT MAX(timestamp) 
                FROM dados_planta 
                GROUP BY strftime('%Y-%m-%d %H:%M', timestamp, '-0 minutes') 
                ORDER BY timestamp DESC 
                LIMIT 6
            )
            ORDER BY timestamp ASC
        """
        return self.cursor.execute(query).fetchall()

    def fechar(self):
        self.conn.close()

# # Teste rápido
# if __name__ == "__main__":
#     db = BancoDeDados()
#     dados_mock = (1090, 20, 650, 620, 670, 1300, 1, False)  # Exemplo de dados
#     db.inserir_dados(dados_mock)
#     db.limpar_registros_antigos()
#     db.fechar()
#     print("Banco de dados atualizado!")

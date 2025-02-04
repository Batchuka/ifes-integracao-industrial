import sqlite3


if __name__ == '__main__':    

    connection = sqlite3.connect('produtos.db')
    
    connection.execute(
        """
            CREATE TABLE produtos (
              id INTEGER NOT NULL PRIMARY KEY,
              nome TEXT NOT NULL,
              preco REAL NOT NULL  
            );
        """
    )
    
    connection.close()

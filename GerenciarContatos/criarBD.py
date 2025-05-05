import sqlite3

class CriarBD:
    def __init__(self):
        try:
            self.conexao = sqlite3.connect("contatos.db")
        except sqlite3.Error as e:
            print(f"erro ao criar banco - {e}")

        self.cursor = self.conexao.cursor() #objeto para manipular o banco

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS 
        contatos ( id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(255) NOT NULL,
        email VARCHAR(255), 
        telefone VARCHAR(20),
        data_aniversario DATE,
        empresa VARCHAR(255),
        cargo VARCHAR(255),
        tipo INTEGER
        );''')
        
        self.conexao.commit()
        self.conexao.close()

if __name__ == '__main__':
    CriaBD = CriarBD()
    CriaBD.create_table()
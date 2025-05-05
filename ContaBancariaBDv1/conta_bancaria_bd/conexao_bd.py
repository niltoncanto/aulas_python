import sqlite3
class conexaoBD:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("banco.db")
            self.cursor = self.conn.cursor()  # Inicializando o cursor
            print("Conexão estabelecida com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def criar_tabela(self):
        if self.conn:
            try:
                self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS contas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero_conta INTEGER NOT NULL,
                titular TEXT NOT NULL,
                saldo REAL NOT NULL,
                limite REAL NOT NULL)''')
                self.conn.commit()
                print("Tabela criada com sucesso!")
            except sqlite3.Error as e:
                print(f"Erro ao criar tabela: {e}")
        else:
            print("Não há conexão com o BD.")

    def fechar_conexao(self):
        if self.conn:
            try:
                self.conn.close()
                print('Conexão encerrada com o BD.')
            except sqlite3.Error as e:
                print(f"Erro ao fechar a conexão: {e}")
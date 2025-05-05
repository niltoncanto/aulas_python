import sqlite3

class ConexaoBD:
    # Conexão com o banco de dados SQLite
    def __init__(self):
        try:
            self.conn = sqlite3.connect('banco.db')  # Tentar se conectar ao banco de dados
            self.cursor = self.conn.cursor()  # Criar o cursor para executar comandos SQL
            print("Conexão estabelecida com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")  # Captura qualquer erro de conexão
            self.conn = None  # Definir conn como None em caso de erro
    
    # Criar tabela de contas
    def criar_tabela_contas(self):
        if self.conn:  # Verifica se a conexão foi estabelecida com sucesso
            try:
                self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS contas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    numero_conta TEXT NOT NULL,
                    nome_titular TEXT NOT NULL,
                    _saldo REAL NOT NULL,
                    __limite REAL NOT NULL
                )
                ''')
                self.conn.commit()  # Salvar mudanças
                print("Tabela 'contas' criada com sucesso.")
            except sqlite3.Error as e:
                print(f"Erro ao criar a tabela: {e}")
        else:
            print("Não foi possível criar a tabela, pois não há conexão com o banco de dados.")
    
    # Fechar conexão
    def fechar_conexao(self):
        if self.conn:
            try:
                self.conn.close()  # Fechar a conexão
                print("Conexão fechada com sucesso.")
            except sqlite3.Error as e:
                print(f"Erro ao fechar a conexão: {e}")

# Exemplo de uso
#conexao = ConexaoBD()
#conexao.criar_tabela_contas()
#conexao.fechar_conexao()

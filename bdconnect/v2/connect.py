import pyodbc

class SQLServerDB:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = None
        self.port = 1433
    def conectar(self):
        try:
            self.conn = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.server};port={self.port};DATABASE={self.database};UID={self.username};PWD={self.password}')
            print("Conexão bem-sucedida ao banco de dados.")
        except Exception as e:
            raise ConnectionError(f"Erro ao conectar ao banco de dados: {str(e)}")

    def inserir_dados(self, tabela, colunas, valores):
        try:
            cursor = self.conn.cursor()
            insert_query = f"INSERT INTO {tabela} ({', '.join(colunas)}) VALUES ({', '.join(['?']*len(colunas))})"
            cursor.execute(insert_query, valores)
            self.conn.commit()
            print("Dados inseridos com sucesso.")
        except Exception as e:
            raise ValueError(f"Erro ao inserir dados: {str(e)}")

    def selecionar_dados(self, tabela, colunas, condicao=None):
        try:
            cursor = self.conn.cursor()
            colunas_selecao = ', '.join(colunas) if colunas else '*'
            select_query = f"SELECT {colunas_selecao} FROM {tabela}"
            if condicao:
                select_query += f" WHERE {condicao}"
            result = cursor.execute(select_query)
            rows = result.fetchall()
            return rows
        except Exception as e:
            raise ValueError(f"Erro ao selecionar dados: {str(e)}")

    def atualizar_dados(self, tabela, colunas, valores, condicao):
        try:
            cursor = self.conn.cursor()
            update_query = f"UPDATE {tabela} SET {', '.join([f'{coluna} = ?' for coluna in colunas])} WHERE {condicao}"
            cursor.execute(update_query, valores)
            self.conn.commit()
            print("Dados atualizados com sucesso.")
        except Exception as e:
            raise ValueError(f"Erro ao atualizar dados: {str(e)}")

    def excluir_dados(self, tabela, condicao):
        try:
            cursor = self.conn.cursor()
            delete_query = f"DELETE FROM {tabela} WHERE {condicao}"
            cursor.execute(delete_query)
            self.conn.commit()
            print("Dados excluídos com sucesso.")
        except Exception as e:
            raise ValueError(f"Erro ao excluir dados: {str(e)}")

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")

def main():
    server = 'tcp:aulas.database.windows.net'
    database = 'aulas'
    username = 'niltoncanto'
    password = 'Koupati1000@'

    try:
        db = SQLServerDB(server, database, username, password)
        db.conectar()

        # Teste de inserção
        db.inserir_dados('alunos', ['nome', 'ra', 'id_curso', 'semestre'], ('Nilton Furtado', 100000, 3, 5))

        # Teste de seleção
        resultados = db.selecionar_dados('alunos', ['nome', 'ra', 'id_curso', 'semestre'])
        print("Resultados da consulta:")
        for resultado in resultados:
            print(resultado)
        print("*************************************************")
        for row in resultado.fetchall():
            print(f"Nome: {row.nome}, ra: {row.ra}, curso:{row.curso}")

        # Teste de atualização
        db.atualizar_dados('alunos', ['nome'], ('Nilton Furtado Canto',), 'nome = ?')
        
        # Teste de exclusão
        db.excluir_dados('NomeDaTabela', 'coluna = ?')

    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        if db:
            db.fechar_conexao()

if __name__ == "__main__":
    main()

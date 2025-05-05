import pyodbc

class DatabaseManager:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = None
        self.cursor = None

    def conectar(self):
        try:
            self.conn = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}')
            self.cursor = self.conn.cursor()
            print("Conexão bem-sucedida!")
        except pyodbc.Error as e:
            print(f"Erro na conexão: {str(e)}")

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Conexão encerrada.")

    def inserir_aluno(self, nome, ra, id_curso, semestre):
        try:
            query = "INSERT INTO alunos (nome, ra, id_curso, semestre) VALUES (?, ?, ?, ?)"
            self.cursor.execute(query, nome, ra, id_curso, semestre)
            self.conn.commit()
            print("Aluno inserido com sucesso.")
        except pyodbc.Error as e:
            print(f"Erro ao inserir aluno: {str(e)}")

    def selecionar_alunos(self):
        try:
            query = "SELECT * FROM alunos"
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()
            for row in resultados:
                print(f"Nome: {row.nome}, RA: {row.ra}, Curso: {row.id_curso}, Semestre: {row.semestre}")
        except pyodbc.Error as e:
            print(f"Erro ao selecionar alunos: {str(e)}")

    def atualizar_aluno(self, ra, novo_nome):
        try:
            query = "UPDATE alunos SET nome = ? WHERE ra = ?"
            self.cursor.execute(query, novo_nome, ra)
            self.conn.commit()
            print("Aluno atualizado com sucesso.")
        except pyodbc.Error as e:
            print(f"Erro ao atualizar aluno: {str(e)}")

    def deletar_aluno(self, ra):
        try:
            query = "DELETE FROM alunos WHERE ra = ?"
            self.cursor.execute(query, ra)
            self.conn.commit()
            print("Aluno excluído com sucesso.")
        except pyodbc.Error as e:
            print(f"Erro ao excluir aluno: {str(e)}")

    def selecionar_cursos(self):
        try:
            query = "SELECT * FROM cursos"
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()
            for row in resultados:
                print(f"Curso: {row.curso}, Alias: {row.alias}")
        except pyodbc.Error as e:
            print(f"Erro ao selecionar cursos: {str(e)}")

if __name__ == "__main__":
    server = 'tcp:aulas.database.windows.net'
    database = 'aulas'
    username = "aluno"
    password = "ShuPez@12tZHT"

    db = DatabaseManager(server, database, username, password)
    db.conectar()

    # Exemplos de utilização:
    db.inserir_aluno("João", "12345", 1, 2)
    db.selecionar_alunos()
    db.atualizar_aluno("12345", "João Silva")
    db.deletar_aluno("12345")
    db.selecionar_cursos()

    db.desconectar()

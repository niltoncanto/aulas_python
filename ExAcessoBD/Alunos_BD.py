import sqlite3
class DatabaseManager:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

    def fechar_conexao(self):
        self.conn.close()

    def inserir_aluno(self, nome, ra, id_curso, semestre):
        self.cur.execute("INSERT INTO alunos (nome, ra, id_curso, semestre) VALUES (?, ?, ?, ?)",
                         (nome, ra, id_curso, semestre))
        self.conn.commit()

    def selecionar_alunos(self, id_curso):
        self.cur.execute("SELECT * FROM alunos WHERE id_curso=?", (id_curso,))
        alunos = self.cur.fetchall()
        for aluno in alunos:
            print(aluno)

    def atualizar_aluno(self, ra, nome):
        self.cur.execute("UPDATE alunos SET nome=? WHERE ra=?", (nome, ra))
        self.conn.commit()

    def excluir_aluno(self, ra):
        self.cur.execute("DELETE FROM alunos WHERE ra=?", (ra,))
        self.conn.commit()

    def selecionar_cursos(self):
        self.cur.execute("SELECT * FROM cursos")
        cursos = self.cur.fetchall()
        for curso in cursos:
            print(curso)

def main():
    # Exemplos de operações
    print("Operações de exemplo:")
    db_mgr = DatabaseManager('cursos.db')
    
    # Teste de inserção de aluno
    db_mgr.inserir_aluno('Aluno Teste', 'RA123', 1, 1)
    
    # Teste de seleção de alunos por curso
    print("Alunos do curso 1:")
    db_mgr.selecionar_alunos(1)
    
    # Teste de atualização de nome do aluno
    db_mgr.atualizar_aluno('RA123', 'Aluno Teste Atualizado')
    
    # Teste de exclusão de aluno
    db_mgr.excluir_aluno('RA123')
    
    # Teste de seleção de todos os cursos
    print("Cursos disponíveis:")
    db_mgr.selecionar_cursos()

if __name__ == "__main__":
    main()

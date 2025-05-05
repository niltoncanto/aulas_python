import sqlite3
class DatabaseManager:
    def __init__(self,banco):
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()
    
    def fechar_conexao(self):
        self.conexao.close()
    
    def inserir_aluno(self,nome,ra,id_curso,semestre):
        self.cursor.execute('''INSERT INTO alunos (nome,ra,id_curso,semestre) VALUES (?,?,?,?)''',
                               (nome,ra,id_curso,semestre))
        self.conexao.commit()
        
    def atualizar_aluno(self,nome,ra,id_curso,semestre):
        self.cursor.execute('''UPDATE alunos SET nome=?,id_curso=?,semestre=? where ra=?''',(nome,id_curso,semestre,ra))
        self.conexao.commit()

    def remover_aluno(self,ra):
        self.cursor.execute('''DELETE FROM alunos WHERE ra = ?''',(ra))
import sqlite3

try:
    # Conectar ao banco de dados. Se o arquivo não existir, ele será criado.
    conexao = sqlite3.connect('cursos.db')

    # Criar um objeto cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Tentar inserir dados nas tabelas
    try:
        cursor.execute('''INSERT INTO cursos (curso, alias) VALUES
        ('Ciência da Computação', 'CC'),
        ('Análise de Sistemas', 'ADS'),
        ('Sistemas de Informação', 'SI');''')

        cursor.execute('''
        INSERT INTO alunos (nome, ra, id_curso, semestre) VALUES
        ('Aluno 1', 'RA001', 1, 1),
        ('Aluno 2', 'RA002', 2, 2),
        ('Aluno 3', 'RA003', 3, 3),
        ('Aluno 3', 'RA004', 4, 4),
        ('Aluno 3', 'RA005', 5, 5),
        ('Aluno 3', 'RA006', 6, 6);''')

    except sqlite3.IntegrityError as e:
        print("Erro de integridade:", e)
    except sqlite3.OperationalError as e:
        print("Erro operacional (possivelmente tabela não encontrada):", e)
    except Exception as e:
        print("Erro desconhecido ao inserir dados:", e)
    else:
        # Se não houver exceções, confirma a operação
        conexao.commit()
    finally:
        # Fechar a conexão
        conexao.close()

except sqlite3.Error as e:
    print("Erro ao conectar ao banco de dados:", e)

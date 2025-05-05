import sqlite3

try:
    # Conectar ao banco de dados. Se o arquivo não existir, ele será criado.
    conexao = sqlite3.connect('cursos.db')

    # Criar um objeto cursor para executar comandos SQL
    cursor = conexao.cursor()

    try:
        # Criar tabela cursos
        cursor.execute('''CREATE TABLE IF NOT EXISTS cursos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        curso TEXT NOT NULL,
        alias TEXT
        );''')

        # Criar tabela alunos
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ra TEXT NOT NULL,
        id_curso INTEGER,
        semestre INTEGER,
        FOREIGN KEY (id_curso) REFERENCES cursos(id)
        );''')

    except sqlite3.OperationalError as e:
        print("Erro operacional ao criar tabelas:", e)
    except Exception as e:
        print("Erro desconhecido:", e)
    else:
        # Se não houver exceções, confirma a operação
        conexao.commit()
    finally:
        # Fechar a conexão
        conexao.close()

except sqlite3.Error as e:
    print("Erro ao conectar ao banco de dados:", e)

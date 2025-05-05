import sqlite3

# Conectar ao banco de dados. Se o arquivo não existir, ele será criado.
conexao = sqlite3.connect('dbases.db')

# Criar um objeto cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar uma tabela
cursor.execute('''CREATE TABLE CPessoais (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome NVARCHAR(255) COLLATE Latin1_General_CI_AI, -- CI_AI indica "Case-Insensitive" e "Accent-Insensitive"
    email NVARCHAR(255),
    matricula NVARCHAR(20)
);''')

cursor.execute('''
CREATE TABLE CProfissionais (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome NVARCHAR(255),
    email NVARCHAR(255),
    telefone NVARCHAR(20),
    empresa NVARCHAR(255),
    cargo NVARCHAR(255)
);''')


# Confirmar a operação
conexao.commit()
# Fechar a conexão
conexao.close()





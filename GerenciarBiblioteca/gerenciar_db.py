import sqlite3

conexao = sqlite3.connect('dbases.db')
cursor = conexao.cursor()

nome = "Carlos Silva"
email = "Carlos.silva@example.com"

# Inserir um novo registro
cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))

nome = "Julia Silva"
email = "Julia.silva@example.com"

# Inserir um novo registro
cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))


cursor.execute('''SELECT * FROM usuarios''')
for linha in cursor.fetchall():
    print(linha)
conexao.commit()
conexao.close()


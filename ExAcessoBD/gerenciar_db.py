import sqlite3

conexao = sqlite3.connect('cursos.db')
cursor = conexao.cursor()

# nome = "Carlos Silva"
# email = "Carlos.silva@example.com"
# # Inserir um novo registro
# cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))


cursor.execute('''SELECT * FROM cursos''')
for linha in cursor.fetchall():
    print(linha)

cursor.execute('''SELECT * FROM alunos where id>2''')
for linha in cursor.fetchall():
    print(linha)    
#conexao.commit()
conexao.close()


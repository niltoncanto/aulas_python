import sqlite3
conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
              (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER)''')
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Ana", 28))
conexao.commit()
conexao.close()
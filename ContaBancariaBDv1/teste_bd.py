import sqlite3
conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor() #ponteiro para o banco
#criar tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS user (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome TEXT NOT NULL,
                  cpf TEXT NOT NULL )''')
conexao.commit()
#inserir dados
nome1 = "João da Silva"
cpf1 = "099999999"
nome2 = "Maria da Silva"
cpf2 = "0777777777"
cursor.execute('''INSERT INTO user (nome,cpf) VALUES (?,?)''', (nome1,cpf1))
cursor.execute('''INSERT INTO user (nome,cpf) VALUES (?,?)''', (nome2,cpf2))
conexao.commit()
#listar dados
cursor.execute('''SELECT * FROM user''')

""" for usuario in cursor.fetchall(): 
    print(usuario) """

print("******")
""" print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone()) """

for usuario in cursor.fetchmany(3): 
    print(usuario)

#update dados
cursor.execute('''UPDATE user SET NOME = ? WHERE id = ?''',('Carlos',1))
conexao.commit()

conexao.close()




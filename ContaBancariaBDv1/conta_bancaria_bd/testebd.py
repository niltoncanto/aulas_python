import sqlite3
conn = sqlite3.connect("teste.db")
cursor = conn.cursor()
#criar tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
               nome TEXT NOT NULL, cpf TEXT NOT NULL)
                ''')
#INSERT
nome1 = "joão carlos"
cpf1 = '2323232323'
nome2 = 'Maria Carla'
cpf2 = '55555'
cursor.execute('''INSERT INTO users (nome,cpf) VALUES
               (?,?)''',(nome1,cpf1))      
cursor.execute('''INSERT INTO users (nome,cpf) VALUES
               (?,?)''',(nome2,cpf2))

#UPDATE
#cursor.execute('''UPDATE users SET nome="Mario",cpf="11111"''')

#DELETE
cursor.execute('''DELETE FROM users WHERE nome="Mario"''')

#SELECT
cursor.execute('''SELECT * FROM users''')
linha = cursor.fetchone() #imprime a 1a linha e aponta para proxima
print(linha)
linha = cursor.fetchone()
print(linha)
print("*****")
for linha in cursor.fetchmany(5): #imprime n linhas
    print(linha)

print("*****")
for linha in cursor.fetchall(): #imprime todas as linhas
    print(linha)

conn.commit()
conn.close()
import pyodbc
#config conexao
server = "tcp:aulas.database.windows.net"
database = "aulas"
user = "aluno"
password = "ShuPez@12tZHT"

#criar conexao com o banco
try:
    conn = pyodbc.connect(f"DRIVER=ODBC Driver 17 for SQL Server; SERVER={server}; DATABASE={database}; UID={user}; PWD={password}")
except Exception as e:
    print(f"Erro ao conectar o banco:{e}")

#criar cursor (ponteiro para os resultados da operacao no banco)
cursor = conn.cursor()

#Select 
query = "SELECT * FROM alunos WHERE id_curso = ?"
valor = 1
response = cursor.execute(query,valor)
for rows in response.fetchall():
    print(rows)

#update
query = "UPDATE alunos SET nome = ? Where ra = ?"
valor1 = "Pedro Paulo Pedro"
valor2 = "555555"
cursor.execute(query,valor1,valor2)
cursor.commit()

#Select 
query = "SELECT * FROM alunos"
response = cursor.execute(query)
for rows in response.fetchall():
    print(rows)

#insert
query = "INSERT INTO alunos (nome, ra, id_curso, semestre) VALUES (?, ?, ?, ?)"
valores = ("Teste 123","666666",2,4)
cursor.execute(query,valores)
cursor.commit()

#Select 
query = "SELECT * FROM alunos"
response = cursor.execute(query)
for rows in response.fetchall():
    print(rows)

cursor.close()




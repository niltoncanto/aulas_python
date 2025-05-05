import pyodbc;

#configuração da conexão
server = "tcp:aulas.database.windows.net"
database = "aulas"
user = "aluno"
password = "ShuPez@12tZHT"
#user = "niltoncanto"
#password = "Koupati1000@"
#conexao com o banco de dados
try:
    conexao = pyodbc.connect(f"DRIVER=ODBC Driver 17 for SQL Server; SERVER={server}; DATABASE={database}; UID={user}; PWD={password}")
except Exception as e:
    print(f"Erro acesso ao banco: {e}")

#conexao = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server; SERVER = {server}; DATABASE = {database}; UID = {user}; PWD={password}')

#criar cursor (objeto para )
cursor = conexao.cursor()

#criar query para inserir dados
query = "insert into alunos (nome,ra,id_curso,semestre) values (?,?,?,?)"
#valores a serem inseridos
valores = ("João Paulo",555555, 1, 3)
#executar a query
cursor.execute(query, valores)
#confirmar a query
cursor.commit()

#criar uma query para selecionar dados
query = "select * from alunos where id_curso = 1"
result = cursor.execute(query)
for linha in result.fetchall():
    print(linha)


#criar uma query para update da tabela alunos
query = "update alunos set nome = ? where ra = ?"
valor1 = 'nilton canto'
valor2 = '555555'
cursor.execute(query,valor1,valor2)
cursor.commit()


#criar uma query para selecionar dados
query = "select * from alunos where id_curso = 1"
result = cursor.execute(query)
for linha in result.fetchall():
    print(linha)

#criar uma query para deletar uma linha específica
query = "delete from alunos where ra = ?"
valor = "555555"
cursor.execute(query,valor)
cursor.commit()

#fechar o cursor
cursor.close()
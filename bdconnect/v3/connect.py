import pyodbc

# Configuração da conexão
server = 'tcp:aulas.database.windows.net'
database = 'aulas'
user = "aluno"
password = "ShuPez@12tZHT"
port = "1433"

# String de conexão
connection_string = f'DRIVER={{SQL Server}};SERVER={server};PORT={port};DATABASE={database};UID={user};PWD={password}'

# Conectar ao banco de dados
try:
    conexao = pyodbc.connect(connection_string)
    cursor = conexao.cursor()
    print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro ao acessar o banco: {e}")

#criar cursor (objeto para executar comandos no banco  de dados )
cursor = conexao.cursor()

#criar query para inserir dados
query = "insert into alunos (nome,ra,id_curso,semestre) values (?,?,?,?)"
#valores a serem inseridos
valores = ("João Paulo",8889999, 1, 3)
#executar a query
cursor.execute(query, valores)
#confirmar a query
cursor.commit()

#criar uma query para selecionar dados
query = "select * from alunos where id_curso = 1"
result = cursor.execute(query)
for linha in result.fetchall():
    print(linha[1])


#criar uma query para update da tabela alunos
query = "update alunos set nome = ? where ra = ?"
valor1 = 'nilton canto'
valor2 = '8889999'
cursor.execute(query,valor1,valor2)
cursor.commit()


#criar uma query para selecionar dados
query = "select * from alunos where id_curso = 1"
result = cursor.execute(query)
for linha in result.fetchall():
    print(linha)

#criar uma query para deletar uma linha específica
""" query = "delete from alunos where ra = ?"
valor = "888889"
cursor.execute(query,valor)
cursor.commit() """

#fechar o cursor
cursor.close()
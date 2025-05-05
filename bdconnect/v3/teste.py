import pyodbc

# Configuração da conexão
server = 'tcp:aulas.database.windows.net'
database = 'aulas'
user = "aluno"
password = "ShuPez@12tZHT"
port = "1433"

# String de conexão
connection_string = f'DRIVER={{SQL Server}};SERVER={server},{port};DATABASE={database};UID={user};PWD={password}'

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
query = "insert into alunos (?) values (?,?,?,?)"
#valores a serem inseridos
valores = (('nome','ra','id_curso','semestre'),"João Paulo",545454, 1, 3)
#executar a query
cursor.execute(query, valores)
#confirmar a query
cursor.commit()

#criar uma query para selecionar dados
query = "select * from alunos where id_curso = 1"
result = cursor.execute(query)
for linha in result.fetchall():
    print(linha)
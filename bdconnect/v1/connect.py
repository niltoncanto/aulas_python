import pyodbc

# Configuração da conexão
server = 'localhost'
database = 'aulas'
#username = 'niltoncanto'
#password = 'Koupati1000@'
username = "aluno"
password = "ShuPez@12tZHT"
# Conectar ao banco de dados
conn = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}')

# Criar um cursor
cursor = conn.cursor()

# Comando SQL de inserção
insert_query = "INSERT INTO alunos (nome, ra, id_curso, semestre) VALUES (?, ?, ?, ?)"

# Valores a serem inseridos
values = ('Nilton Canto', 23455, 1, 8)

# Executar a inserção
cursor.execute(insert_query, values)

# Confirmar a inserção
conn.commit()

# Fechar o cursor
cursor.close()

# Comando SQL de consulta
cursor = conn.cursor()
select_query = "SELECT * FROM alunos"

# Executar a consulta
result = cursor.execute(select_query)

# Recuperar os resultados
for row in result:
    print(row)

# Fechar o cursor
cursor.close()

# Comando SQL de atualização
cursor = conn.cursor()
update_query = "UPDATE alunos SET id_curso = ? WHERE ra = ?"

# Novos valores
new_value1 = 2
condition_value2 = "23455"

# Executar a atualização
cursor.execute(update_query, (new_value1, condition_value2))
conn.commit()

# Fechar o cursor
cursor.close()


# Comando SQL de consulta
cursor = conn.cursor()
select_query = "SELECT * FROM alunos"

# Executar a consulta
result = cursor.execute(select_query)

# Recuperar os resultados
for row in result:
    print(row)

#Comando SQL de exclusão
delete_query = "DELETE FROM alunos WHERE ra = ?"

#Valor a ser excluído
value_to_delete = "RA-ADS-29"

# Executar a exclusão
cursor.execute(delete_query, value_to_delete)
conn.commit()



select_query = "SELECT * FROM alunos"
# Executar a consulta
result = cursor.execute(select_query)
# Recuperar os resultados
for row in result:
    print(row)



# Fechar o cursor
cursor.close()

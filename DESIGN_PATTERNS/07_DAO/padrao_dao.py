import sqlite3
class ConectaBanco:
    def __init__(self, db_name):
        self.db_name = db_name

    def get_conexao(self):
        return sqlite3.connect(self.db_name)
    
class Cliente:
    def __init__(self,nome,email,cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf
    
class ClienteDAO:
    def __init__(self,db_conexao: ConectaBanco):
        self.conexao_db = db_conexao
        self.criar_tabela()

    def criar_tabela(self):
        cursor= self.conexao_db.get_conexao()
        cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                email TEXT,
                cpf TEXT NOT NULL               
            )''')  
    def listar(self):
        pass
    def inserir(self, cliente:Cliente):
        conexao = self.conexao_db.get_conexao()
        cursor = conexao.cursor()

        cursor.execute('''INSERT INTO clientes (nome,email,cpf) VALUES (?,?,?)''',
                       (cliente.nome,cliente.email,cliente.cpf))
        conexao.commit()
        conexao.close()
    def deletar (self, cliente:Cliente):
        pass
    def atualizar(self,cliente:Cliente):
        pass

class ClienteController:
    def __init__(self):
        self.conexao_bd = ConectaBanco("clientes.db")
        self.cliente_dao = ClienteDAO(self.conexao_bd)

    def cadastrar_cliente(self,cliente:Cliente):
        self.cliente_dao.inserir(cliente)

if __name__=="__main__":
# Exemplo de uso do controlador para cadastrar múltiplos clientes
    controlador = ClienteController()
    clientes = [
        Cliente("Alice", "alice@example.com", "11122233344"),
        Cliente("Bob", "bob@example.com", "22233344455"),
        Cliente("Carol", "carol@example.com", "33344455566")
    ]
    for cliente in clientes:
        controlador.cadastrar_cliente(cliente)
import sqlite3
from abc import ABC,abstractmethod
class ConectaBanco:
    def __init__(self,bd_nome):
        self.bd_nome = bd_nome
    def get_conexao(self):
        return sqlite3.connect(self.bd_nome)
class Cliente:
    def __init__(self,nome,email,cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf
class ClienteDao(ABC):
    def __init__(self,conexao:ConectaBanco):
        self.conexao = conexao
        self.criar_tabela()
    @abstractmethod
    def criar_tabela(self):
        pass
    @abstractmethod
    def inserir(self):
        pass
    @abstractmethod
    def deletar(self):
        pass
    @abstractmethod
    def atualizar(self):
        pass
class ClienteDaoSqlite(ClienteDao):
    def criar_tabela(self):
        cursor = self.conexao.get_conexao().cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY,
                       nome TEXT NOT NULL, 
                       email TEXT NOT NULL,
                       cpf TEXT NOT NULL)''')
        self.conexao.get_conexao().commit()
        self.conexao.get_conexao().close()
    def deletar(self):
        pass
    def atualizar(self):
        pass
    def inserir(self, cliente: Cliente):
        conexao = self.conexao_db.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('''INSERT INTO clientes (nome, email, cpf) VALUES (?, ?, ?)''',
                       (cliente.nome, cliente.email, cliente.cpf))
        conexao.commit()
        conexao.close()

class ClienteController:
    def __init__(self):
        self.conexao_bd = ConectaBanco("clientes3.db")
        self.cliente_dao = ClienteDaoSqlite(self.conexao_bd)

    def cadastrar_cliente(self, cliente: Cliente):
        self.cliente_dao.inserir(cliente)

if __name__ == "__main__":
    controlador = ClienteController()
    clientes = [
        Cliente("Alice", "alice@example.com", "11122233344"),
        Cliente("Bob", "bob@example.com", "22233344455"),
        Cliente("Carol", "carol@example.com", "33344455566")
    ]
    for cliente in clientes:
        controlador.cadastrar_cliente(cliente)
import sqlite3
from typing import List, Optional

class ConectaBanco:
    """Classe para gerenciar conexões com o banco de dados."""
    def __init__(self, db_name: str = "clientes.db"):
        self.db_name = db_name

    def get_conexao(self) -> sqlite3.Connection:
        """Retorna uma conexão com o banco de dados SQLite."""
        return sqlite3.connect(self.db_name)

class Cliente:
    """Classe representando a entidade Cliente."""
    def __init__(self, id: int, nome: str, cpf: str, telefone: str, endereco: str):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco

class ClienteDAO:
    """Classe para realizar operações de banco de dados na tabela Cliente."""
    def __init__(self, db_conexao: ConectaBanco):
        self.db_conexao = db_conexao
        self.criar_tabela()

    def criar_tabela(self):
        """Cria a tabela de clientes caso ela não exista."""
        conn = self.db_conexao.get_conexao()
        with conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL,
                telefone TEXT,
                endereco TEXT
            )''')

    def cadastrar(self, cliente: Cliente) -> None:
        """Cadastra um novo cliente no banco de dados."""
        conn = self.db_conexao.get_conexao()
        with conn:
            conn.execute('''INSERT INTO clientes (nome, cpf, telefone, endereco)
                            VALUES (?, ?, ?, ?)''', 
                            (cliente.nome, cliente.cpf, cliente.telefone, cliente.endereco))

    def listar(self) -> List[Cliente]:
        """Retorna uma lista com todos os clientes cadastrados."""
        conn = self.db_conexao.get_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        rows = cursor.fetchall()
        return [Cliente(id=row[0], nome=row[1], cpf=row[2], telefone=row[3], endereco=row[4]) for row in rows]

    def consultar_por_id(self, id: int) -> Optional[Cliente]:
        """Consulta um cliente pelo ID."""
        conn = self.db_conexao.get_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return Cliente(id=row[0], nome=row[1], cpf=row[2], telefone=row[3], endereco=row[4])
        return None

    def atualizar(self, cliente: Cliente) -> None:
        """Atualiza os dados de um cliente existente."""
        conn = self.db_conexao.get_conexao()
        with conn:
            conn.execute('''UPDATE clientes SET nome = ?, cpf = ?, telefone = ?, endereco = ?
                            WHERE id = ?''', 
                            (cliente.nome, cliente.cpf, cliente.telefone, cliente.endereco, cliente.id))

    def excluir(self, cliente: Cliente) -> None:
        """Exclui um cliente do banco de dados pelo ID."""
        conn = self.db_conexao.get_conexao()
        with conn:
            conn.execute("DELETE FROM clientes WHERE id = ?", (cliente.id,))

class ControleCliente:
    """Classe controladora que utiliza ClienteDAO para gerenciar clientes."""
    def __init__(self):
        self.conexao_banco = ConectaBanco()
        self.cliente_dao = ClienteDAO(self.conexao_banco)

    def cadastrar_cliente(self, cliente: Cliente) -> None:
        """Cadastra um novo cliente."""
        self.cliente_dao.cadastrar(cliente)

    def listar_clientes(self) -> List[Cliente]:
        """Lista todos os clientes cadastrados."""
        return self.cliente_dao.listar()

    def atualizar_cliente(self, cliente: Cliente) -> None:
        """Atualiza os dados de um cliente."""
        self.cliente_dao.atualizar(cliente)

    def excluir_cliente(self, cliente: Cliente) -> None:
        """Exclui um cliente."""
        self.cliente_dao.excluir(cliente)

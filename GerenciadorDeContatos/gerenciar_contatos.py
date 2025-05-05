import sqlite3
from abc import ABC, abstractmethod
from datetime import date

# Classe abstrata Contato
class Contato(ABC):
    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone

    @abstractmethod
    def obter_informacoes(self):
        pass

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def telefone(self):
        return self.__telefone

# Subclasse ContatoPessoal
class ContatoPessoal(Contato):
    def __init__(self, nome, email, telefone, data_aniversario):
        super().__init__(nome, email, telefone)
        self.__data_aniversario = data_aniversario

    def obter_informacoes(self):
        return f"Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Aniversário: {self.__data_aniversario}"

    @property
    def data_aniversario(self):
        return self.__data_aniversario

# Subclasse ContatoProfissional
class ContatoProfissional(Contato):
    def __init__(self, nome, email, telefone, empresa, cargo):
        super().__init__(nome, email, telefone)
        self.__empresa = empresa
        self.__cargo = cargo

    def obter_informacoes(self):
        return f"Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Empresa: {self.__empresa}, Cargo: {self.__cargo}"

    @property
    def empresa(self):
        return self.__empresa

    @property
    def cargo(self):
        return self.__cargo

# Classe GerenciadorContatos
class GerenciadorContatos:
    def __init__(self):
        self.conn = sqlite3.connect('contatos.db')
        self.criar_tabela()

    def criar_tabela(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS contatos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telefone TEXT NOT NULL,
                    aniversario TEXT,
                    empresa TEXT,
                    cargo TEXT,
                    tipo TEXT NOT NULL
                )
            ''')

    def inserir_contato_pessoal(self, contato: ContatoPessoal):
        with self.conn:
            self.conn.execute('''
                INSERT INTO contatos (nome, email, telefone, aniversario, tipo)
                VALUES (?, ?, ?, ?, 'Pessoal')
            ''', (contato.nome, contato.email, contato.telefone, contato.data_aniversario))

    def inserir_contato_profissional(self, contato: ContatoProfissional):
        with self.conn:
            self.conn.execute('''
                INSERT INTO contatos (nome, email, telefone, empresa, cargo, tipo)
                VALUES (?, ?, ?, ?, ?, 'Profissional')
            ''', (contato.nome, contato.email, contato.telefone, contato.empresa, contato.cargo))

    def atualizar_contato_pessoal(self, contato_id, contato: ContatoPessoal):
        with self.conn:
            self.conn.execute('''
                UPDATE contatos
                SET nome = ?, email = ?, telefone = ?, aniversario = ?
                WHERE id = ? AND tipo = 'Pessoal'
            ''', (contato.nome, contato.email, contato.telefone, contato.data_aniversario, contato_id))

    def atualizar_contato_profissional(self, contato_id, contato: ContatoProfissional):
        with self.conn:
            self.conn.execute('''
                UPDATE contatos
                SET nome = ?, email = ?, telefone = ?, empresa = ?, cargo = ?
                WHERE id = ? AND tipo = 'Profissional'
            ''', (contato.nome, contato.email, contato.telefone, contato.empresa, contato.cargo, contato_id))

    def listar_contatos_pessoais(self):
        with self.conn:
            return self.conn.execute('''
                SELECT * FROM contatos WHERE tipo = 'Pessoal'
            ''').fetchall()

    def listar_contatos_profissionais(self):
        with self.conn:
            return self.conn.execute('''
                SELECT * FROM contatos WHERE tipo = 'Profissional'
            ''').fetchall()

    def listar_contatos(self):
        with self.conn:
            return self.conn.execute('''
                SELECT * FROM contatos
            ''').fetchall()

    def buscar_contato(self, nome: str):
        with self.conn:
            return self.conn.execute('''
                SELECT * FROM contatos WHERE nome = ?
            ''', (nome,)).fetchall()

# Teste do Gerenciador de Contatos
if __name__ == "__main__":
    # Criação do Gerenciador de Contatos
    gerenciador = GerenciadorContatos()

    # Adicionando Contatos Pessoais e Profissionais
    contato_pessoal = ContatoPessoal("João Silva", "joao@email.com", "11987654321", "1990-10-10")
    contato_profissional = ContatoProfissional("Maria Souza", "maria@empresa.com", "11987654322", "Empresa X", "Gerente")

    gerenciador.inserir_contato_pessoal(contato_pessoal)
    gerenciador.inserir_contato_profissional(contato_profissional)

    # Listar todos os contatos
    contatos = gerenciador.listar_contatos()
    for contato in contatos:
        print(contato)

    # Buscar contato por nome
    contato_buscado = gerenciador.buscar_contato("João Silva")
    print(f"Contato buscado: {contato_buscado}")

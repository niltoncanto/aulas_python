from abc import ABC, abstractmethod
import sqlite3
import os

class Contato(ABC):
    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone

    @abstractmethod
    def obter_informacoes(self):
        pass

class ContatoPessoal(Contato):
    def __init__(self, nome, email, telefone, data_aniversario):
        super().__init__(nome, email, telefone)
        self.__data_aniversario = data_aniversario

    def obter_informacoes(self):
        return f"Nome: {self._Contato__nome} E-mail: {self._Contato__email} Telefone: {self._Contato__telefone} Aniversário: {self.__data_aniversario}"

class ContatoProfissional(Contato):
    def __init__(self, nome, email, telefone, empresa, cargo):
        super().__init__(nome, email, telefone)
        self.__empresa = empresa
        self.__cargo = cargo

    def obter_informacoes(self):
        return f"Nome: {self._Contato__nome} E-mail: {self._Contato__email} Telefone: {self._Contato__telefone} Empresa: {self.__empresa} Cargo: {self.__cargo}"

class GerenciadorContatos:
    def __init__(self):
        # Define o caminho absoluto para o banco de dados
        db_path = os.path.join(os.path.dirname(__file__), "contatos.db")
        print(db_path)
        self.conexao = sqlite3.connect(db_path)
        self.cursor = self.conexao.cursor()

    def inserir_contato(self, contato):
        if isinstance(contato, ContatoPessoal):
            query = '''INSERT INTO contatos (nome, email, telefone, data_aniversario, empresa, cargo, tipo) VALUES (?,?,?,?,?,?,?)'''
            self.cursor.execute(query, (contato._Contato__nome, contato._Contato__email, contato._Contato__telefone, contato._ContatoPessoal__data_aniversario,None,None, 1))
            self.conexao.commit()
        else:
            query = '''INSERT INTO contatos (nome, email, telefone, data_aniversario,empresa,cargo, tipo) VALUES (?,?,?,?,?,?,?)'''
            self.cursor.execute(query, (contato._Contato__nome, contato._Contato__email, contato._Contato__telefone, None,contato._ContatoProfissional__empresa,contato._ContatoProfissional__cargo, 2))
            self.conexao.commit()

    def listar_contatos(self):
        query = "SELECT * FROM contatos;"
        self.cursor.execute(query)
        for contato in self.cursor.fetchall():
            print(contato)

    def buscar_contato(self, nome):
        query = f"SELECT * FROM contatos WHERE nome like '%{nome}%';"
        self.cursor.execute(query)
        for contato in self.cursor.fetchall():
            print(contato)

    def atualizar_contato(self, id, **kwargs):
        query = "UPDATE contatos SET "
        parametros = []
        set_clause = []
        for k, v in kwargs.items():
            set_clause.append(f"{k} = ?")
            parametros.append(v)
        query += ", ".join(set_clause)
        query += " WHERE id = ?"
        parametros.append(id)
        
        # Agora, use a execução da query com parâmetros
        # cursor.execute(query, parametros)
        print(query, parametros)  # Simulando a execução para visualizar


if __name__ == "__main__":
    contato1 = ContatoPessoal("Joao", "nilton@aaaaa.com.br", "343343434", "15/04/1970")
    contato2 = ContatoProfissional("Nilton123", "nilton@aaaaa.com.br", "343343434", "Nasa","Engenheiro")
    gerenciador = GerenciadorContatos()
    gerenciador.inserir_contato(contato1)
    gerenciador.inserir_contato(contato2)
    gerenciador.listar_contatos()
    print("***********************************")
    gerenciador.buscar_contato('Joao')
    gerenciador.atualizar_contato(id=3,nome='Pedro',email='xxx@xxx.com.br')
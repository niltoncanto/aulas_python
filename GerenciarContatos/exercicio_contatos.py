from abc import ABC, abstractmethod
import sqlite3

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
        pass

class ContatoProfissional(Contato):
    def __init__(self, nome, email, telefone, empresa, cargo):
        super().__init__(nome, email, telefone)
        self.__empresa = empresa
        self.__cargo = cargo

    def obter_informacoes(self):
        pass

class GerenciadorContatos:
    def __init__(self):
        self.conexao = sqlite3.connect("contatos.db")
        self.cursor = self.conexao.cursor()

    def inserir_contato(self, contato, tipo_contato):
        pass

    def listar_contatos(self):
        pass

    def buscar_contato(self, nome):
        pass

    def atualizar_contato(self,id):
        pass



if __name__=="__main__":
    pass
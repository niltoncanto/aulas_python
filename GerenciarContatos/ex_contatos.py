from abc import ABC, abstractmethod
from datetime import date
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
        return f'Nome: {self._Contato__nome}, Email: {self._Contato__email}, Telefone: {self._Contato__telefone}, Data de Aniversário: {self.__data_aniversario}'

class ContatoProfissional(Contato):
    def __init__(self, nome, email, telefone, empresa, cargo):
        super().__init__(nome, email, telefone)
        self.__empresa = empresa
        self.__cargo = cargo

    def obter_informacoes(self):
        return f'Nome: {self._Contato__nome}, Email: {self._Contato__email}, Telefone: {self._Contato__telefone}, Empresa: {self.__empresa}, Cargo: {self.__cargo}'

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

    def atualizar_contato(self,nome):
        pass






if __name__=="__main__":

    contato_pessoal = ContatoPessoal(nome="Maria Silva", email="maria.silva@example.com", telefone="123456789", data_aniversario="1990/5/15")
    contato_profissional = ContatoProfissional(nome="João Pereira", email="joao.pereira@example.com", telefone="987654321", empresa="Tech Solutions", cargo="Desenvolvedor")

    gerenciador = GerenciadorContatos()

    gerenciador.inserir_contato(contato_pessoal, tipo_contato=1)
    gerenciador.inserir_contato(contato_profissional, tipo_contato=2)

    print("Listando todos os contatos:")
    gerenciador.listar_contatos()

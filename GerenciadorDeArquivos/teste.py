import os
import pytest
from gerenciador import GerenciadorDeArquivos  # Substitua 'seu_modulo' pelo nome do módulo onde a classe GerenciadorDeArquivos está definida

class TestGerenciadorDeArquivos:
    @pytest.fixture(autouse=True, scope='function')
    def setup_class(self):
        self.gerenciador = GerenciadorDeArquivos()
        self.nome_diretorio = "diretorio_teste"
        self.nome_arquivo = "arquivo_teste.txt"

    def test_criar_diretorio(self):
        self.gerenciador.criar_diretorio(self.nome_diretorio)
        assert os.path.exists(self.nome_diretorio)

    def test_listar_diretorio(self):
        self.gerenciador.criar_diretorio(self.nome_diretorio)
        # Aqui você pode verificar se a listagem está correta, talvez redirecionando a saída padrão e comparando-a

    def test_gravar_em_arquivo(self):
        self.gerenciador.gravar_em_arquivo(self.nome_arquivo, "Olá, mundo!")
        assert os.path.exists(self.nome_arquivo)

    def test_ler_arquivo(self):
        self.gerenciador.gravar_em_arquivo(self.nome_arquivo, "Olá, mundo!")
        # Aqui você pode verificar se a leitura está correta, talvez redirecionando a saída padrão e comparando-a

    def test_apagar_diretorio(self):
        self.gerenciador.criar_diretorio(self.nome_diretorio)
        self.gerenciador.apagar_diretorio(self.nome_diretorio)
        assert not os.path.exists(self.nome_diretorio)

    def test_renomear(self):
        self.gerenciador.criar_diretorio(self.nome_diretorio)
        self.gerenciador.renomear(self.nome_diretorio, "novo_nome_diretorio")
        assert not os.path.exists(self.nome_diretorio)
        assert os.path.exists("novo_nome_diretorio")

    @pytest.fixture(autouse=True, scope='function')
    def teardown(self):
        if os.path.exists(self.nome_diretorio):
            os.rmdir(self.nome_diretorio)
        if os.path.exists("novo_nome_diretorio"):
            os.rmdir("novo_nome_diretorio")
        if os.path.exists(self.nome_arquivo):
            os.remove(self.nome_arquivo)
""" 
import pytest

@pytest.fixture(autouse=True)
def setup_and_teardown():
    print("Setup: Código de configuração aqui")
    yield
    print("Teardown: Código de limpeza aqui")

def test_one():
    print("Teste 1")
    
def test_two():
    print("Teste 2") """

import os
import pytest
from circulo import Circulo
from retangulo import Retangulo 
from gerenciararquivo import GerenciarArquivo
import numpy as np
#from pytest import approx

# Testes para a classe Circulo
def test_circulo_area():
    circulo = Circulo(5)
    assert circulo.calcular_area() == np.pi * 5 * 5

def test_circulo_perimetro():
    circulo = Circulo(5)
    assert circulo.calcular_perimetro() == 2 * np.pi * 5

# Testes para a classe Retangulo
def test_retangulo_area():
    retangulo = Retangulo(4, 6)
    assert retangulo.calcular_area() == 4 * 6

""" @pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (1, 2, 3), (4, 8, 12)])
def test_retangulo_perimetro():
    retangulo = Retangulo(4, 6)
    assert retangulo.calcular_perimetro() == 2 * (4 + 6) """

# Utilizando o decorador para parametrizar o teste
@pytest.mark.parametrize("largura, altura, esperado", [(1, 2, 6), (1, 2, 6), (4, 8, 24)])
def test_retangulo_perimetro(largura, altura, esperado):
    # Criando um objeto Retangulo com as dimensões fornecidas
    retangulo = Retangulo(largura, altura)
    # Verificando se o perímetro calculado é igual ao valor esperado
    assert retangulo.calcular_perimetro() == esperado
    
# Fixture para configurar e limpar o arquivo de teste
@pytest.fixture
def setup_teardown_arquivo():
    # Configuração: removendo o arquivo de teste, se ele existir
    if os.path.exists("test_formas.txt"):
        os.remove("test_formas.txt")
    
    yield  # Este é o ponto onde a fixture "pausa" e permite que o teste seja executado
    
    # Limpeza: removendo o arquivo de teste
    if os.path.exists("test_formas.txt"):
        os.remove("test_formas.txt")

# Teste utilizando a fixture
def test_gerenciar_arquivo_gravar_ler(setup_teardown_arquivo):
    # Testando o método gravar
    GerenciarArquivo.gravar("Teste", "test_formas.txt")

    # Testando o método ler
    conteudo = GerenciarArquivo.ler("test_formas.txt")
    assert conteudo.strip() == "Teste"  # strip() é usado para remover espaços em branco e quebras de linha





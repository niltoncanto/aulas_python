import math
import os
import pytest
from circulo import Circulo
from retangulo import Retangulo
from formageometrica import FormaGeometrica
from gerenciararquivo import GerenciarArquivo

# Testes para a classe Circulo
def test_circulo_area():
    circulo = Circulo(5)
    assert circulo.calcular_area() == math.pi*5*5
def test_circulo_perimetro():
    circulo = Circulo(5)
    assert circulo.calcular_perimetro() == 2*math.pi*5

# Testes para a classe Retangulo
def test_retangulo_area():
    retangulo = Retangulo(3,4)
    assert retangulo.calcular_area() == 12

# Utilizando o decorador para parametrizar o teste
@pytest.mark.parametrize("altura,largura,esperado",[(1,2,6),(3,3,12),(4,6,20)])
def test_retangulo_perimetro(altura,largura,esperado):
    retangulo = Retangulo(altura,largura)
    assert retangulo.calcular_perimetro() == esperado
    
# Fixture para configurar e limpar o arquivo de teste
@pytest.fixture
def test_setup_teardown():
    if os.path.exists("test_formas.txt"):
        os.remove("test_formas.txt")

    yield

    if os.path.exists("test_formas.txt"):
        os.remove("test_formas.txt")

# Teste utilizando a fixture

def test_gerenciararquivo_gravar_ler(test_setup_teardown):
    GerenciarArquivo.gravar("teste","test_formas.txt")

    conteudo = GerenciarArquivo.ler("test_formas.txt")
    assert conteudo.strip() == "teste"

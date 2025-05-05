import math
import os
import pytest
from circulo import Circulo
from retangulo import Retangulo
from gerenciararquivo import GerenciarArquivo

def test_area_circulo():
    circulo = Circulo(10)
    assert circulo.calcular_area()==math.pi*10*10

def test_perimetro_circulo():
    circulo = Circulo(4)
    assert circulo.calcular_perimetro()==2*math.pi*4

def test_area_retangulo():
    ret = Retangulo(4,3)
    assert ret.calcular_area() == 4*3

@pytest.mark.parametrize("altura,largura,esperado",[(1,3,8),(3,4,14)])
def test_perimetro_retangula(altura,largura,esperado):
    ret = Retangulo(altura,largura)
    assert ret.calcular_perimetro() == esperado

@pytest.fixture
def test_setup_teardown():
    if os.path.exists("test_formas.txt"):
        os.remove("test_formas.txt") 

    yield # aguarda a execução do test unitário

    if os.path.exists("test_formas.txt"):
        os.remove("test_formas.txt") 

def test_gerenciararquivo_gravar(test_setup_teardown):
    GerenciarArquivo.gravar("Teste gravação","test_formas.txt")
    conteudo = GerenciarArquivo.ler("test_formas.txt")
    assert conteudo.strip() == "Teste gravação"
import pytest
import os
from exercicio_pytest import ExercicioPyTest

@pytest.fixture
def obj():
    return ExercicioPyTest()

def test_soma(obj):
    assert obj.soma(20,1) == 21

def test_concatena_strings(obj):
    assert obj.concatena_strings("Olá, ", "mundo!") == "Olá, mundo!"

@pytest.fixture
def test_setup_teardown_arquivo():
    if os.path.exists("temp.txt"):
        os.remove("temp.txt")

    yield

    if os.path.exists("temp.txt"):
        os.remove("temp.txt")



def test_gravar_em_arquivo(obj,test_setup_teardown_arquivo):
    obj.gravar_em_arquivo("Teste Teste", "temp.txt")
    assert os.path.exists("temp.txt") == True

def test_ler_de_arquivo(obj,test_setup_teardown_arquivo):
    obj.gravar_em_arquivo("Teste Teste", "temp.txt")
    assert obj.ler_de_arquivo("temp.txt") == "Teste Teste"

@pytest.mark.parametrize("txt,txtInv",[("Hello", "olleH"),("oi","io")])
def test_inverter_string(obj,txt,txtInv):
    assert obj.inverter_string(txt) == txtInv

def test_contar_vogais(obj):
    assert obj.contar_vogais("Cerveja") == 3



@pytest.mark.parametrize("entrada,esperado",[(0,1),(1,1),(2,2),(3,6)])
def test_fatorial(obj,entrada,esperado):
    assert obj.fatorial(entrada) == esperado

def test_eh_par(obj):
    assert obj.eh_par(4) == True
    assert obj.eh_par(5) == False

def test_listar_arquivo(obj):
    assert "exercicio_pytest.py" in obj.listar_arquivos(".")

def test_calcular_media(obj):
    assert obj.calcular_media([1,2,3,4,5]) == 3


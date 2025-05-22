from nome_utils import normalizar_nome

def test_nome_simples():
    assert normalizar_nome("maria") == "Maria"

def test_nome_com_espacos_extras():
    assert normalizar_nome("   jOÃO   da  silva ") == "João Da Silva"

def test_nome_com_tudo_maiusculo():
    assert normalizar_nome("ANA BEATRIZ COSTA") == "Ana Beatriz Costa"

def test_nome_vazio():
    assert normalizar_nome("   ") == ""



    

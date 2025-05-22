from cpf_utils import validar_cpf
def test_cpf_valido():
    """CPF válido deve retornar True"""
    assert validar_cpf("52998224725") is True
def test_cpf_invalido_digitos():
    """CPF com dígitos verificadores errados deve retornar False"""
    assert validar_cpf("52998224700") is False
def test_cpf_com_caracteres_invalidos():
    """CPF com caracteres não numéricos deve retornar False"""
    assert validar_cpf("abc98224700") is False
def test_cpf_tamanho_invalido():
    """CPF com menos de 11 dígitos deve retornar False"""
    assert validar_cpf("123456789") is False
def test_cpf_todos_iguais():
    """CPF com todos os dígitos iguais deve retornar False"""
    assert validar_cpf("11111111111") is False



import pytest
from cadastro_usuarios import CadastroUsuario

# Teste de instância e validação
def test_instanciar_usuario_valido():
    usuario = CadastroUsuario("João Silva", "123.456.789-10", "01/01/1990", "Rua A, 123", "(11) 98765-4321", "senha123")
    assert usuario.nome == "João Silva"
    assert usuario.cpf == "123.456.789-10"
    assert usuario.nascimento == "01/01/1990"
    assert usuario.endereco == "Rua A, 123"
    assert usuario.telefone == "(11) 98765-4321"
    assert usuario.senha == "senha123"

# Testes de validação de nome
def test_validar_nome_valido():
    usuario = CadastroUsuario("João Silva", "123.456.789-10", "01/01/1990", "Rua A, 123", "(11) 98765-4321", "senha123")
    usuario.validar_nome()

def test_validar_nome_invalido():
    usuario = CadastroUsuario("João", "123.456.789-10", "01/01/1990", "Rua A, 123", "(11) 98765-4321", "senha123")
    with pytest.raises(ValueError):
        usuario.validar_nome()

# Testes de validação de CPF
def test_validar_cpf_valido():
    usuario = CadastroUsuario("João Silva", "123.456.789-10", "01/01/1990", "Rua A, 123", "(11) 98765-4321", "senha123")
    usuario.validar_cpf()

def test_validar_cpf_invalido():
    usuario = CadastroUsuario("João Silva", "12345678910", "01/01/1990", "Rua A, 123", "(11) 98765-4321", "senha123")
    with pytest.raises(ValueError):
        usuario.validar_cpf()

# Testes de validação de data de nascimento
def test_validar_nascimento_valido():
    usuario = CadastroUsuario("João Silva", "123.456.789-10", "01/01/1990", "Rua A, 123", "(11) 98765-4321", "senha123")
    usuario.validar_nascimento()

def test_validar_nascimento_invalido():
    usuario = CadastroUsuario("João Silva", "123.456.789-10", "01/01/3000", "Rua A, 123", "(11) 98765-4321", "senha123")
    with pytest.raises(ValueError):
        usuario.validar_nascimento()

def test_validar_nascimento_formato_invalido():
    usuario = CadastroUsuario("João Silva", "123.456.789-10", "1990-01-01", "Rua A, 123", "(11) 98765-4321", "senha123")
    with pytest.raises(ValueError):
        usuario.validar_nascimento()

# Testes de validação de endereço
def test_validar_endereco_valido():
    usuario = CadastroUsuario("João Silva", "123.456.789-10", "01/01/1990", "Rua A, 123", "(11) 98765-4321", "senha123")
    usuario.validar_endereco()

def test_validar_endereco_invalido():
    usuario = CadastroUsuario("João Silva", "123.456.789-10", "01/01/1990", "", "(11) 98765-4321", "senha123")
    with pytest.raises(ValueError):
        usuario.validar_endereco()

# Testes de validação de telefone
def test_validar_telefone_valido():
    usuario = CadastroUsuario("João Silva", "123.456.789-10", "01/01/1990", "Rua A, 123", "(11) 98765-4321", "senha123")
    usuario.validar_telefone()

def test_validar_telefone_invalido():
    usuario = CadastroUsuario("João Silva", "123.456.789-10", "01/01/1990", "Rua A, 123", "11987654321", "senha123")
    with pytest.raises(ValueError):
        usuario.validar_telefone()

# Testes de validação de senha
def test_validar_senha_valida():
    usuario = CadastroUsuario("João Silva", "123.456.789-10", "01/01/1990", "Rua A, 123", "(11) 98765-4321", "senha123")
    usuario.validar_senha()

def test_validar_senha_invalida():
    usuario = CadastroUsuario("João Silva", "123.456.789-10", "01/01/1990", "Rua A, 123", "(11) 98765-4321", "1234567")
    with pytest.raises(ValueError):
        usuario.validar_senha()

# Teste de exibição de informações
def test_mostrar_info(capsys):
    usuario = CadastroUsuario("João Silva", "123.456.789-10", "01/01/1990", "Rua A, 123", "(11) 98765-4321", "senha123")
    usuario.mostrar_info()
    captured = capsys.readouterr()
    assert "João Silva" in captured.out
    assert "123.456.789-10" in captured.out
    assert "01/01/1990" in captured.out
    assert "Rua A, 123" in captured.out
    assert "(11) 98765-4321" in captured.out

# Teste de gravação de informações
def test_gravar_info(tmpdir):
    usuario = CadastroUsuario("João Silva", "123.456.789-10", "01/01/1990", "Rua A, 123", "(11) 98765-4321", "senha123")
    nome_arquivo = tmpdir.join("cadastro_12345678910.txt")
    usuario.gravar_info()
    with open(f"cadastro_12345678910.txt", "r") as arquivo:
        conteudo = arquivo.read()
    assert "João Silva" in conteudo
    assert "123.456.789-10" in conteudo
    assert "01/01/1990" in conteudo
    assert "Rua A, 123" in conteudo
    assert "(11) 98765-4321" in conteudo

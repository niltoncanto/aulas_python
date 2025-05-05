import pytest
from cadastro_usuarios import CadastroUsuario

# Fixture para criar instâncias da classe CadastroUsuario
@pytest.fixture
def usuario_valido():
    return CadastroUsuario("João Silva", "123.456.789-10", "01/01/1990", "Rua A, 123", "(11) 98765-4321", "senha123")

# Fixture para criar um objeto com CPF inválido
@pytest.fixture
def usuario_cpf_invalido():
    return CadastroUsuario("João Silva", "12345678910", "01/01/1990", "Rua A, 123", "(11) 98765-4321", "senha123")

# Método setup para ser executado antes de cada teste
class TestCadastroUsuario:
    def setup_method(self):
        self.usuario = CadastroUsuario("João Silva", "123.456.789-10", "01/01/1990", "Rua A, 123", "(11) 98765-4321", "senha123")

    # Teste de instanciação com fixture
    def test_instanciar_usuario_valido(self, usuario_valido):
        assert usuario_valido.nome == "João Silva"
        assert usuario_valido.cpf == "123.456.789-10"
        assert usuario_valido.nascimento == "01/01/1990"
        assert usuario_valido.endereco == "Rua A, 123"
        assert usuario_valido.telefone == "(11) 98765-4321"
        assert usuario_valido.senha == "senha123"

    # Testes de validação de nome usando parametrize
    @pytest.mark.parametrize("nome, valido", [
        ("João Silva", True),
        ("João", False),
        ("", False)
    ])
    def test_validar_nome(self, nome, valido):
        self.usuario.nome = nome
        if valido:
            self.usuario.validar_nome()
        else:
            with pytest.raises(ValueError):
                self.usuario.validar_nome()

    # Testes de validação de CPF com fixture
    def test_validar_cpf_valido(self, usuario_valido):
        usuario_valido.validar_cpf()

    def test_validar_cpf_invalido(self, usuario_cpf_invalido):
        with pytest.raises(ValueError):
            usuario_cpf_invalido.validar_cpf()

    # Testes de validação de data de nascimento com parametrize
    @pytest.mark.parametrize("nascimento, valido", [
        ("01/01/1990", True),
        ("01/01/3000", False),
        ("1990-01-01", False)
    ])
    def test_validar_nascimento(self, nascimento, valido):
        self.usuario.nascimento = nascimento
        if valido:
            self.usuario.validar_nascimento()
        else:
            with pytest.raises(ValueError):
                self.usuario.validar_nascimento()

    # Testes de validação de endereço
    def test_validar_endereco_valido(self, usuario_valido):
        usuario_valido.validar_endereco()

    def test_validar_endereco_invalido(self):
        self.usuario.endereco = ""
        with pytest.raises(ValueError):
            self.usuario.validar_endereco()

    # Testes de validação de telefone com parametrize
    @pytest.mark.parametrize("telefone, valido", [
        ("(11) 98765-4321", True),
        ("11987654321", False),
        ("", False)
    ])
    def test_validar_telefone(self, telefone, valido):
        self.usuario.telefone = telefone
        if valido:
            self.usuario.validar_telefone()
        else:
            with pytest.raises(ValueError):
                self.usuario.validar_telefone()

    # Testes de validação de senha com parametrize
    @pytest.mark.parametrize("senha, valido", [
        ("senha123", True),
        ("1234567", False),
        ("", False)
    ])
    def test_validar_senha(self, senha, valido):
        self.usuario.senha = senha
        if valido:
            self.usuario.validar_senha()
        else:
            with pytest.raises(ValueError):
                self.usuario.validar_senha()

    # Teste de exibição de informações
    def test_mostrar_info(self, capsys, usuario_valido):
        usuario_valido.mostrar_info()
        captured = capsys.readouterr()
        assert "João Silva" in captured.out
        assert "123.456.789-10" in captured.out
        assert "01/01/1990" in captured.out
        assert "Rua A, 123" in captured.out
        assert "(11) 98765-4321" in captured.out

    # Teste de gravação de informações
    def test_gravar_info(self, tmpdir, usuario_valido):
        nome_arquivo = tmpdir.join("cadastro_12345678910.txt")
        usuario_valido.gravar_info()
        with open(f"cadastro_12345678910.txt", "r") as arquivo:
            conteudo = arquivo.read()
        assert "João Silva" in conteudo
        assert "123.456.789-10" in conteudo
        assert "01/01/1990" in conteudo
        assert "Rua A, 123" in conteudo
        assert "(11) 98765-4321" in conteudo

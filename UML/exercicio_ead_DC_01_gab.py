# Classe Estado
class Estado:
    def __init__(self, nome: str, sigla: str):
        self.nome = nome
        self.sigla = sigla

# Classe Cidade
class Cidade:
    def __init__(self, nome: str, estado: Estado):
        self.nome = nome
        self.estado = estado

# Classe Endereco
class Endereco:
    def __init__(self, rua: str, numero: int, bairro: str, cep: str, cidade: Cidade):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade

# Classe Funcionario
class Funcionario:
    def __init__(self, nome: str, nascimento: str, cpf: str, enderecos: Endereco):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.enderecos = enderecos
    
    def getNome(self) -> str:
        return self.nome
    
    def getNascimento(self) -> str:
        return self.nascimento
    
    def getCpf(self) -> str:
        return self.cpf
    
    def getEnderecos(self) -> Endereco:
        return self.enderecos

# Classe Vendedor herda Funcionario
class Vendedor(Funcionario):
    def __init__(self, nome: str, nascimento: str, cpf: str, enderecos: Endereco, equipe: 'EquipeVenda'):
        super().__init__(nome, nascimento, cpf, enderecos)
        self.equipe = equipe
    
    def getSalario(self) -> float:
        # Simulação de cálculo de salário
        return 3000.0

# Classe Gerente herda Funcionario
class Gerente(Funcionario):
    def getSalario(self) -> float:
        # Simulação de cálculo de salário
        return 5000.0

# Classe EquipeVenda
class EquipeVenda:
    def __init__(self, nome: str):
        self.nome = nome

estado_sp = Estado("São Paulo", "SP") 
cidade_sp = Cidade("São Paulo", estado_sp) 
endereco = Endereco("Rua Exemplo", 123, "Centro", "12345-678", cidade_sp) 
vendedor = Vendedor("João", "1980-05-10", "123.456.789-00", endereco,EquipeVenda("Equipe Alpha")) 
print(vendedor.getNome()) 
print(vendedor.getSalario())

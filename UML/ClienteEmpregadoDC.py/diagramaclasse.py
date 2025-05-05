from abc import ABC, abstractmethod

# Definindo a interface (IPessoa)
class IPessoa(ABC):
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    @abstractmethod
    def get_nome(self):
        pass

    @abstractmethod
    def get_documento(self):
        pass

# Definindo a classe Cliente, que é uma classe concreta
class Cliente:
    def __init__(self, nome, endereco, data_primeira_compra, data_ultima_compra, total_comprado):
        self.nome = nome
        self.endereco = endereco
        self.data_primeira_compra = data_primeira_compra
        self.data_ultima_compra = data_ultima_compra
        self.total_comprado = total_comprado

    def get_nome(self):
        return self.nome
    
    def calcular_credito(self):
        # Implementa cálculo de crédito permitido, por exemplo
        return 1000.0

# Cliente Pessoa Jurídica que herda de Cliente e implementa IPessoa
class ClientePJ(Cliente, IPessoa):
    def __init__(self, nome, endereco, data_primeira_compra, data_ultima_compra, total_comprado, cnpj):
        Cliente.__init__(self, nome, endereco, data_primeira_compra, data_ultima_compra, total_comprado)  # Chamando o construtor da classe Cliente
        IPessoa.__init__(self, nome, endereco)  # Chamando o construtor da interface IPessoa
        self.cnpj = cnpj

    def get_documento(self):
        return self.cnpj

# Cliente Pessoa Física que herda de Cliente e implementa IPessoa
class ClientePF(Cliente, IPessoa):
    def __init__(self, nome, endereco, data_primeira_compra, data_ultima_compra, total_comprado, cpf):
        Cliente.__init__(self, nome, endereco, data_primeira_compra, data_ultima_compra, total_comprado)  # Chamando o construtor da classe Cliente
        IPessoa.__init__(self, nome, endereco)  # Chamando o construtor da interface IPessoa
        self.cpf = cpf

    def get_documento(self):
        return self.cpf

# Classe Empregado que também implementa a interface IPessoa
class Empregado(IPessoa):
    def __init__(self, nome, endereco, cargo):
        IPessoa.__init__(self, nome, endereco)
        self.cargo = cargo

    def get_nome(self):
        return self.nome

    def get_documento(self):
        return "Documento do Empregado"

# Exemplo de uso
cliente_pf = ClientePF("João", "Rua A", "2020-01-01", "2023-01-01", 10000, "123.456.789-00")
cliente_pj = ClientePJ("Empresa XYZ", "Rua B", "2020-01-01", "2023-01-01", 20000, "00.123.456/0001-00")
empregado = Empregado("Carlos", "Rua C", "Vendedor")

print(cliente_pf.get_nome())  # João
print(cliente_pf.get_documento())  # 123.456.789-00
print(cliente_pj.get_documento())  # 00.123.456/0001-00
print(empregado.get_nome())  # Carlos

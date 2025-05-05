from abc import ABC, abstractmethod

# Classe abstrata Veiculo
class Veiculo(ABC):
    def __init__(self, marca, modelo, ano, preco_diaria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco_diaria = preco_diaria

    @abstractmethod
    def calcular_custo_locacao(self, dias):
        pass

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.ano}) - R${self.preco_diaria}/dia'

# Classe Carro
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, preco_diaria, numero_de_portas):
        super().__init__(marca, modelo, ano, preco_diaria)
        self.numero_de_portas = numero_de_portas

    def calcular_custo_locacao(self, dias):
        return self.preco_diaria * dias

# Classe Moto
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, preco_diaria, tipo_de_guincho):
        super().__init__(marca, modelo, ano, preco_diaria)
        self.tipo_de_guincho = tipo_de_guincho

    def calcular_custo_locacao(self, dias):
        return self.preco_diaria * dias

# Classe Caminhao
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, preco_diaria, capacidade_carga):
        super().__init__(marca, modelo, ano, preco_diaria)
        self.capacidade_carga = capacidade_carga

    def calcular_custo_locacao(self, dias):
        return self.preco_diaria * dias

# Classe Cliente
class Cliente:
    def __init__(self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.contratos = []

    def visualizar_contratos(self):
        return self.contratos

    def __str__(self):
        return f'{self.nome} - CPF: {self.cpf}'

# Classe Contrato
class Contrato:
    def __init__(self, cliente, veiculo, data_inicio, data_fim):
        self.cliente = cliente
        self.veiculo = veiculo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.custo_total = veiculo.calcular_custo_locacao((data_fim - data_inicio).days)
        cliente.contratos.append(self)

    def calcular_custo_total(self):
        return self.custo_total

    def __str__(self):
        return f'Contrato: {self.cliente} alugou {self.veiculo} de {self.data_inicio} até {self.data_fim} por R${self.custo_total}'

# Classe SistemaLocacao
class SistemaLocacao:
    def __init__(self):
        self.veiculos = []
        self.clientes = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def remover_veiculo(self, veiculo):
        self.veiculos.remove(veiculo)

    def listar_veiculos(self):
        for veiculo in self.veiculos:
            print(veiculo)

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def remover_cliente(self, cliente):
        self.clientes.remove(cliente)

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

    def criar_contrato(self, cliente, veiculo, data_inicio, data_fim):
        contrato = Contrato(cliente, veiculo, data_inicio, data_fim)
        print(f'Contrato criado: {contrato}')

class Menu:
    def menu():
        sistema = SistemaLocacao()
        while True:
                print("\nMENU")
                print("1. ADICIONAR CLIENTE")
                print("2. ADICIONAR VEÍCULO")
                print("3. LISTAR CLIENTES")
                print("4. LISTAR VEÍCULOS")
                print("5. CRIAR CONTRATO")
                print("6. EXCLUIR CLIENTE")
                print("7. EXCLUIR VEÍCULO")
                print("8. EXCLUIR CONTRATO")
                print("9. SAIR")
                
                escolha = input("Escolha uma opção: ")
                
                if escolha == "1":
                    nome = input("Nome do Cliente: ")
                    cpf = input("CPF do Cliente: ")
                    telefone = input("Telefone do Cliente: ")
                    endereco = input("Endereço do Cliente: ")
                    cliente = Cliente(nome, cpf, telefone, endereco)
                    sistema.adicionar_cliente(cliente)
                    print("Cliente adicionado com sucesso!")
                
                elif escolha == "2":
                    tipo_veiculo = input("Tipo de Veículo (Carro/Moto/Caminhao): ").lower()
                    marca = input("Marca: ")
                    modelo = input("Modelo: ")
                    ano = int(input("Ano: "))
                    preco_diaria = float(input("Preço da Diária: "))
                    
                    if tipo_veiculo == "carro":
                        numero_de_portas = int(input("Número de Portas: "))
                        veiculo = Carro(marca, modelo, ano, preco_diaria, numero_de_portas)
                    elif tipo_veiculo == "moto":
                        tipo_de_guincho = input("Tipo de Guincho: ")
                        veiculo = Moto(marca, modelo, ano, preco_diaria, tipo_de_guincho)
                    elif tipo_veiculo == "caminhao":
                        capacidade_carga = float(input("Capacidade de Carga (toneladas): "))
                        veiculo = Caminhao(marca, modelo, ano, preco_diaria, capacidade_carga)
                    else:
                        print("Tipo de veículo inválido.")
                        continue
                    
                    sistema.adicionar_veiculo(veiculo)
                    print("Veículo adicionado com sucesso!")
                
                elif escolha == "3":
                    print("Clientes cadastrados:")
                    sistema.listar_clientes()
                
                elif escolha == "4":
                    print("Veículos disponíveis:")
                    sistema.listar_veiculos()
                
                elif escolha == "5":
                    cpf_cliente = input("CPF do Cliente: ")
                    cliente = next((c for c in sistema.clientes if c.cpf == cpf_cliente), None)
                    if not cliente:
                        print("Cliente não encontrado.")
                        continue

                    print("Veículos disponíveis:")
                    sistema.listar_veiculos()
                    veiculo_index = int(input("Escolha o índice do veículo: ")) - 1
                    if veiculo_index < 0 or veiculo_index >= len(sistema.veiculos):
                        print("Índice de veículo inválido.")
                        continue
                    
                    veiculo = sistema.veiculos[veiculo_index]
                    data_inicio = input("Data de Início (AAAA-MM-DD): ")
                    data_fim = input("Data de Fim (AAAA-MM-DD): ")
                    data_inicio = date.fromisoformat(data_inicio)
                    data_fim = date.fromisoformat(data_fim)
                    
                    sistema.criar_contrato(cliente, veiculo, data_inicio, data_fim)
                
                elif escolha == "6":
                    cpf_cliente = input("CPF do Cliente a ser excluído: ")
                    cliente = next((c for c in sistema.clientes if c.cpf == cpf_cliente), None)
                    if cliente:
                        sistema.remover_cliente(cliente)
                        print("Cliente excluído com sucesso!")
                    else:
                        print("Cliente não encontrado.")
                
                elif escolha == "7":
                    print("Veículos disponíveis:")
                    sistema.listar_veiculos()
                    veiculo_index = int(input("Escolha o índice do veículo a ser excluído: ")) - 1
                    if veiculo_index < 0 or veiculo_index >= len(sistema.veiculos):
                        print("Índice de veículo inválido.")
                        continue
                    
                    veiculo = sistema.veiculos[veiculo_index]
                    sistema.remover_veiculo(veiculo)
                    print("Veículo excluído com sucesso!")
                
                elif escolha == "8":
                    print("Contratos do sistema:")
                    for i, contrato in enumerate([c for cliente in sistema.clientes for c in cliente.visualizar_contratos()]):
                        print(f"{i + 1}. {contrato}")
                    contrato_index = int(input("Escolha o índice do contrato a ser excluído: ")) - 1
                    contratos = [c for cliente in sistema.clientes for c in cliente.visualizar_contratos()]
                    if contrato_index < 0 or contrato_index >= len(contratos):
                        print("Índice de contrato inválido.")
                        continue
                    
                    contrato = contratos[contrato_index]
                    contrato.cliente.contratos.remove(contrato)
                    print("Contrato excluído com sucesso!")
                
                elif escolha == "9":
                    print("Saindo do sistema...")
                    break
                
                else:
                    print("Opção inválida. Tente novamente.")

# Execução do menu
if __name__ == "__main__":
    #menu()

    # Demonstração do Sistema
    from datetime import date
    # Criando o sistema
    sistema = SistemaLocacao()

    # Adicionando veículos
    carro = Carro("Toyota", "Corolla", 2020, 150.0, 4)
    moto = Moto("Honda", "CB500", 2019, 100.0, "Corrente")
    caminhao = Caminhao("Volvo", "FH", 2018, 300.0, 20.0)

    sistema.adicionar_veiculo(carro)
    sistema.adicionar_veiculo(moto)
    sistema.adicionar_veiculo(caminhao)

    # Listando veículos disponíveis
    print("Veículos disponíveis:")
    sistema.listar_veiculos()

    # Adicionando clientes
    cliente1 = Cliente("João Silva", "123.456.789-00", "1234-5678", "Rua A, 123")
    cliente2 = Cliente("Maria Souza", "987.654.321-00", "8765-4321", "Rua B, 456")

    sistema.adicionar_cliente(cliente1)
    sistema.adicionar_cliente(cliente2)

    # Listando clientes
    print("\nClientes cadastrados:")
    sistema.listar_clientes()

    # Criando contrato de locação
    sistema.criar_contrato(cliente1, carro, date(2024, 9, 1), date(2024, 9, 5))
    sistema.criar_contrato(cliente2, moto, date(2024, 9, 2), date(2024, 9, 3))

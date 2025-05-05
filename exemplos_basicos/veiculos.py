from abc import ABC, abstractmethod

# Classe Abstrata Veiculo
class Veiculo(ABC):
    # Construtor da classe Veiculo
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca  # Marca do veículo
        self.modelo = modelo  # Modelo do veículo
        self.ano = ano  # Ano de fabricação do veículo
        self.preco = preco  # Preço do veículo

    # Método abstrato para exibir detalhes do veículo
    @abstractmethod
    def exibir_detalhes(self):
        pass

# Classe VeiculoNovo (herda de Veiculo)
class VeiculoNovo(Veiculo):
    # Construtor da classe VeiculoNovo
    def __init__(self, marca, modelo, ano, preco, garantia_anos):
        super().__init__(marca, modelo, ano, preco)  # Chama o construtor da classe base
        self.garantia_anos = garantia_anos  # Garantia em anos do veículo novo

    # Implementação do método abstrato para exibir detalhes do veículo novo
    def exibir_detalhes(self):
        print(f"[Novo] Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Preço: R${self.preco}, Garantia: {self.garantia_anos} anos")

# Classe VeiculoUsado (herda de Veiculo)
class VeiculoUsado(Veiculo):
    # Construtor da classe VeiculoUsado
    def __init__(self, marca, modelo, ano, preco, quilometragem, unico_dono):
        super().__init__(marca, modelo, ano, preco)  # Chama o construtor da classe base
        self.quilometragem = quilometragem  # Quilometragem do veículo usado
        self.unico_dono = unico_dono  # Indica se o veículo teve um único dono

    # Implementação do método abstrato para exibir detalhes do veículo usado
    def exibir_detalhes(self):
        dono = "Sim" if self.unico_dono else "Não"  # Define se o veículo teve um único dono
        print(f"[Usado] Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Preço: R${self.preco}, Quilometragem: {self.quilometragem} km, Único dono: {dono}")

# Classe Concessionaria
class Concessionaria:
    # Construtor da classe Concessionaria
    def __init__(self):
        self.veiculos = {}  # Dicionário de veículos disponíveis, com ID único como chave
        self.vendas = []  # Lista de veículos vendidos
        self.id_atual = 1  # ID único atual para cadastrar veículos

    # Método para cadastrar um novo veículo
    def cadastrar_veiculo(self, veiculo):
        self.veiculos[self.id_atual] = veiculo  # Adiciona o veículo ao dicionário de veículos
        print(f"Veículo cadastrado com ID {self.id_atual}")
        self.id_atual += 1  # Incrementa o ID único

    # Método para registrar a venda de um veículo
    def registrar_venda(self, veiculo_id):
        if veiculo_id in self.veiculos:  # Verifica se o ID do veículo existe
            veiculo = self.veiculos.pop(veiculo_id)  # Remove o veículo do estoque
            self.vendas.append(veiculo)  # Adiciona o veículo à lista de vendas
            print(f"Veículo ID {veiculo_id} vendido com sucesso!")
        else:
            print("ID inválido. Veículo não encontrado.")

    # Método para exibir os veículos em estoque
    def exibir_estoque(self):
        if not self.veiculos:  # Verifica se não há veículos em estoque
            print("Não há veículos em estoque.")
        else:
            for veiculo_id, veiculo in self.veiculos.items():  # Itera sobre os veículos em estoque
                print(f"ID: {veiculo_id}")
                veiculo.exibir_detalhes()  # Exibe os detalhes do veículo

    # Método para exibir os veículos vendidos
    def exibir_vendas(self):
        if not self.vendas:  # Verifica se não há veículos vendidos
            print("Nenhum veículo vendido até o momento.")
        else:
            for veiculo in self.vendas:  # Itera sobre os veículos vendidos
                veiculo.exibir_detalhes()  # Exibe os detalhes do veículo

# Função principal para executar o programa
def main():
    concessionaria = Concessionaria()  # Cria uma instância da Concessionaria
    while True:
        # Exibe o menu de opções
        print("\n--- Menu ---")
        print("1. Cadastrar Veículo")
        print("2. Registrar Venda")
        print("3. Exibir Estoque")
        print("4. Exibir Vendas")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        # Cadastrar Veículo
        if opcao == "1":
            tipo = input("Tipo de veículo (1 - Novo, 2 - Usado): ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            ano = input("Ano: ")
            preco = float(input("Preço: "))

            # Verifica o tipo de veículo para cadastro
            if tipo == "1":
                garantia_anos = int(input("Garantia (em anos): "))
                veiculo = VeiculoNovo(marca, modelo, ano, preco, garantia_anos)  # Cria um VeiculoNovo
            elif tipo == "2":
                quilometragem = int(input("Quilometragem: "))
                unico_dono = input("Único dono (s/n): ").lower() == 's'
                veiculo = VeiculoUsado(marca, modelo, ano, preco, quilometragem, unico_dono)  # Cria um VeiculoUsado
            else:
                print("Opção inválida!")
                continue

            concessionaria.cadastrar_veiculo(veiculo)  # Cadastra o veículo na concessionária

        # Registrar Venda
        elif opcao == "2":
            concessionaria.exibir_estoque()  # Exibe o estoque atual
            veiculo_id = int(input("Digite o ID do veículo para registrar a venda: "))
            concessionaria.registrar_venda(veiculo_id)  # Registra a venda do veículo

        # Exibir Estoque
        elif opcao == "3":
            concessionaria.exibir_estoque()  # Exibe o estoque atual

        # Exibir Vendas
        elif opcao == "4":
            concessionaria.exibir_vendas()  # Exibe os veículos vendidos

        # Sair
        elif opcao == "5":
            print("Saindo... Obrigado por usar o sistema!")
            break  # Encerra o loop e o programa

        # Opção Inválida
        else:
            print("Opção inválida. Tente novamente.")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal para executar o programa
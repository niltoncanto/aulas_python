# Classe base Veiculo, contendo os atributos e métodos comuns para todos os tipos de veículos.
class Veiculo:
    def __init__(self, marca, modelo, preco_base):
        # Atributos comuns a todos os veículos
        self.marca = marca
        self.modelo = modelo
        self.preco_base = preco_base

    def calcular_valor_venda(self):
        # Método abstrato para ser implementado pelas subclasses
        raise NotImplementedError("Subclasses devem implementar este método!")

# Subclasse Carro que herda de Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, preco_base, num_portas, ar_condicionado):
        # Inicializa os atributos herdados de Veiculo
        super().__init__(marca, modelo, preco_base)
        # Atributos específicos da classe Carro
        self.num_portas = num_portas
        self.ar_condicionado = ar_condicionado

    def calcular_valor_venda(self):
        # Valor adicional se o carro possuir ar condicionado
        valor_ac = 5000 if self.ar_condicionado else 0
        # O valor de venda é o preço base mais o valor adicional (se houver)
        return self.preco_base + valor_ac


# Subclasse Moto que herda de Veiculo
class Moto(Veiculo):
    def __init__(self, marca, modelo, preco_base, cilindradas):
        # Inicializa os atributos herdados de Veiculo
        super().__init__(marca, modelo, preco_base)
        # Atributo específico da classe Moto
        self.cilindradas = cilindradas

    def calcular_valor_venda(self):
        # O valor de venda é o preço base ajustado pelo número de cilindradas
        return self.preco_base + (self.cilindradas * 10)


# Subclasse Caminhao que herda de Veiculo
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, preco_base, capacidade_carga, eixos):
        # Inicializa os atributos herdados de Veiculo
        super().__init__(marca, modelo, preco_base)
        # Atributos específicos da classe Caminhao
        self.capacidade_carga = capacidade_carga
        self.eixos = eixos

    def calcular_valor_venda(self):
        # O valor de venda é o preço base ajustado pela capacidade de carga e número de eixos
        return self.preco_base + (self.capacidade_carga * 20) + (self.eixos * 1000)


# Classe Concessionaria que gerencia os veículos
class Concessionaria:
    def __init__(self):
        # A lista de veículos que a concessionária possui
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        # Método para adicionar um novo veículo à lista
        self.veiculos.append(veiculo)

    def calcular_valor_estoque(self):
        # Calcula o valor total do estoque somando o valor de venda de cada veículo
        valor_total = 0
        for veiculo in self.veiculos:
            valor_total += veiculo.calcular_valor_venda()
        return valor_total

    def exibir_menu(self):
        # Exibe o menu e permite a interação com o usuário
        while True:
            print("\n--- Menu da Concessionária ---")
            print("1. Incluir Veículo")
            print("2. Calcular Valor do Estoque")
            print("3. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.incluir_veiculo_menu()
            elif opcao == "2":
                valor = self.calcular_valor_estoque()
                print(f"O valor total do estoque é: R$ {valor:.2f}")
            elif opcao == "3":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def incluir_veiculo_menu(self):
        # Solicita informações para adicionar um novo veículo
        print("\n--- Incluir Veículo ---")
        tipo = input("Informe o tipo de veículo (carro/moto/caminhao): ").lower()

        marca = input("Marca: ")
        modelo = input("Modelo: ")
        preco_base = float(input("Preço base: R$ "))

        if tipo == "carro":
            num_portas = int(input("Número de portas: "))
            ar_condicionado = input("Possui ar-condicionado? (s/n): ").lower() == 's'
            carro = Carro(marca, modelo, preco_base, num_portas, ar_condicionado)
            self.adicionar_veiculo(carro)
        elif tipo == "moto":
            cilindradas = int(input("Cilindradas: "))
            moto = Moto(marca, modelo, preco_base, cilindradas)
            self.adicionar_veiculo(moto)
        elif tipo == "caminhao":
            capacidade_carga = int(input("Capacidade de carga (toneladas): "))
            eixos = int(input("Número de eixos: "))
            caminhao = Caminhao(marca, modelo, preco_base, capacidade_carga, eixos)
            self.adicionar_veiculo(caminhao)
        else:
            print("Tipo de veículo inválido.")


# Exemplo de uso do sistema
concessionaria = Concessionaria()
concessionaria.exibir_menu()

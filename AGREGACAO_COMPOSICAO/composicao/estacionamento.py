class Veiculo:
    def __init__(self, placa, modelo, cor):
        self.placa = placa
        self.modelo = modelo
        self.cor = cor

class Motorista:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

class RegistroEstacionamento:
    def __init__(self, veiculo, data_entrada):
        self.veiculo = veiculo
        self.data_entrada = data_entrada
        self.data_saida = None

class ControleEstacionamento:
    def __init__(self, motorista):
        self.motorista = motorista
        self.registros = []

    def registrar_entrada(self, veiculo, data_entrada):
        registro = RegistroEstacionamento(veiculo, data_entrada)
        self.registros.append(registro)

    def registrar_saida(self, placa, data_saida):
        for registro in self.registros:
            if registro.veiculo.placa == placa and registro.data_saida is None:
                registro.data_saida = data_saida
                return True
        return False

    def listar_registros(self):
        for registro in self.registros:
            status = f"Entrada: {registro.data_entrada}, Saída: {registro.data_saida}" 
            if registro.data_saida 
            else 
            f"Entrada: {registro.data_entrada}, Saída: Pendente"
            print(f"Veículo: {registro.veiculo.placa} - {registro.veiculo.modelo} ({registro.veiculo.cor}) - {status}")

class Estacionamento:
    def __init__(self):
        self.veiculos = {}
        self.motoristas = {}
        self.registros_estacionamento = []

    def incluir_veiculo(self):
        placa = input("Placa do veículo: ")
        modelo = input("Modelo do veículo: ")
        cor = input("Cor do veículo: ")
        self.veiculos[placa] = Veiculo(placa, modelo, cor)
        print("Veículo adicionado com sucesso!")

    def incluir_motorista(self):
        nome = input("Nome do motorista: ")
        cpf = input("CPF do motorista: ")
        telefone = input("Telefone do motorista: ")
        self.motoristas[cpf] = Motorista(nome, cpf, telefone)
        print("Motorista adicionado com sucesso!")

    def registrar_entrada(self):
        cpf = input("Informe o CPF do motorista: ")
        placa = input("Informe a placa do veículo: ")
        data_entrada = input("Data de entrada (DD/MM/AAAA): ")

        if cpf in self.motoristas and placa in self.veiculos:
            motorista = self.motoristas[cpf]
            veiculo = self.veiculos[placa]
            controle = ControleEstacionamento(motorista)
            controle.registrar_entrada(veiculo, data_entrada)
            self.registros_estacionamento.append(controle)
            print("Entrada registrada com sucesso!")
        else:
            print("Motorista ou veículo não encontrados.")

    def registrar_saida(self):
        placa = input("Informe a placa do veículo: ")
        data_saida = input("Data de saída (DD/MM/AAAA): ")

        for registro in self.registros_estacionamento:
            if registro.registrar_saida(placa, data_saida):
                print("Saída registrada com sucesso!")
                return
        print("Veículo não encontrado ou já saiu.")

    def ver_registros(self):
        for controle in self.registros_estacionamento:
            print(f"Motorista: {controle.motorista.nome}")
            controle.listar_registros()

    def exibir_menu(self):
        while True:
            print("\n--- Menu do Estacionamento ---")
            print("1. Incluir Veículo")
            print("2. Incluir Motorista")
            print("3. Registrar Entrada")
            print("4. Registrar Saída")
            print("5. Ver Registros")
            print("6. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.incluir_veiculo()
            elif opcao == "2":
                self.incluir_motorista()
            elif opcao == "3":
                self.registrar_entrada()
            elif opcao == "4":
                self.registrar_saida()
            elif opcao == "5":
                self.ver_registros()
            elif opcao == "6":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Execução do programa
estacionamento = Estacionamento()
estacionamento.exibir_menu()

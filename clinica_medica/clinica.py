from datetime import datetime

class Pessoa:
    # Construtor da classe Pessoa, base para Paciente e Medico
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Paciente(Pessoa):
    # Construtor da classe Paciente, herdando de Pessoa
    def __init__(self, nome, cpf, data_nascimento):
        super().__init__(nome, cpf, data_nascimento)

class Medico(Pessoa):
    # Construtor da classe Medico, herdando de Pessoa e adicionando CRM e especialidade
    def __init__(self, nome, cpf, data_nascimento, crm, especialidade):
        super().__init__(nome, cpf, data_nascimento)
        self.crm = crm
        self.especialidade = especialidade

class Consulta:
    # Construtor da classe Consulta
    def __init__(self, paciente, medico, data_hora, observacoes):
        self.paciente = paciente
        self.medico = medico
        self.data_hora = data_hora
        self.observacoes = observacoes

class Menu:
    def __init__(self):
        # Dicionários para armazenar médicos e pacientes, e uma lista para as consultas
        self.medicos = {}
        self.pacientes = {}
        self.consultas = []

    def incluir_medico(self):
        # Solicita dados do médico e o adiciona ao dicionário
        nome = input("Nome do médico: ")
        cpf = input("CPF do médico: ")
        while True:
            data_nascimento_str = input("Data de nascimento (YYYY-MM-DD): ")
            try:
                data_nascimento = datetime.strptime(data_nascimento_str, '%Y-%m-%d')
                break
            except ValueError:
                print("Formato de data inválido. Por favor, use o formato YYYY-MM-DD.")
        crm = input("CRM: ")
        especialidade = input("Especialidade: ")
        medico = Medico(nome, cpf, data_nascimento, crm, especialidade)
        self.medicos[crm] = medico

    def incluir_paciente(self):
        # Solicita dados do paciente e o adiciona ao dicionário
        nome = input("Nome do paciente: ")
        cpf = input("CPF do paciente: ")
        while True:
            data_nascimento_str = input("Data de nascimento (YYYY-MM-DD): ")
            try:
                data_nascimento = datetime.strptime(data_nascimento_str, '%Y-%m-%d')
                break
            except ValueError:
                print("Formato de data inválido. Por favor, use o formato YYYY-MM-DD.")
        paciente = Paciente(nome, cpf, data_nascimento)
        self.pacientes[cpf] = paciente

    def agendar_consulta(self):
        # Permite agendar uma consulta
        cpf_paciente = input("CPF do paciente: ")
        crm_medico = input("CRM do médico: ")
        while True:
            data_hora_str = input("Data e hora da consulta (YYYY-MM-DD HH:MM): ")
            try:
                data_hora = datetime.strptime(data_hora_str, '%Y-%m-%d %H:%M')
                break
            except ValueError:
                print("Formato de data inválido. Por favor, use o formato YYYY-MM-DD HH:MM.")
        observacoes = input("Observações: ")
        if cpf_paciente in self.pacientes and crm_medico in self.medicos:
            consulta = Consulta(self.pacientes[cpf_paciente], self.medicos[crm_medico], data_hora, observacoes)
            self.consultas.append(consulta)
        else:
            print("Médico ou paciente não encontrado.")
    
    def ver_agenda(self):
            # Método para exibir todas as consultas agendadas
            if not self.consultas:
                print("Nenhuma consulta agendada.")
                return
            for consulta in self.consultas:
                print(f"Consulta agendada para {consulta.data_hora} - Médico: {consulta.medico.nome}, Paciente: {consulta.paciente.nome}")
    
    def exibir_menu(self):
        # Exibe as opções do menu e permite a interação com o usuário
        while True:
            print("\nMenu de Opções:")
            print("1. Incluir Médico")
            print("2. Incluir Paciente")
            print("3. Agendar Consulta")
            print("4. Ver consultas")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.incluir_medico()
            elif opcao == "2":
                self.incluir_paciente()
            elif opcao == "3":
                self.agendar_consulta()
            elif opcao == "4":
                self.ver_agenda()
            elif opcao == "5":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")

# Executando o sistema
menu = Menu()
menu.exibir_menu()

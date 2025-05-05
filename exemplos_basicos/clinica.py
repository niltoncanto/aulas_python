import time
from datetime import datetime  
class Pessoa:
  def __init__(self,nome,cpf,data_nascimento):
    self.nome = nome
    self.cpf = cpf
    self.data_nascimento = data_nascimento
    def __str__(self):
           return f"Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}"

class Paciente(Pessoa):
  pass

class Medico(Pessoa):
    def __init__(self,nome,cpf,data_nascimento,crm,especialidade):
        self.crm = crm
        self.especialidade = especialidade
        super().__init__(nome,cpf,data_nascimento)
    def __str__(self):
           return f"Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}, CRM: {self.crm}, Especialidade: {self.especialidade}"

class Consulta:
  def __init__(self,paciente,medico,data_hora,observacoes):
    self.paciente = paciente
    self.medico = medico
    self.data_hora = data_hora
    self.observacoes = observacoes

    def __str__(self):
           return f"Paciente: {self.paciente.nome}"

class Menu:
    def __init__(self):
        self.medicos ={}
        self.pacientes ={}
        self.consultas=[]
    
    def incluir_medico(self):
        nome = input("Nome do Médico:")
        cpf = input("CPF do Médico:")
        data_nascimento_usuario = input("Data de Nascimento do Médico:")
        #data_nascimento = datetime.strptime(data_nascimento_usuario, "%d/%m/%Y")
        crm = input("crm do Médico:")
        especialidade = input("Especialidade do Médico:")
        self.medicos[crm] = Medico(nome,cpf,data_nascimento_usuario,crm,especialidade)

    def incluir_paciente(self):
        nome = input("Nome do Paciente:")
        cpf = input("CPF do Paciente:")
        data_nascimento = input("Data de Nascimento do Paciente:")
        self.pacientes[cpf] = Paciente(nome,cpf,data_nascimento)
    
    def agendar_consulta(self):
        cpf_paciente = input("CPF do Paciente:")
        if cpf_paciente in self.pacientes:
            paciente = self.pacientes.get(cpf_paciente)
        else:
            return f"paciente {cpf_paciente} não encontrado"    
        
        crm_medico = input("CRM do Médico:")
        if crm_medico in self.medicos:
            medico = self.medicos.get(crm_medico)
        else:
            return f"paciente {cpf_paciente} não encontrado" 
        data_hora_usuario = input("Data e hora da consulta dd/mm/aaaa hh:mm:")
        #data_hora = datetime.strptime(data_hora_usuario,'%d/%m/%Y %H:%M')
        observacoes = input("Observações:")
        self.consultas.append(Consulta(paciente,medico,data_hora_usuario,observacoes))
        return f"Consulta agendada com sucesso!"
    
    def listar_medicos(self):
      for v in self.medicos.values():
        print(v)

    def listar_pacientes(self):
      for v in self.pacientes.values():
        print(v)

    def listar_consultas(self):
      for i in self.consultas:
        print(i.paciente.nome,i.medico.nome,i.data_hora)

    def exibir_menu(self):
        while True:
            print("**Escolha sua Opção**")
            print("1.Incluir Médico")
            print("2.Incluir Paciente")
            print("3.Agendar Consulta")
            print("4.Listar Médicos")
            print("5.Listar Pacientes")
            print("6.Listar Consultas")
            print("7.Sair")
            opcao = int(input("Opção: "))
            if opcao==1:
                self.incluir_medico()
            elif opcao == 2:
                self.incluir_paciente()
            elif opcao ==3:
                print(self.agendar_consulta())
            elif opcao == 4:
                self.listar_medicos()
            elif opcao == 5:
                self.listar_pacientes()
            elif opcao == 6:
                self.listar_consultas()
            elif opcao == 7:
                print("Saindo do sistema...")
                time.sleep(2)
                break       
            else:
                return f"Opção inválida!"
      
menu = Menu()
menu.exibir_menu()
paciente = Paciente("Nome","cpf","nascimento")
medico = Medico("Nome","cpf","nascimento","crm","especialidade")
consulta = Consulta(paciente,medico,'data_hora_usuario','observacoes')
print(consulta.paciente)
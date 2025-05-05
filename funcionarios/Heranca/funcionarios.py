from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, cpf, salario_base):
        self.nome = nome
        self.cpf = cpf
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass

class Administrativo(Funcionario):
    def __init__(self, nome, cpf, salario_base, departamento):
        super().__init__(nome, cpf, salario_base)
        self.departamento = departamento

    def calcular_salario(self):
        return self.salario_base

class Professor(Funcionario):
    def __init__(self, nome, cpf, salario_base, titulacao, horas_aula):
        super().__init__(nome, cpf, salario_base)
        self.titulacao = titulacao
        self.horas_aula = horas_aula

    def calcular_salario(self):
        return self.horas_aula * 100

class Tecnico(Funcionario):
    def __init__(self, nome, cpf, salario_base, cargo):
        super().__init__(nome, cpf, salario_base)
        self.cargo = cargo

    def calcular_salario(self):
        return self.salario_base + 500

class Empresa:
    def __init__(self):
        self.funcionarios = []

    def incluir_funcionario(self):
        tipo = input("Tipo de funcionário (1-Administrativo, 2-Professor, 3-Técnico): ")
        nome = input("Nome do funcionário: ")
        cpf = input("CPF do funcionário: ")
        salario_base = float(input("Salário base do funcionário: "))

        if tipo == "1":
            departamento = input("Departamento: ")
            funcionario = Administrativo(nome, cpf, salario_base, departamento)
        elif tipo == "2":
            titulacao = input("Titulação: ")
            horas_aula = int(input("Horas de aula semanais: "))
            funcionario = Professor(nome, cpf, salario_base, titulacao, horas_aula)
        elif tipo == "3":
            cargo = input("Cargo: ")
            funcionario = Tecnico(nome, cpf, salario_base, cargo)
        else:
            print("Tipo inválido!")
            return

        self.funcionarios.append(funcionario)
        print("Funcionário cadastrado com sucesso!")

    def calcular_folha_pagamento(self):
        total = sum(funcionario.calcular_salario() for funcionario in self.funcionarios)
        print(f"Folha de pagamento total: R${total:.2f}")

    def exibir_menu(self):
        while True:
            print("\nMenu:")
            print("1. Incluir Funcionário")
            print("2. Calcular Folha de Pagamento")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.incluir_funcionario()
            elif opcao == "2":
                self.calcular_folha_pagamento()
            elif opcao == "3":
                break
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    empresa = Empresa()
    empresa.exibir_menu()

# Objetivo: Desenvolver um sistema para gerenciar uma empresa com diferentes tipos de funcionários, incluindo salários, cargos e bonificações.
#  Parte 1: Definir Classes
# 1. Classe Funcionário: 
#    - Atributos: nome, ID, salário.
#    - Métodos: mostrar_detalhes, calcular_bonificacao.
# 2. Classe Gerente (herda de Funcionário):
# 
# 3. Classe Engenheiro (herda de Funcionário):
#    - Atributo adicionais: especialidade (por exemplo, software, hardware).
#    - Método  mostrar_detalhes (sobrescrito)

class Funcionario:
    id = 1000
    def __init__(self,nome,salario,departamento):
        self.nome = nome
        Funcionario.id += 1
        self.salario = salario
        self.departamento = departamento

    def mostrar_detalhes(self):
        return self.id,self.nome,self.salario,self.departamento

    def calcular_bonificacao(self,taxa_bonus):
        return float(self.salario)*taxa_bonus

class Gerente(Funcionario):
    def __init__(self,nome,salario,departamento):
        super().__init__(nome,salario,departamento)

class Engenheiro(Funcionario):
    def __init__(self,nome,salario,departamento,especialidade):
        self.especialidade = especialidade
        super().__init__(nome,salario,departamento)

    def mostrar_detalhes(self):
        return str(super().mostrar_detalhes()),str(self.especialidade)

func1 = Funcionario("João","2000","TI")
func2 = Funcionario("Marcos","2500","TI")
gerente = Gerente("Paulo","20000","TI")
engenheiro1 = Engenheiro("Carlos",15000,"TI","Software")
engenheiro2 = Engenheiro("Antonio",17000,"TI","Redes")
print(func1.calcular_bonificacao(0.1))
print(gerente.calcular_bonificacao(0.7))
print(engenheiro1.calcular_bonificacao(0.5))
print(gerente.mostrar_detalhes())
print(engenheiro1.mostrar_detalhes())

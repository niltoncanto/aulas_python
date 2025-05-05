'''Parte 1: Definir Classes
1. Classe Funcionário: 
   - Atributos: nome, ID, salário.
   - Métodos: mostrar_detalhes, calcular_bonificacao.'''

class Funcionario:
    contador = 1000
    BONIFICACAO = 0.10
    lista_funcionarios = []
    def __init__(self,nome,salario):
        self.id = Funcionario.contador
        Funcionario.contador+=1
        self.salario = salario
        self.nome = nome
        self.lista_funcionarios.append(self)

    def mostrar_detalhes(self):
        print("id:" + str(self.id))
        print("Nome:" + self.nome)
        print("Salario:" + str(self.salario))

    def calcular_bonificacao(self):
        return self.salario*self.BONIFICACAO
    




'''2. Classe Gerente (herda de Funcionário):
   - Atributos adicionais: equipe (lista de funcionários sob a gestão).
   - Métodos adicionais: adicionar_funcionario, remover_funcionario.'''
from funcionario import Funcionario
class Gerente(Funcionario):
      BONIFICACAO_GERENTE=0.30
      bonificacao_total = 0
      salario_total =0
      def __init__(self,nome,salario):
         super().__init__(nome,salario)
         self.equipe=[]
    
      def adicionar_funcionario_equipe(self,funcionario):
        self.equipe.append(funcionario)

      def remover_funcionario_equipe(self,funcionario):
        self.equipe.remove(funcionario)

      def calcular_bonificacao(self):
         return self.salario*self.BONIFICACAO_GERENTE
      
      def calcular_salario_total(self):
        for func in self.equipe:
            Gerente.salario_total = Gerente.salario_total + func.salario
        return Gerente.salario_total
      
      def calcular_bonificacao_total(self):
        for func in self.equipe:
            self.bonificacao_total += func.calcular_bonificacao()
        return self.bonificacao_total


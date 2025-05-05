'''3. Classe Engenheiro (herda de Funcionário):
   - Atributos adicionais: area (por exemplo, software, hardware).
'''
from funcionario import Funcionario
class Engenheiro(Funcionario):
    def __init__(self,nome,salario,departamento):
        super().__init__(nome,salario)
        self.departamento = departamento
   
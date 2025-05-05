from departamento import Departamento
from funcionario import Funcionario
from gerente import Gerente
from engenheiro import Engenheiro

def main():
    financeiro = Departamento()
    rh = Departamento()
    ti = Departamento()
    func1 = Funcionario("Ana",3000.0)
    func2 = Funcionario("João",4000.0)
    func3 = Funcionario("Pedro",2500.0)
    func4 = Funcionario("Manuel",2000.0)
    func5 = Funcionario("Felipe",6000.0)
    gerente1 = Gerente("Ricardo",10000.0)
    gerente2 = Gerente("Paulo",15000.0)
    gerente3 = Gerente("Joel",20000.0)
    engenheiro1 = Engenheiro("Maria",12000.0,"software")
    engenheiro2 = Engenheiro("Carlos",10000.0,"infra")
    engenheiro3 = Engenheiro("Mario",13000.0,"hardware")

    #Adicionando funcionários ao departamento
    gerente1.adicionar_funcionario_equipe(func1)
    gerente1.adicionar_funcionario_equipe(func2)
    gerente1.adicionar_funcionario_equipe(func3)
    gerente1.adicionar_funcionario_equipe(engenheiro1)
    gerente1.adicionar_funcionario_equipe(engenheiro2)
    gerente1.adicionar_funcionario_equipe(engenheiro3)
    gerente2.adicionar_funcionario_equipe(func4)
    gerente3.adicionar_funcionario_equipe(func5)
    print("*************************************************")
    print("Salário Total do Departamento: " + str(gerente1.calcular_salario_total()))
    print("Bonificação Total do Departamento: " + str(gerente1.calcular_bonificacao_total()))
    print("Bonificação do Gerente de TI: " + str(gerente1.calcular_bonificacao()))
    print("*************************************************")
    func2.mostrar_detalhes()
    print("Bonificação do Funcionario João: " + str(func2.calcular_bonificacao()))
    print("*************************************************")

if __name__=="__main__":
    main()

from conexao_bd import ConexaoBD
from conta_bancaria import ContaBancaria
from dao_conta import ContaBancariaDAO

if __name__ == "__main__":
    conexao = ConexaoBD()
    conexao.criar_tabela_contas()
    

    # Criar uma nova conta bancária
    conta1 = ContaBancaria("12345-6", "João Silva", 1000, 500)
    
    # Exibir informações da conta
    conta1.exibir_informacoes()
    
    # Depositar e sacar valores
    conta1.depositar(500)
    conta1.sacar(700)
    
    # Exibir o saldo atualizado
    print(f"Saldo atualizado: {conta1.get_saldo()}")
    
    # Salvar a conta no banco de dados
    salvar_conta(conta1)
    
    # Listar todas as contas no banco
    listar_contas()

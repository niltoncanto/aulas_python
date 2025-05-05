from conexao_bd import conexaoBD
from conta_bancaria import ContaBancaria
from dao_conta import ContaBancariaDAO

if __name__ == '__main__':
    conexao = conexaoBD()  # cria a conexão
    conexao.criar_tabela()  # cria a tabela contas

    conta1 = ContaBancaria(112344, "João Paulo", 2000, 5000)  # cria a conta1
    conta2 = ContaBancaria(22222, "Ana Maria", 5000, 15000)   # cria a conta2
    
    conta1.exibir_info()  # exibe informações da conta1

    conta1.depositar(300)  # deposita 300
    conta1.sacar(700)  # saca 700 da conta1

    conta1.exibir_info()  # exibe informações atualizadas

    conta_dao = ContaBancariaDAO(conexao)  # cria objeto dao_conta
    conta_dao.salvar_conta(conta1)  # salva conta1 no banco
    conta_dao.salvar_conta(conta2)  # salva conta2 no banco
    
    conexao.fechar_conexao()  # fecha a conexãoe
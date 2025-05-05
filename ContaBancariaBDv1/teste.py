import sqlite3
class conexaoBD:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("banco.db")
            self.cursor = self.conn.cursor()  # Inicializando o cursor
            print("Conexão estabelecida com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def criar_tabela(self):
        if self.conn:
            try:
                self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS contas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero_conta INTEGER NOT NULL,
                titular TEXT NOT NULL,
                saldo REAL NOT NULL,
                limite REAL NOT NULL)''')
                self.conn.commit()
                print("Tabela criada com sucesso!")
            except sqlite3.Error as e:
                print(f"Erro ao criar tabela: {e}")
        else:
            print("Não há conexão com o BD.")

    def fechar_conexao(self):
        if self.conn:
            try:
                self.conn.close()
                print('Conexão encerrada com o BD.')
            except sqlite3.Error as e:
                print(f"Erro ao fechar a conexão: {e}")

class ContaBancaria:
    def __init__(self, numero_conta: int, titular: str, saldo: float, limite: float):
        self.numero_conta = numero_conta
        self.__saldo = saldo
        self.__limite = limite
        self.titular = titular
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, saldo: float):
        self.__saldo = saldo
    
    def get_limite(self):
        return self.__limite
    
    def set_limite(self, limite):
        self.__limite = limite
    
    def depositar(self, valor: float):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido!")
    
    def sacar(self, valor: float):
        if valor > 0 and valor <= (self.__saldo + self.__limite):
            self.__saldo -= valor
        else:
            print("Valor inválido ou Saldo insuficiente!")
    
    def exibir_info(self):
        print(f"Conta:{self.numero_conta} \
            Titular:{self.titular} \
            Saldo:{self.__saldo} \
            Limite:{self.__limite }")

class ContaBancariaDAO:
    def __init__(self, conexao):
        self.conn = conexao.conn  # Acessa a conexão diretamente
        self.cursor = conexao.cursor  # Referencie o cursor diretamente, sem os parênteses
    
    def salvar_conta(self, conta):
        self.cursor.execute('''INSERT INTO contas 
            (numero_conta, titular, saldo, limite) 
            VALUES (?, ?, ?, ?)''',  # Corrigido para usar placeholders
            (conta.numero_conta, conta.titular, conta.get_saldo(), conta.get_limite()))
        self.conn.commit()
    
    def listar_contas(self):
        self.cursor.execute('''SELECT * FROM contas''')
        contas = self.cursor.fetchall()
        return contas

if __name__ == '__main__':
    conexao = conexaoBD()  # cria a conexão
    conexao.criar_tabela()  # cria a tabela contas

    conta1 = ContaBancaria(112344, "João Paulo", 2000, 5000)  # cria a conta1
    conta2 = ContaBancaria(22222, "Ana Maria", 5000, 15000)  # cria a conta2
    
    conta1.exibir_info()  # exibe informações da conta1

    conta1.depositar(300)  # deposita 300
    conta1.sacar(700)  # saca 700 da conta1

    conta1.exibir_info()  # exibe informações atualizadas

    conta_dao = ContaBancariaDAO(conexao)  # cria objeto dao_conta
    conta_dao.salvar_conta(conta1)  # salva conta1 no banco
    conta_dao.salvar_conta(conta2)  # salva conta2 no banco
    
    conexao.fechar_conexao()  # fecha a conexão

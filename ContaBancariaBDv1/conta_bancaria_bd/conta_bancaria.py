class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo, limite):
        self.numero_conta = numero_conta
        self.__saldo = saldo
        self.__limite = limite
        self.titular = titular
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, saldo):
        self.__saldo = saldo
    
    def get_limite(self):
        return self.__limite
    
    def set_limite(self, limite):
        self.__limite = limite
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido!")
    
    def sacar(self, valor):
        if valor > 0 and valor <= (self.__saldo + self.__limite):
            self.__saldo -= valor
        else:
            print("Valor inválido ou Saldo insuficiente!")
    
    def exibir_info(self):
        print(f"Conta:{self.numero_conta} \
            Titular:{self.titular} \
            Saldo:{self.__saldo} \
            Limite:{self.__limite }")

#conta = ContaBancaria(12345,"Paulo",500000,800000)
#conta.depositar(100000)
#conta.sacar(300000)
#print(conta.get_saldo())
#print(conta.exibir_info())

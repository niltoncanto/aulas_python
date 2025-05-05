class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo, limite):
        self.numero_conta = numero_conta  # Público
        self._saldo = saldo  # Protegido
        self.__limite = limite  # Privado
        self.nome_titular = nome_titular  # Público
    
    # Getter para saldo
    def get_saldo(self):
        return self._saldo
    
    # Setter para saldo
    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self._saldo = novo_saldo
        else:
            print("Saldo não pode ser negativo.")
    
    # Getter para limite (privado)
    def get_limite(self):
        return self.__limite
    
    # Setter para limite
    def set_limite(self, novo_limite):
        if novo_limite >= 0:
            self.__limite = novo_limite
        else:
            print("O limite não pode ser negativo.")
    
    # Método para depositar
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            print("Valor de depósito inválido.")
    
    # Método para sacar
    def sacar(self, valor):
        if 0 < valor <= (self._saldo + self.__limite):
            self._saldo -= valor
        else:
            print("Saque excede o saldo ou o limite.")
    
    # Exibir informações da conta
    def exibir_informacoes(self):
        print(f"Conta: {self.numero_conta}, Titular: {self.nome_titular}, Saldo: {self._saldo}, Limite: {self.__limite}")

from abc import ABC, abstractmethod
from datetime import datetime

# Interface Transacao
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

# Classes concretas para Saque e Deposito
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao({
                "tipo": "Saque",
                "valor": self.valor,
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            })
            print(f"Saque de R$ {self.valor} realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o saque.")

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao({
            "tipo": "Depósito",
            "valor": self.valor,
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })
        print(f"Depósito de R$ {self.valor} realizado com sucesso!")

# Classe Historico
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def mostrar_extrato(self):
        for transacao in self.transacoes:
            print(f'{transacao["data"]}\t{transacao["tipo"]}\tR$ {transacao["valor"]}')
        print('=' * 20)

# Classe Cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao: Transacao):
        transacao.registrar(conta)

# Classe PessoaFisica herdando de Cliente
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

# Classe Conta
class Conta:
    def __init__(self, numero, agencia, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def nova_conta(self, cliente, numero):
        return Conta(numero, self.agencia, cliente)

# Classe ContaCorrente herdando de Conta
class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite, limite_saques):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

# Simulador de operação
def main():
    # Criando um cliente
    cliente = PessoaFisica(cpf="12345678900", nome="João Silva", data_nascimento="01/01/1990", endereco="Rua A, 123")

    # Criando uma conta para o cliente
    conta = ContaCorrente(numero=1, agencia="0001", cliente=cliente, limite=500, limite_saques=5)
    cliente.adicionar_conta(conta)

    # Realizando um depósito
    deposito = Deposito(150)
    cliente.realizar_transacao(conta, deposito)

    # Realizando um saque
    saque = Saque(50)
    cliente.realizar_transacao(conta, saque)

    # Mostrando o extrato
    conta.historico.mostrar_extrato()

if __name__ == "__main__":
    main()

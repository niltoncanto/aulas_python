# Interface que define o contrato comum para todas as estratégias de cálculo de tarifas
from abc import ABC, abstractmethod

class EstrategiaCalculoTarifa(ABC):
    @abstractmethod
    def calcular_tarifa(self, valor_transacao):
        pass

# Classe de estratégia para calcular a tarifa padrão com base na porcentagem fixa
class TarifaPadraoStrategy(EstrategiaCalculoTarifa):
    def __init__(self, taxa_porcentagem):
        self.taxa_porcentagem = taxa_porcentagem

    def calcular_tarifa(self, valor_transacao):
        return valor_transacao * (self.taxa_porcentagem / 100.0)

# Classe de estratégia para calcular a tarifa VIP como uma taxa fixa
class TarifaVIPStrategy(EstrategiaCalculoTarifa):
    def __init__(self, taxa_fixa):
        self.taxa_fixa = taxa_fixa

    def calcular_tarifa(self, valor_transacao):
        return self.taxa_fixa

# Classe de estratégia para calcular a tarifa especial com base em uma fórmula complexa
class TarifaEspecialStrategy(EstrategiaCalculoTarifa):
    def calcular_tarifa(self, valor_transacao):
        # Implemente a lógica complexa de cálculo aqui
        # Esta é apenas uma implementação de exemplo
        return valor_transacao * 0.05  # 5% do valor da transação

# Classe principal que aceita a estratégia de cálculo de tarifa e calcula a tarifa com base na estratégia escolhida
class Pagamento:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def processar_pagamento(self, valor_transacao):
        return self.estrategia.calcular_tarifa(valor_transacao)

# Exemplo de uso:
if __name__=="__main__":
    # Crie uma instância da classe de pagamento com a estratégia desejada
    estrategia_padrao = TarifaPadraoStrategy(2.0)  # 2% de tarifa
    pagamento_padrao = Pagamento(estrategia_padrao)

    # Calcule a tarifa com base na estratégia escolhida
    valor_transacao = 1000.0
    tarifa = pagamento_padrao.processar_pagamento(valor_transacao)

    print("Tarifa Padrão: R$", tarifa)

    estrategia_vip = TarifaVIPStrategy(5.0)  # R$5.00 de tarifa VIP
    pagamento_vip = Pagamento(estrategia_vip)
    tarifa_vip = pagamento_vip.processar_pagamento(valor_transacao)
    print("Tarifa VIP: R$", tarifa_vip)

    estrategia_especial = TarifaEspecialStrategy()
    pagamento_especial = Pagamento(estrategia_especial)
    tarifa_especial = pagamento_especial.processar_pagamento(valor_transacao)
    print("Tarifa Especial: R$", tarifa_especial)

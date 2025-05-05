from abc import ABC,abstractmethod
class Pagamento:
    def __init__(self,estrategia):
        self.estrategia = estrategia

    def processar_pagamento(self,valor_transacao):
        return self.estrategia.calcular_tarifa(valor_transacao)

class EstrategiaCalculoTarifa(ABC):
    @abstractmethod
    def calcular_tarifa(self,valor_transacao):
        pass

class TarifaPadraoStrategy(EstrategiaCalculoTarifa):
    def __init__(self,taxa_porcentagem):
        self.taxa_porcentagem = taxa_porcentagem
    def calcular_tarifa(self,valor_transacao):
         return valor_transacao*self.taxa_porcentagem/100

class TarifaVIPStrategy(EstrategiaCalculoTarifa):
    def __init__(self,taxa_fixa):
        self.taxa_fixa = taxa_fixa
    def calcular_tarifa(self,valor_transacao):
        return self.taxa_fixa

class TarifaEspecialStrategy(EstrategiaCalculoTarifa):
    def __init__(self,taxa_variavel):
        self.taxa_variavel = taxa_variavel

    def calcular_tarifa(self,valor_transacao):
        return valor_transacao*self.taxa_variavel
    
if __name__=="__main__":
    tarifa = TarifaPadraoStrategy(2.0)
    pagamento = Pagamento(tarifa)
    valor_transacao = 1000.00
    taxa = pagamento.processar_pagamento(valor_transacao)
    print(taxa)
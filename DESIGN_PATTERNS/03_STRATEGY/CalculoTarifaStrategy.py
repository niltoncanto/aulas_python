# Importa o módulo ABC para a criação de classes abstratas e o decorador abstractmethod para métodos abstratos
from abc import ABC, abstractmethod

# Classe principal que gerencia o processo de pagamento, utilizando uma estratégia específica para calcular tarifas
class Pagamento:
    def __init__(self, estrategia):
        # O método construtor recebe uma instância de estratégia e a armazena como um atributo
        self.estrategia = estrategia
    
    def processar_pagamento(self, valor_transacao):
        # Método que processa o pagamento chamando o método calcular_tarifa da estratégia específica
        return self.estrategia.calcular_tarifa(valor_transacao)

# Classe abstrata que define a interface padrão para todas as estratégias de cálculo de tarifa
class EstrategiaCalculoTarifa(ABC):
    @abstractmethod
    def calcular_tarifa(self, valor_transacao):
        # Método abstrato que deve ser implementado por todas as subclasses. Define a assinatura do método de cálculo de tarifa.
        pass

# Implementação concreta de uma estratégia de cálculo de tarifa padrão com base em uma porcentagem
class TarifaPadraoStrategy(EstrategiaCalculoTarifa):
    def __init__(self, taxa_porcentagem):
        # Inicializa a taxa de porcentagem a ser aplicada
        self.taxa_porcentagem = taxa_porcentagem
    
    def calcular_tarifa(self, valor_transacao):
        # Calcula a tarifa com base em uma porcentagem da transação
        return valor_transacao * self.taxa_porcentagem / 100

# Implementação concreta de uma estratégia de cálculo de tarifa VIP com uma tarifa fixa
class TarifaVIPStrategy(EstrategiaCalculoTarifa):
    def __init__(self, taxa_fixa):
        # Inicializa a taxa fixa a ser aplicada
        self.taxa_fixa = taxa_fixa
    
    def calcular_tarifa(self, valor_transacao):
        # Retorna a tarifa fixa independentemente do valor da transação
        return self.taxa_fixa

# Implementação concreta de uma estratégia de cálculo de tarifa especial com uma taxa variável
class TarifaEspecialStrategy(EstrategiaCalculoTarifa):
    def __init__(self, taxa_variavel):
        # Inicializa a taxa variável a ser aplicada
        self.taxa_variavel = taxa_variavel
    
    def calcular_tarifa(self, valor_transacao):
        # Calcula a tarifa com base na taxa variável multiplicada pelo valor da transação
        return valor_transacao * self.taxa_variavel

# Código de teste para verificar o funcionamento das classes e estratégias
if __name__ == "__main__":
    # Cria uma instância de TarifaPadraoStrategy com uma taxa de 2%
    tarifa = TarifaPadraoStrategy(2.0)
    
    # Cria uma instância da classe Pagamento usando a estratégia de tarifa padrão
    pagamento = Pagamento(tarifa)
    
    # Define o valor da transação
    valor_transacao = 1000.00
    
    # Calcula e imprime a tarifa aplicada à transação
    taxa = pagamento.processar_pagamento(valor_transacao)
    print(taxa)  # Saída esperada: 20.0, que é 2% de 1000.00


    '''
    Explicação do Padrão Strategy
    O padrão de projeto Strategy permite definir uma família de algoritmos, encapsulá-los em classes separadas e torná-los intercambiáveis. 
    Neste exemplo, temos diferentes estratégias de cálculo de tarifa (TarifaPadraoStrategy, TarifaVIPStrategy, TarifaEspecialStrategy) 
    que podem ser usadas de forma flexível pela classe Pagamento. Isso proporciona uma maneira de estender ou modificar o comportamento de 
    cálculo de tarifa sem alterar a estrutura da classe principal Pagamento.
    '''

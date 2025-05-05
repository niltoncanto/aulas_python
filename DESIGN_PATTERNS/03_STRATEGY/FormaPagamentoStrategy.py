from abc import ABC, abstractmethod

# Passo 1: Interface/Forma abstrata
class FormaPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor_pedido):
        pass

# Passo 2: Implementação das estratégias
class CartaoCreditoStrategy(FormaPagamento):
    def processar_pagamento(self, valor_pedido):
        # Lógica de processamento para cartão de crédito
        return f"Pagamento de R${valor_pedido} realizado com cartão de crédito."

class PayPalStrategy(FormaPagamento):
    def processar_pagamento(self, valor_pedido):
        # Lógica de processamento para PayPal
        return f"Pagamento de R${valor_pedido} realizado com PayPal."

class TransferenciaBancariaStrategy(FormaPagamento):
    def processar_pagamento(self, valor_pedido):
        # Lógica de processamento para transferência bancária
        return f"Pagamento de R${valor_pedido} realizado via transferência bancária."

# Passo 3: Classe LojaOnline
class LojaOnline:
    def __init__(self, estrategia_pagamento):
        self.estrategia_pagamento = estrategia_pagamento

    def finalizar_compra(self, valor_pedido):
        mensagem_confirmacao = self.estrategia_pagamento.processar_pagamento(valor_pedido)
        return mensagem_confirmacao

# Passo 4: teste
if __name__ == "__main__":
    cartao_credito = CartaoCreditoStrategy()
    loja = LojaOnline(cartao_credito)
    valor_pedido = 100.0
    mensagem_confirmacao = loja.finalizar_compra(valor_pedido)
    print(mensagem_confirmacao)

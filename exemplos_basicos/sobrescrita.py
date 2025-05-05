# Classe Pai
class Payment:
    def process_payment(self, amount):
        return f"Processando pagamento de {amount} reais"

# Classe Filha
class CreditCardPayment(Payment):
    # Sobrescrevendo o método process_payment()
    def process_payment(self, amount):
        return f"Processando pagamento de {amount} reais via cartão de crédito"

# Classe Filha
class BankTransferPayment(Payment):
    # Sobrescrevendo o método process_payment()
    def process_payment(self, amount):
        return f"Processando pagamento de {amount} reais via transferência bancária"

# Testando a sobrescrita de métodos
payment1 = CreditCardPayment()
payment2 = BankTransferPayment()

print(payment1.process_payment(100))  # Saída: Processando pagamento 
print(payment2.process_payment(250))  # Saída: Processando pagamento

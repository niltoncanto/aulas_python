from abc import ABC, abstractmethod

# Classe abstrata Notifier (Notificador) que define o método abstrato 'send' (enviar).
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Implementação concreta de Notifier para envio de e-mails.
class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Enviando e-mail com a mensagem: {message}")

# Implementação concreta de Notifier para envio de SMS.
class SMSNotifier(Notifier):
    def send(self, message):
        print(f"Enviando SMS com a mensagem: {message}")

# Implementação concreta de Notifier para não enviar notificação.
class NullNotifier(Notifier):
    def send(self, message):
        # Nenhuma notificação é enviada
        pass

# Factory Method responsável por criar objetos Notifier com base no tipo fornecido.
class NotifierFactory:
    def get_notifier(self, type):
        if type == "email":
            return EmailNotifier()
        elif type == "sms":
            return SMSNotifier()
        else:
            return NullNotifier()

# Função cliente que utiliza um objeto Notifier para enviar uma mensagem.
def client_code(notifier, message):
    notifier.send(message)

# Uso do sistema de notificação:
# 1. Criamos uma instância da fábrica de notificadores.
factory = NotifierFactory()
# 2. Usamos a fábrica para obter um notificador do tipo "email".
notifier = factory.get_notifier("email")
# 3. Chamamos a função cliente para enviar uma mensagem usando o notificador obtido.
client_code(notifier, "Olá! Este é um teste de notificação.")

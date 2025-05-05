 #sem princípio de inversão de dependência
class EmailNotifier:
    def send(self, message):
        print(f"Enviando e-mail: {message}")

class SMSNotifier:
    def send(self, message):
        print(f"Enviando SMS: {message}")

class NotificationService:
    def __init__(self, notifier_type):
        if notifier_type == "email":
            self.notifier = EmailNotifier()
        elif notifier_type == "sms":
            self.notifier = SMSNotifier()

    def notify(self, message):
        self.notifier.send(message)

# Usando o serviço de notificação
service = NotificationService("email")
service.notify("Olá, você tem uma nova notificação!")

#com 

from abc import ABC, abstractmethod
# Abstração (interface)
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass
# Módulos de baixo nível
class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Enviando e-mail: {message}")
class SMSNotifier(Notifier):
    def send(self, message):
        print(f"Enviando SMS: {message}")
# Módulo de alto nível
class NotificationService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def notify(self, message):
        self.notifier.send(message)
# Usando o serviço de notificação
email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()
service = NotificationService(email_notifier)
service.notify("Olá, você tem uma nova notificação por e-mail!")
service_sms = NotificationService(sms_notifier)
service_sms.notify("Olá, você tem uma nova notificação por SMS!")

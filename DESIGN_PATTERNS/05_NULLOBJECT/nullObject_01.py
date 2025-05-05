from abc import ABC, abstractmethod
class Notifier(ABC):
    @abstractmethod
    def send(self,mensagem):
        pass
class EmailNotifier():
    def send(self,mensagem):
        print(f"Enviando msg email {mensagem}")
class SMSNotifier():
    def send(self,mensagem):
        print(f"Enviando msg SMS {mensagem}")
class NULLNotifier():
    def send(self,mensagem):
        pass

class FactoryNotifier:
    def get_notifier(self,type):
        if type=='email':
            return EmailNotifier()
        elif type=='SMS':
            return SMSNotifier()
        else:
            return NULLNotifier()


if __name__=="__main__":
    notificacao = FactoryNotifier()
    notificacao.get_notifier("email").send("teste email...")
    notificacao.get_notifier("sms").send("teste sms...")
    notificacao.get_notifier("Null").send("teste nada...")

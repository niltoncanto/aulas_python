from abc import ABC, abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self, leilao, preco):
        pass
class Leilao:
    def __init__(self, nome):
        self.nome = nome
        self._observers = []
        self._preco = 0
    def register_observer(self, observer):
        self._observers.append(observer)
    def remove_observer(self, observer):
        self._observers.remove(observer)
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self, self._preco)
    def set_preco(self, preco):
        self._preco = preco
        self.notify_observers()
class Usuario(Observer):
    def __init__(self, nome):
        self.nome = nome
    def update(self, leilao, preco):
        print(f"{self.nome} foi notificado que o preço do leilão \
              '{leilao.nome}' agora é {preco}")
if __name__ == "__main__":
    leilao = Leilao("Leilão de Arte")
    alice = Usuario("Alice")
    bob = Usuario("Bob")
    carol = Usuario("Carol")
    leilao.register_observer(alice)
    leilao.register_observer(bob)
    leilao.set_preco(100)  # Alice e Bob são notificados
    leilao.register_observer(carol)
    leilao.remove_observer(bob)
    leilao.set_preco(150)  # Alice e Carol são notificados

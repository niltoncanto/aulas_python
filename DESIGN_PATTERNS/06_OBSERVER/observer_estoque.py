from abc import ABC, abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self, product):
        pass
class Product:
    def __init__(self, name, threshold):
        self.name = name
        self.threshold = threshold
        self._observers = []
        self._stock = 0
    def register_observer(self, observer):
        self._observers.append(observer)
    def remove_observer(self, observer):
        self._observers.remove(observer)
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)
    def set_stock(self, stock):
        self._stock = stock
        if self._stock < self.threshold:
            self.notify_observers()
class Department(Observer):
    def __init__(self, name):
        self.name = name
    def update(self, product):
        if product._stock < product.threshold:
            print(f"Departamento {self.name} alertado: Estoque baixo para \
                  {product.name}, apenas {product._stock} unidades restantes.")
if __name__ == "__main__":
    widget = Product("Widget", 50)
    sales = Department("Vendas")
    logistics = Department("Logística")
    widget.register_observer(sales)
    widget.register_observer(logistics)
    widget.set_stock(60)  # Não gera notificação
    widget.set_stock(45)  # Gera notificação para ambos os departamentos

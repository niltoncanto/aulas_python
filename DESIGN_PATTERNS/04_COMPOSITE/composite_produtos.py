from abc import ABC, abstractmethod

# Component
class CatalogComponent(ABC):
    @abstractmethod
    def show_details(self) -> None:
        pass

# Leaf
class Product(CatalogComponent):
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def show_details(self) -> None:
        print(f"Product: {self.name}, Price: ${self.price:.2f}")

# Composite
class Category(CatalogComponent):
    def __init__(self, name: str) -> None:
        self.name = name
        self._components = []

    def add(self, component: CatalogComponent) -> None:
        self._components.append(component)

    def remove(self, component: CatalogComponent) -> None:
        self._components.remove(component)

    def show_details(self) -> None:
        print(f"Category: {self.name}")
        for component in self._components:
            component.show_details()

# Client code
if __name__ == "__main__":
    product1 = Product("Laptop", 1500.00)
    product2 = Product("Smartphone", 700.00)
    product3 = Product("Tablet", 300.00)

    electronics = Category("Electronics")
    computers = Category("Computers")
    phones = Category("Phones")

    computers.add(product1)
    phones.add(product2)
    electronics.add(computers)
    electronics.add(phones)
    electronics.add(product3)

    electronics.show_details()

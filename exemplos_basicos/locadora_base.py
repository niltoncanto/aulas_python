from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    @abstractmethod
    def exibir_informacoes(self):
        pass

    # Implemente os getters e setters para marca, modelo e ano

# Crie as classes Carro, Moto e Caminhao, herdando de Veiculo

# Exemplo de implementação para a classe Carro (implemente métodos similares para Moto e Caminhao):
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.__portas = portas

    def exibir_informacoes(self):
        print(f"Carro: {self.__marca} {self.__modelo} Ano: {self.__ano} Portas: {self.__portas}")

    # Implemente o getter e setter para portas




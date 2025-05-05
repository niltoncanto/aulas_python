from abc import ABC, abstractmethod
from datetime import datetime

# Classe abstrata Veiculo
class Veiculo(ABC):
    quantidade_veiculos = 0  # Atributo de classe
    
    def __init__(self, modelo, ano, valor):
        if not Veiculo.validar_ano(ano):
            raise ValueError("Ano do veículo inválido!")
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        Veiculo.quantidade_veiculos += 1  # Incrementa a quantidade de veículos

    @abstractmethod
    def calcular_seguro(self):
        pass  # Será implementado nas subclasses

    @staticmethod
    def validar_ano(ano):
        ano_atual = datetime.now().year
        return 1886 <= ano <= ano_atual

    @classmethod
    def total_veiculos(cls):
        return cls.quantidade_veiculos

# Subclasse Carro
class Carro(Veiculo):
    def calcular_seguro(self):
        return self.valor * 0.05  # Exemplo de cálculo de seguro para Carro

# Subclasse Caminhão
class Caminhão(Veiculo):
    def calcular_seguro(self):
        return self.valor * 0.1  # Exemplo de cálculo de seguro para Caminhão

# Subclasse Moto
class Moto(Veiculo):
    def calcular_seguro(self):
        return self.valor * 0.03  # Exemplo de cálculo de seguro para Moto

# Teste do sistema
def main():
    carro1 = Carro("Sedan", 2020, 50000)
    caminhao1 = Caminhão("Truck", 2015, 120000)
    moto1 = Moto("Esportiva", 2018, 30000)
    
    print(f"Seguro do Carro: R${carro1.calcular_seguro():.2f}")
    print(f"Seguro do Caminhão: R${caminhao1.calcular_seguro():.2f}")
    print(f"Seguro da Moto: R${moto1.calcular_seguro():.2f}")
    
    print(f"Total de veículos cadastrados: {Veiculo.total_veiculos()}")

if __name__ == "__main__":
    main()

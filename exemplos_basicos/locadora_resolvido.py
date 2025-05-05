from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano

    @abstractmethod
    def exibir_informacoes(self):
        pass

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def ano(self):
        return self._ano

    # Setters
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @ano.setter
    def ano(self, ano):
        self._ano = ano

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self._portas = portas

    def exibir_informacoes(self):
        print(f"Carro: Marca: {self._marca}, Modelo: {self._modelo}, Ano: {self._ano}, Portas: {self._portas}")

    @property
    def portas(self):
        return self._portas

    @portas.setter
    def portas(self, portas):
        self._portas = portas

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self._cilindradas = cilindradas

    def exibir_informacoes(self):
        print(f"Moto: Marca: {self._marca}, Modelo: {self._modelo}, Ano: {self._ano}, Cilindradas: {self._cilindradas}")

    @property
    def cilindradas(self):
        return self._cilindradas

    @cilindradas.setter
    def cilindradas(self, cilindradas):
        self._cilindradas = cilindradas

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, capacidade_carga):
        super().__init__(marca, modelo, ano)
        self._capacidade_carga = capacidade_carga

    def exibir_informacoes(self):
        print(f"Caminhao: Marca: {self._marca}, Modelo: {self._modelo}, Ano: {self._ano}, Capacidade de Carga: {self._capacidade_carga}Kg")

    @property
    def capacidade_carga(self):
        return self._capacidade_carga

    @capacidade_carga.setter
    def capacidade_carga(self, capacidade_carga):
        self._capacidade_carga = capacidade_carga

def main():
    veiculos = [
        Carro("Ford", "Fiesta", 2018, 4),
        Moto("Honda", "CB500", 2019, "500cc"),
        Caminhao("Mercedes", "Actros", 2020, 30000)
    ]

    for veiculo in veiculos:
        veiculo.exibir_informacoes()

if __name__ == "__main__":
    main()





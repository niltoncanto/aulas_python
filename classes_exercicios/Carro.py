class Carro:
    # Construtor para inicializar os atributos
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False  # Carro começa desligado

    # Método para ligar o carro
    def ligar(self):
        self.ligado = True
        print("Carro ligado!")

    # Método para desligar o carro
    def desligar(self):
        self.ligado = False
        print("Carro desligado!")

    # Método para mostrar informações do carro
    def mostrar_info(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nLigado: {'Sim' if self.ligado else 'Não'}")


# Testando a classe Carro
meu_carro = Carro("Ford", "Fiesta", 2020)
meu_carro.mostrar_info()
meu_carro.ligar()
meu_carro.mostrar_info()

class Animal:
    # Construtor para inicializar os atributos
    def __init__(self, nome, tipo, som):
        self.nome = nome
        self.tipo = tipo
        self.som = som

    # Método para fazer o animal emitir o som
    def fazer_som(self):
        print(f"{self.nome} faz {self.som}!")

    # Método para alimentar o animal
    def alimentar(self):
        print(f"Alimentando {self.nome}")

    # Método para fazer o animal dormir
    def dormir(self):
        print(f"{self.nome} está dormindo.")

    # Método para mostrar informações do animal
    def mostrar_info(self):
        print(f"Nome: {self.nome}\nTipo: {self.tipo}\nSom: {self.som}")


# Testando a classe Animal
meu_animal = Animal("Rex", "Mamífero", "Latido")
meu_animal.mostrar_info()
meu_animal.fazer_som()


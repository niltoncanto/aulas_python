'''
1. Classe Animal: 
   - Atributos:
     - `nome`: Representa o nome do animal (por exemplo, "Rex").
     - `tipo`: Define a classificação do animal (como "Mamífero", "Réptil", etc.).
     - `som`: Descreve o som característico que o animal faz (como "Latido", "Miado", etc.).
   - Construtor:
     - Inicializa os atributos `nome`, `tipo`, e `som`.
   - Métodos:
     - `setSom(String som)`: Permite alterar o som do animal.
     - `fazerSom()`: Imprime a ação de o animal fazer o seu som característico.
     - `alimentar()`: Imprime a ação de alimentar o animal.
     - `dormir()`: Imprime a ação do animal dormindo.
     - `mostrarInfo()`: Imprime as informações do animal.
'''
class Animal:
    def __init__(self, nome, tipo, som):
        self.nome = nome
        self.tipo = tipo
        self.som = som
    
    def setSom(self, som):
        self.som = som  

    def fazerSom(self):
        print(f"{self.nome} fazendo som: {self.som}")

    def alimentar(self):
        print(f"{self.nome} sendo alimentado")

    def dormir(self):
        print(f"{self.nome} dormindo")

    def mostrarInfo(self):
        print(f"Nome: {self.nome}")
        print(f"Tipo: {self.tipo}")
        print(f"Som: {self.som}")

# Testando a classe Animal
if __name__ == "__main__":
    a1 = Animal("Rex", "Mamífero", "Latido")
    a1.mostrarInfo()
    a1.fazerSom()
    a1.alimentar()
    a1.dormir()
    print()
    
    a2 = Animal("Mimi", "Mamífero", "Miado")
    a2.mostrarInfo()
    a2.fazerSom()
    a2.alimentar()
    a2.dormir()
    print()
    
    a3 = Animal("Tico", "Ave", "Canto")
    a3.mostrarInfo()
    a3.fazerSom()
    a3.alimentar()
    a3.dormir()
    print()
    
    a4 = Animal("Nemo", "Peixe", "Blub")
    a4.mostrarInfo()
    a4.fazerSom()
    a4.alimentar()
    a4.dormir()
    print()






















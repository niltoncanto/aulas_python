# Objetivo: Estudo de Classes e Métodos - Faça um programa em Python com as seguintes especificações:

# classe chamada Ponto, com os atributos x e y (coordenadas do ponto).
# classe chamada Retangulo, com os atributos largura e altura.
# método que retorna as coordenadas do Ponto.
# método que retorna o centro de um Retângulo.

# Cada objeto retângulo deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
# A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
# Crie um menu que permita:
    # 1. criar o retângulo
    # 2. calcular o centro do retângulo
    # 3. alterar o vértice, largura e altura do retângulo
    # 4. sair do sistema

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def imprimir_ponto(self):
        print(f"({self.x}, {self.y})")

class Retangulo:
    def __init__(self, ponto_inferior_esquerdo, largura, altura):
        self.ponto_inferior_esquerdo = ponto_inferior_esquerdo
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        centro_x = self.ponto_inferior_esquerdo.x + self.largura / 2
        centro_y = self.ponto_inferior_esquerdo.y + self.altura / 2
        return Ponto(centro_x, centro_y)

# Menu
class Menu:

    @staticmethod
    def menu():
        # Criando alguns objetos Retangulo
        retangulo1 = Retangulo(Ponto(0, 0), 10, 5)
        retangulo2 = Retangulo(Ponto(5, 5), 8, 3)

        while True:
            print("\nMenu:")
            print("1. Criar retangulo")
            print("2. Imprimir Centro")
            print("3. Alterar valores do Retângulo")
            print("4. Sair")
            escolha = input("Escolha uma opção: ")
            if escolha == '1':
                x = float(input("Digite o novo x para o vértice inferior esquerdo do Retângulo: "))
                y = float(input("Digite o novo y para o vértice inferior esquerdo do Retângulo: "))
                largura = float(input("Digite a nova largura do Retângulo: "))
                altura = float(input("Digite a nova altura do Retângulo: "))
                ponto = Ponto(x, y)
                retangulo = Retangulo(ponto, largura, altura)
            elif escolha == '2':
                try:
                    centro = retangulo.encontrar_centro()
                    print(centro.x,centro.y)
                except NameError:
                    print("meu_objeto não existe, crie primeiro o retângulo.")
            elif escolha == '3':
                x = float(input("Digite o novo x para o vértice inferior esquerdo do Retângulo: "))
                y = float(input("Digite o novo y para o vértice inferior esquerdo do Retângulo: "))
                largura = float(input("Digite a nova largura do Retângulo: "))
                altura = float(input("Digite a nova altura do Retângulo: "))
                retangulo.ponto_inferior_esquerdo = Ponto(x, y)
                retangulo.largura = largura
                retangulo.altura = altura
            elif escolha == '4':
                break
            else:
                print("Opção inválida!")

Menu.menu()

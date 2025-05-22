# sistema_refatorado.py

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def contem_item(self, item):
        return item in self.itens

    def exibir_nome(self):
        print("Nome do usuário:", self.nome)


class CalculadoraTempo:
    def calcular_tempo(self):
        tempo = 0
        for i in range(5):
            tempo += i * 2
        print("Tempo calculado:", tempo)

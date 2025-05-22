# sistema.py

class S:
    def __init__(self):
        self.x = []
        self.n = "João"
        self.t = 0  # tempo total (não usado)

    def a(self, y):
        # verifica se y está na lista
        if y in self.x:
            return True
        else:
            return False

    def b(self, y):
        # adiciona à lista, mas não é mais usado
        self.x.append(y)

    def c(self):
        # método faz duas coisas: imprime nome e calcula tempo
        print("Nome do usuário:", self.n)
        tempo = 0
        for i in range(5):
            tempo += i * 2
        print("Tempo calculado:", tempo)

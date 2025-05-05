class Usuario:
    def __init__(self, nome, ID):
        self.nome = nome
        self.ID = ID

    def fazerReserva(self, livro):
        return livro.reservar()
    
    def fazerDevolucao(self,livro):
        return livro.devolver()

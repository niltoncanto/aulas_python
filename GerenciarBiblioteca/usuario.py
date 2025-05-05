class Usuario:
    ID = 10000
    def __init__(self, nome):
        self.nome = nome
        Usuario.ID += 1

    def to_string(self):
        return f"{self.nome};{self.ID}\n"

    def fazerReserva(self, livro):
        print(livro.reservar())

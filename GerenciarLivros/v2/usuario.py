class Usuario:
    def __init__(self,id,nome):
        self.id = id
        self.nome = nome
    
    def fazerReserva(self,livro):
        return livro.reservar()
    
    def fazerDevolucao(self,livro):
        return livro.devolver()

    def __str__(self):
        return f"{self.nome}, {self.ID}"

    

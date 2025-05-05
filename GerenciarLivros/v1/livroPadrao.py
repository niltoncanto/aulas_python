from livro import Livro, Status
from datetime import datetime, timedelta

class LivroPadrao(Livro):
    def __init__(self, titulo, autor, ISBN):
        super().__init__(titulo, autor, ISBN)
        self.dataDeDevolucao = None

    def reservar(self):
        if self.status == Status.DISPONIVEL:
            self.status = Status.RESERVADO
            self.dataDeDevolucao = datetime.now() + timedelta(days=7)
            return f"Livro reservado com sucesso. Data de devolução: {self.dataDeDevolucao}"
        else:
            return "Livro já está reservado."

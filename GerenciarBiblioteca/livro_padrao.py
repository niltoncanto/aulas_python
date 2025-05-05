from livro import Livro,Status
from datetime import datetime,timedelta

class LivroPadrao(Livro):
    def __init__(self, titulo, autor, ISBN):
        super().__init__(titulo, autor, ISBN)
        self.dataDeDevolucao = datetime.now() + timedelta(days=7)

    def to_string(self):
        return super().to_string() + "Padrão";self.dataDeDevolucao
        
    def reservar(self):
        if self.status == Status.DISPONIVEL:
            self.status = Status.RESERVADO
            return "Livro reservado com sucesso."
        else:
            return "Livro já está reservado."

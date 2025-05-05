from livro import Livro,Status
from datetime import datetime,timedelta

#classe LivroPadrao herda classe Livro
class LivroPadrao(Livro):
    def __init__(self,titulo,autor,isbn):
        super().__init__(titulo,autor,isbn)
        self.dataDevolucao = None
        
    def reservar(self):
        if self.status==Status.DISPONIVEL:
            self.status = Status.RESERVADO
            self.dataDevolucao = datetime.now() + timedelta(days=7)
            return f"Reserva realizada, devolver ate:{self.dataDevolucao}"
        else:
            return "Livro indisponível"
from datetime import datetime,timedelta
from livro import Status,Livro
#classe LivroPadrao herda classe Livro
class LivroPadrao(Livro):
    def __init__(self,titulo,autor,isbn):
        super().__init__(titulo,autor,isbn)
        
        
    def reservar(self):
        if self.status == Status.DISPONIVEL:
            self.status = Status.RESERVADO
            self.dataDevolucao = datetime.now() + timedelta(days=7)
            return f"Livro reservado, devolucao em:{self.dataDevolucao}"
        else:
            return "livro indisponível"

    


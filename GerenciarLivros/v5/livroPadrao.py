from livro import Livro
from datetime import datetime, timedelta
class livroPadrao(Livro):
    def __init__(self,titulo,autor,isbn):
        super().__init__(titulo,autor,isbn)
        self.data_devolucao = None
        pass
    
    def reservar(self):
        pass
    
    def devolver(self):
        data_devolucao = datetime.now() + timedelta(days=7)
    
